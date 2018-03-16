import datetime
import io
import textwrap
import traceback
import subprocess
from contextlib import redirect_stdout

import aiohttp
import discord
from discord.ext import commands

import config


def is_owner(ctx):
    return ctx.author.id in config.owners


class Owner:
    def __init__(self, bot):
        self.bot = bot
        self.last_result = None

    @commands.command(name="eval")
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


"""
                                        ===================================
                                        VERSION 1.0.0 LEFTOVERS STARTS HERE
                                        ===================================

import datetime
import textwrap
import traceback
from contextlib import redirect_stdout
import hastebin
import js2py
from discord.ext import commands

from cogs.utils.tools import *

ownerids = [
    267207628965281792,
    99965250052300800,
    170991374445969408,
    188663897279037440,
    132584525296435200
]

class Owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def owner(self, ctx):
        ""\"Execute owner commands.

        You shouldn't even be looking at this command, but it's an option for people who are genuinely curious about the behind the scenes portion for the bot.
        The subcommands are:```
        shutdown   - Shut down the bot.
        game       - Set the playing status.
        todo       - Add something to the todo list.
        nick       - Set the bot nickname in this guild.
        status     - Set the physical status of the bot.
        name       - Set the bot username.
        serverlist - Lists all the bot's servers.
        bigservers - Lists all servers with x members.```

        **Usage:** `g_owner <subcommand> [extended options]`

        **Permission:** Bot Owner""\"
        member = ctx.message.author
        console = self.bot.get_channel(316688736089800715)

        if member.id not in ownerids:
            await ctx.send(":x: Je ne vous connais pas!! L'accès est refusé!!")
        else:
            try:
                args = ctx.message.content
                args = args.split(' ')
                if args[1] == "shutdown":
                    await ctx.send("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
                    await console.send(':warning: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] `' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
                    raise SystemExit
                elif args[1] == "game":
                    gargs = ctx.message.content
                    gargs = gargs.replace(self.bot.command_prefix[0]+"owner game", "")
                    gargs = gargs.replace(self.bot.command_prefix[1]+"owner game", "")
                    server_count = 0
                    member_count = 0
                    for server in self.bot.servers:
                        server_count += 1
                        for member in server.members:
                            member_count += 1
                    if gargs == "":
                        await ctx.send(":x: You must specify a game or `reset`!")
                    elif gargs == " reset":
                        await self.bot.change_presence(game=discord.Game(name='g_help | with '+str(server_count)+' servers and '+str(member_count)+' users!'))
                        await ctx.send(":white_check_mark: Reset my playing status.")
                    else:
                        await self.bot.change_presence(game=discord.Game(name='g_help |' + str(gargs)))
                        await ctx.send(":white_check_mark: Set my playing status to `g_help |" + str(gargs) + "`!")
#                elif args[1] == "leaveserver": removing this for remake later
#                    await ctx.send(":white_check_mark: I have left this server. Bye! :wave:")
#                    await self.bot.leave_server(ctx.message.server)
#                    # It's just us now. Just be calm and it shall all be over soon...
                elif args[1] == "todo":
                    todoChannel = self.bot.get_channel(316638257104551946)
                    targs = ctx.message.content
                    targs = targs.replace(self.bot.command_prefix[0]+"owner todo", "")
                    targs = targs.replace(self.bot.command_prefix[1]+"owner todo", "")
                    if targs == "":
                        await ctx.send(':x: Couldn\'t add your message to the todo list. Reason: Cannot send an empty message.')
                    else:
                        await todoChannel.send("-"+str(targs))
                        await ctx.send(':white_check_mark: Successfully added your message to the to-do list!')
                        # Va, je ne te hais point. 
                elif args[1] == "nick":
                    nargs = ctx.message.content
                    nargs = nargs.replace(self.bot.command_prefix[0]+"owner nick", "")
                    nargs = nargs.replace(self.bot.command_prefix[1]+"owner nick", "")
                    if nargs == "":
                        await ctx.send(":x: You must specify either a nickname or `reset`!")
                    elif nargs == " reset":
                        await ctx.message.guild.me.edit(nick="")
                        await ctx.send(":white_check_mark: My nickname was reset!")
                    else:
                        await ctx.message.guild.me.edit(nick=str(nargs))
                        await ctx.send(":white_check_mark: My nickname was changed to `"+str(nargs)+"` successfully!")
                elif args[1] == "status":
                    sargs = ctx.message.content
                    sargs = sargs.replace(self.bot.command_prefix[0]+"owner status", "")
                    sargs = sargs.replace(self.bot.command_prefix[1]+"owner status", "")
                    if sargs == "":
                        await ctx.send(":x: You must specify a status to set to!")
                    elif sargs == " online":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.online)
                        await ctx.send("Done! Set my status to `online`!")
                    elif sargs == " idle":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.idle)
                        await ctx.send("Done! Set my status to `idle`!")
                    elif sargs == " dnd":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.dnd)
                        await ctx.send("Done! Set my status to `dnd`!")
                    elif sargs == " invisible":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.invisible)
                        await ctx.send("Done! Set my status to `invisible`!")
                    else:
                        await ctx.send(":x: Not a valid status. Valid statuses are: `online`, `idle`, `dnd`, `invisible`")
                        # Les chefs-d'oeuvre ne sont jamais que des tentatives heureuses
                elif args[1] == "name":
                    unargs = ctx.message.content
                    unargs = sargs.replace(self.bot.command_prefix[0]+"owner name", "")
                    unargs = sargs.replace(self.bot.command_prefix[1]+"owner name", "")
                    if unargs == "":
                        await ctx.send(x+"You must specify a name")
                    else:
                        await self.bot.user.edit(username=str(unargs))
                        await ctx.send("Done! Changed my name successfully to `"+str(unargs)+"`")
                        await ctx.send("`"+str(ctx.message.author)+"` changed my username to `"+str(unargs)+"`")

                elif args[1] == "serverlist":
                    guilds = ""
                    for guild in sorted(self.bot.guilds, key=lambda x: x.name.lower()):
                        guilds += "{} ({}) owned by {} ({}) with {} members.\n".format(guild.name, guild.id, str(guild.owner), guild.owner.id, len(guild.members))
                    guilds = guilds.encode('utf-8')
                    await ctx.send("I did it, mom! "+hastebin.post(guilds))
                elif args[1] == "bigservers":
                    m = ""
                    try:
                        n = int(args[2])
                    except (ValueError, IndexError):
                        n = 1000
                    for server in sorted(self.bot.guilds, key=lambda x: x.name):
                        if len(server.members) > n:
                            m += server.name+" - "+str(server.owner)+" - "+str(len(server.members))+"\n"
                    await ctx.send("Servers with over {0} members.```\n{1}```".format(n, m))
                else:
                    await ctx.send(":x: Not a valid owner subcommand.")
            except IndexError:    
                embed = discord.Embed(title="Owner Commands",description="```css\n  ===== [OwnerCmds] =====\nThe following are subcommands, meaning they are used with g_owner <subcommand> <args>\n  ===== ===== ===== =====\n.game        | Set my playing status.\n.nick        | Set my nickname on the current server.\n.name        | Set my username.\n.eval        | Evaluate Python code.\n.status      | Set my status.\n.shutdown    | Shutdown the bot.\n.leaveserver | Leave the current server.\n  ===== ===== ===== ===== \nThese are commands that sit on their own and are not owner subcommands.\n  ===== ===== ===== =====\n.load        | Load a cog.\n.reload      | Reload a cog.\n.unload      | Unload a cog.```", color=ctx.message.author.color).set_footer(text="Commands created in Discord.py")
                await ctx.send(content=None, embed=embed)

    @commands.command(hidden=True)
    async def eval(self, ctx):
        args = ctx.message.content
        args = args.split(' ')
        if ctx.message.author.id not in ownerids:
            await ctx.send(":x: You do not have permission to evaluate code.")
            return
        try:
            if args[1] != "":
                if args[1] == "py":
                    code = ctx.message.content.replace(args[0]+" "+args[1]+" ", "")
                    code = code.strip('` ')
                elif args[1] == "js":
                    code = ctx.message.content.replace(args[0]+" "+args[1]+" ", "")
                    javascript = 'Excecuted successfully and returned: {}'
                    try:
                        result = js2py.eval_js(str(code))
                        if result is None:
                            a = "Executed successfully with no objects returned."
                        else:
                            a = javascript.format(result)
                        await ctx.send(embed=discord.Embed(
                            description=a,
                            color=0x00ff00
                        ).set_author(
                            name="Evaluated with success",
                            icon_url=ctx.message.author.avatar_url.replace("?size=1024", "")
                        ).set_footer(
                            text="Executed by: "+str(ctx.message.author)
                        ).set_thumbnail(
                            url='http://www.iconsdb.com/icons/preview/green/checked-checkbox-xxl.png'
                        ).add_field(
                            name="Code",
                            value="[See here.]({})".format(hastebin.post(code))))
                        return
                    except Exception as e:
                        await ctx.send(embed=discord.Embed(description="Excecuted and errored: {}".format(type(e).__name__ + ': ' + str(e)),color=0xff0000).set_author(name="Evaluated and errored", icon_url=ctx.message.author.avatar_url.replace("?size=1024", "")).set_footer(text="Executed by: "+str(ctx.message.author)).set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Red_x.svg/480px-Red_x.svg.png').add_field(name="Code",value="[See here.]({}.js)".format(hastebin.post(code))))
                        return
                else:
                    code = ctx.message.content.replace(args[0]+" ", "")
                    code = code.strip('` ')
                env = {
                    'self': self,
                    'bot': self.bot,
                    'ctx': ctx,
                    'message': ctx.message,
                    'guild': ctx.guild,
                    'channel': ctx.channel,
                    'author': ctx.author,
                    'me': ctx.me
                }
                env.update(globals())
    
                stdout = io.StringIO()

                toCompile = f'async def func():\n{textwrap.indent(code, "  ")}'

                try:
                    exec(toCompile, env)
                except Exception as e:
                    em=discord.Embed(description=f"Excecuted and errored: {e.__class__.__name__}: {e}",color=0xff0000)
                    em.set_author(
                        name="Evaluated and errored",
                        icon_url=ctx.message.author.avatar_url.replace("?size=1024", ""))
                    em.set_footer(text="Executed by: "+str(ctx.message.author))
                    em.set_thumbnail(
                        url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Red_x.svg/480px-Red_x.svg.png')
                    return await ctx.send(embed=em)

                func = env['func']
                try:
                    with redirect_stdout(stdout):
                        ret = await func()
                except Exception as e:
                    value = stdout.getvalue()
                    em = discord.Embed(
                        description=f"Excecuted and errored: ```py\n{value}{traceback.format_exc()}```",
                        color=0xff0000)
                    em.set_author(
                        name="Evaluated and errored",
                        icon_url=ctx.message.author.avatar_url.replace("?size=1024", ""))
                    em.set_footer(text="Executed by: "+str(ctx.message.author))
                    em.set_thumbnail(
                        url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Red_x.svg/480px-Red_x.svg.png')
                    await ctx.send(embed=em)
                else:
                    value = stdout.getvalue()
                    if ret is None or type(ret) is discord.Message:
                        if value:
                            x = f"{value}"
                        else:
                            x = "Executed successfully with no objects returned."
                    else:
                        x = f"Executed successfully and returned: {value}{ret}"
                    em = discord.Embed(description=x,
                                       color=0x00ff00)
                    em.set_author(
                        name="Evaluated with success",
                        icon_url=ctx.message.author.avatar_url.replace("?size=1024", ""))
                    em.set_footer(text="Executed by: "+str(ctx.message.author))
                    em.set_thumbnail(url='http://www.iconsdb.com/icons/preview/green/checked-checkbox-xxl.png')
                    await ctx.send(embed=em)                
        except IndexError:
            await ctx.send(":x: Specify code to evaluate")


def setup(bot):
    bot.add_cog(Owner(bot))
"""
