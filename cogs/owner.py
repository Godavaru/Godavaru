import datetime
import io
import sys
import textwrap
import traceback
import subprocess
import pymysql
from prettytable import PrettyTable
from contextlib import redirect_stdout

import aiohttp
import discord
from discord.ext import commands
from .utils.tools import *

import config


def is_owner(ctx):
    return ctx.author.id in config.owners


class Owner:
    def __init__(self, bot):
        self.bot = bot
        self.last_result = None

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
                msg = await ctx.send("Unable to send returns due to the length. Uploading to hastebin...")
                async with aiohttp.ClientSession() as session:
                    async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
                        if resp.status == 200:
                            await msg.edit(content="*Executed in {}ms and returned:* https://hastebin.com/".format(
                                ((datetime.datetime.utcnow() - before) * 1000).total_seconds()) + (await resp.json())[
                                                       "key"])
                        else:
                            await msg.edit(content="Error uploading to hastebin :(")

    @commands.command(name="exec")
    @commands.check(is_owner)
    async def _exec(self, ctx, *, code: str):
        """Execute code in a command shell. (Bot Owner Only)"""
        sp = subprocess.Popen(code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
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
        sys.exit()

    @commands.command(aliases=['db', 'dbquery'])
    @commands.check(is_owner)
    async def query(self, ctx, *, query: str):
        """Query the MySQL database. (Bot Owner Only)"""
        try:
            db = pymysql.connect(config.db_ip, config.db_user, config.db_pass, config.db_name)
            cur = db.cursor()
            cur.execute(query)
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
            await ctx.send(f"```\n{table}```" if table != "" else ":x: Nothing was returned in this query.")
        except pymysql.err.ProgrammingError as e:
            err_msg = str(e).split(',')[1].replace(')', '').replace('"', '')
            await ctx.send(f":x: {err_msg}")

    @commands.command()
    @commands.check(is_owner)
    async def reload(self, ctx, *, extension: str):
        """Reload an extension (Bot Owner Only)"""
        try:
            self.bot.unload_extension('cogs.' + extension)
            self.bot.load_extension('cogs.' + extension)
            await ctx.send(f":ok_hand: Reloaded /cogs/{extension}.py")
        except Exception:
            await ctx.send(f":sob: I-I'm sorry, I couldn't reload the `{extension}` module >w< "
                           + f"```py\n{traceback.format_exc()}```")

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