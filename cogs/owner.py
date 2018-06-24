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


def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'


def cleanup_code(content):
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
    return content.strip('` \n')


class Owner:
    def __init__(self, bot):
        self.bot = bot
        self.last_result = None
        self.sessions = set()

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
                    ((datetime.datetime.utcnow() - before) * 1000).total_seconds()) + await self.bot.post_to_haste(
                    content))

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
            return await ctx.send(
                resolve_emoji('ERROR', ctx) + ' S-sorry! The command timed out... I-I\'ll try harder next time!')
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
            table = None
            if cur.description:
                desc = list(cur.description)
                x = []
                for it in desc:
                    item = list(it)
                    x.append(item[0])
                table = PrettyTable(x)
                for row in cur.fetchall():
                    table.add_row(list(row))
            db.commit()
            cur.close()
            db.close()
            try:
                await ctx.send(f"```\n{table}```" if table else resolve_emoji('ERROR',
                                                                              ctx) + " Nothing was returned in this query.")
            except discord.HTTPException:
                await ctx.send(f'Content too long. Hastepaste: ' + await self.bot.post_to_haste(table))
        except pymysql.err.ProgrammingError as e:
            err_msg = str(e).split(',')[1].replace(')', '').replace('"', '')
            await ctx.send(resolve_emoji('ERROR', ctx) + err_msg)

    @commands.command()
    @commands.check(is_owner)
    async def reload(self, ctx, *, extension: str):
        """Reload an extension (Bot Owner Only)"""
        if extension != "all":
            try:
                self.bot.unload_extension('cogs.' + extension.replace('/', '.'))
                self.bot.load_extension('cogs.' + extension.replace('/', '.'))
                await ctx.send(resolve_emoji('SUCCESS', ctx) + f" Reloaded /cogs/{extension}.py")
            except Exception:
                await ctx.send(resolve_emoji('ERROR', ctx)
                               + f" I-I'm sorry, I couldn't reload the `{extension}` extensions >w< "
                               + f"```py\n{traceback.format_exc()}```")
        else:
            extensions = [f for f in os.listdir('./cogs') if f.endswith('.py')] + ['events.' + f for f in
                                                                                   os.listdir('./cogs/events') if
                                                                                   f.endswith('.py')]
            for ext in extensions:
                try:
                    self.bot.unload_extension('cogs.' + ext[:-3])
                    self.bot.load_extension('cogs.' + ext[:-3])
                except:
                    await ctx.send(resolve_emoji('ERROR', ctx)
                                   + f'I ran into an error reloading the {ext[:-3]} extension. ```py\n{traceback.format_exc()}```')
                    continue
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Reloaded all extensions.')

    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, *, extension: str):
        """Unload an extension (Bot Owner Only)"""
        self.bot.unload_extension("cogs." + extension.replace('/', '.'))
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f" Unloaded /cogs/{extension}.py")

    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, *, extension: str):
        """Load an extension (Bot Owner Only)"""
        try:
            self.bot.load_extension("cogs." + extension.replace('/', '.'))
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f" Loaded /cogs/{extension}.py")
        except Exception:
            await ctx.send(resolve_emoji('ERROR', ctx)
                           + f" I-I'm sorry, I couldn't load the `{extension}` module >w< "
                           + f"```py\n{traceback.format_exc()}```")

    @commands.command()
    @commands.check(is_owner)
    async def blacklist(self, ctx, id: int, *, reason: str = None):
        """Blacklist a user or a guild."""
        if not reason:
            reason = 'Not defined.'
        if str(id) in self.bot.blacklist.keys():
            await ctx.send(
                resolve_emoji('ERROR', ctx) + f' That ID is already blacklisted for `{self.bot.blacklist[str(id)]}`\n'
                                              f'Do you wish to remove this blacklist?')

            def check(m):
                return m.content.lower() == 'yes' and m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                return await ctx.send('Kept blacklist due to request timeout.')
            del self.bot.blacklist[str(id)]
            self.bot.query_db(f'DELETE FROM blacklist WHERE id={id};')
            em = discord.Embed(description=f'**ID:** {id}\n**Action:** Un-Blacklist\n**Reason:** {reason}',
                               color=0x00ff00)
            em.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
            em.timestamp = datetime.datetime.utcnow()
            await self.bot.get_channel(388274450870829057).send(embed=em)
            return await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Removed the blacklist for **{id}**.')
        self.bot.blacklist[str(id)] = reason
        self.bot.query_db(f'INSERT INTO blacklist VALUES(%s, %s)', (id, reason))
        em = discord.Embed(description=f'**ID:** {id}\n**Action:** Blacklist\n**Reason:** {reason}', color=0xff0000)
        em.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
        em.timestamp = datetime.datetime.utcnow()
        await self.bot.get_channel(388274450870829057).send(embed=em)
        if self.bot.get_guild(id):
            await self.bot.get_guild(id).leave()
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Blacklisted ID **{id}** for `{reason}`')


def setup(bot):
    bot.add_cog(Owner(bot))
