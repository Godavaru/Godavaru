"""
NOTICE:
    The following is taken with minor (to no) modification from https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py:
        cleanup_code
        get_syntax_error
        _eval
        repl
"""
import datetime
import io
import inspect
import os
import sys
import textwrap
import traceback
import subprocess
import pymysql
import asyncio
from prettytable import PrettyTable
from contextlib import redirect_stdout

import discord
from discord.ext import commands
from .utils.tools import resolve_emoji

import config


def is_owner(ctx):
    return ctx.author.id in config.owners


class Owner:
    def __init__(self, bot):
        self.bot = bot
        self.last_result = None
        self.sessions = set()

    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

    @commands.command(name="eval", aliases=["ev", "debug"])
    @commands.check(is_owner)
    async def _eval(self, ctx, *, code):
        """Evaluate code. (Bot Owner Only)"""
        env = {
            'self': self,
            'bot': self.bot,
            'client': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'guild': ctx.guild,
            'channel': ctx.channel,
            'author': ctx.author,
            'me': ctx.me,
            'that': self.last_result
        }
        env.update(globals())

        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(code, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            err = "; ".join(str(e).split("\n"))
            return await ctx.send(f"Error while executing: `{e.__class__.__name__}: {err}`")

        before = datetime.datetime.utcnow()
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            err = "; ".join(str(e).split("\n"))
            return await ctx.send(f"Error while executing: `{e.__class__.__name__}: {err}`")
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    if isinstance(value, str):
                        value = "'" + value.replace("'", "\\'") + "'"
                    content = f"{value}"
                    self.last_result = value
                else:
                    content = None
            else:
                y = ret if not isinstance(ret, str) else "'" + ret.replace("'", "\\'") + "'"
                content = f"{value}{y}"
                self.last_result = ret
            try:
                await ctx.send(f"*Executed in {((datetime.datetime.utcnow() - before) * 1000).total_seconds()}ms" + (
                    f".* ```py\n{content}```" if content else " with no returns.*"))
            except discord.HTTPException:
                await ctx.send("*Executed in {}ms and returned:*\nContent too long. Haste: ".format(
                    ((datetime.datetime.utcnow() - before) * 1000).total_seconds()) + self.bot.post_to_haste(content))

    @commands.command()
    @commands.check(is_owner)
    async def repl(self, ctx):
        """Launches an interactive REPL session."""
        variables = {
            'ctx': ctx,
            'bot': self.bot,
            'message': ctx.message,
            'guild': ctx.guild,
            'channel': ctx.channel,
            'author': ctx.author,
            '_': None,
        }

        if ctx.channel.id in self.sessions:
            await ctx.send('Already running a REPL session in this channel. Exit it with `quit`.')
            return

        self.sessions.add(ctx.channel.id)
        await ctx.send('Enter code to execute or evaluate. `exit()` or `quit` to exit.')

        def check(m):
            return m.author.id == ctx.author.id and \
                   m.channel.id == ctx.channel.id

        while True:
            try:
                response = await self.bot.wait_for('message', check=check, timeout=10.0 * 60.0)
            except asyncio.TimeoutError:
                await ctx.send('Timed out, exiting REPL session.')
                self.sessions.remove(ctx.channel.id)
                break

            cleaned = self.cleanup_code(response.content)

            if cleaned in ('quit', 'exit', 'exit()'):
                await ctx.send('Exiting.')
                self.sessions.remove(ctx.channel.id)
                return

            executor = exec
            if cleaned.count('\n') == 0:
                # single statement, potentially 'eval'
                try:
                    code = compile(cleaned, '<repl session>', 'eval')
                except SyntaxError:
                    pass
                else:
                    executor = eval

            if executor is exec:
                try:
                    code = compile(cleaned, '<repl session>', 'exec')
                except SyntaxError as e:
                    await ctx.send(self.get_syntax_error(e))
                    continue

            variables['message'] = response

            fmt = None
            stdout = io.StringIO()

            try:
                with redirect_stdout(stdout):
                    result = executor(code, variables)
                    if inspect.isawaitable(result):
                        result = await result
            except Exception as e:
                value = stdout.getvalue()
                fmt = f'```py\n{value}{traceback.format_exc()}\n```'
            else:
                value = stdout.getvalue()
                if result is not None:
                    fmt = f'```py\n{value}{result}\n```'
                    variables['_'] = result
                elif value:
                    fmt = f'```py\n{value}\n```'

            try:
                if fmt is not None:
                    if len(fmt) > 2000:
                        await ctx.send('Content too long. Haste: ' + await self.bot.post_to_haste(fmt))
                    else:
                        await ctx.send(fmt)
            except discord.Forbidden:
                pass
            except discord.HTTPException as e:
                await ctx.send(f'Unexpected error: `{e}`')

    @commands.command(name="exec")
    @commands.check(is_owner)
    async def _exec(self, ctx, *, code: str):
        """Execute code in a command shell. (Bot Owner Only)"""
        sp = subprocess.Popen(code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            out, err = sp.communicate(timeout=8)
            sp.terminate()
        except subprocess.TimeoutExpired:
            sp.kill()
            return await ctx.send('S-sorry! The command timed out... I-I\'ll try harder next time!')
        msg = "Executing...\n"
        if out:
            msg += 'Success! ```\n{}```\n'.format(out.decode())
        if err:
            msg += 'Error/Info/Warn! ```\n{}```\n'.format(err.decode())
        msg += "Returncode: {}".format(sp.returncode)
        await ctx.send(msg)

    @commands.command(aliases=["die", "reboot"])
    @commands.check(is_owner)
    async def shutdown(self, ctx):
        """Shutdown the bot. Thanks to PM2, this also reboots it. (Bot Owner Only)"""
        await ctx.send(":wave: Shutting down...")
        self.bot.logout()
        sys.exit(0)

    @commands.command(aliases=['db', 'dbquery'])
    @commands.check(is_owner)
    async def query(self, ctx, *, query: str):
        """Query the MySQL database. (Bot Owner Only)"""
        try:
            db = pymysql.connect(config.db_ip, config.db_user, config.db_pass, config.db_name, charset='utf8mb4')
            cur = db.cursor()
            cur.execute(query)
            table = ":x: Nothing was returned in this query."
            if cur.description:
                desc = list(cur.description)
                x = []
                for it in desc:
                    l = list(it)
                    x.append(l[0])
                table = PrettyTable(x)
                for row in cur.fetchall():
                    table.add_row(list(row))
            db.commit()
            cur.close()
            db.close()
            try:
                await ctx.send(f"```\n{table}```")
            except discord.HTTPException:
                await ctx.send(f'Content too long. Hastepaste: ' + await self.bot.post_to_haste(table))
        except pymysql.err.ProgrammingError as e:
            err_msg = str(e).split(',')[1].replace(')', '').replace('"', '')
            await ctx.send(f":x: {err_msg}")

    @commands.command()
    @commands.check(is_owner)
    async def reload(self, ctx, *, extension: str):
        """Reload an extension (Bot Owner Only)"""
        if extension != "all":
            try:
                self.bot.unload_extension('cogs.' + extension)
                self.bot.load_extension('cogs.' + extension)
                await ctx.send(f":ok_hand: Reloaded /cogs/{extension}.py")
            except Exception:
                await ctx.send(f":sob: I-I'm sorry, I couldn't reload the `{extension}` extensions >w< "
                               + f"```py\n{traceback.format_exc()}```")
        else:
            extensions = [f for f in os.listdir('./cogs') if f.endswith('.py')]
            for ext in extensions:
                try:
                    self.bot.unload_extension('cogs.' + ext[:-3])
                    self.bot.load_extension('cogs.' + ext[:-3])
                except:
                    await ctx.send(
                        f'I ran into an error reloading the {ext[:-3]} extension. ```py\n{traceback.format_exc()}```')
                    continue
            await ctx.send(':white_check_mark: Reloaded all extensions.')

    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, *, extension: str):
        """Unload an extension (Bot Owner Only)"""
        self.bot.unload_extension("cogs." + extension)
        await ctx.send(f":ok_hand: Unloaded /cogs/{extension}.py")

    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, *, extension: str):
        """Load an extension (Bot Owner Only)"""
        try:
            self.bot.load_extension("cogs." + extension)
            await ctx.send(f":ok_hand: Loaded /cogs/{extension}.py")
        except Exception:
            await ctx.send(f":sob: I-I'm sorry, I couldn't load the `{extension}` module >w< "
                           + f"```py\n{traceback.format_exc()}```")


def setup(bot):
    bot.add_cog(Owner(bot))
