import discord
from discord.ext import commands
import inspect
import datetime, re
import json
import asyncio
import random
import time
import platform
import datetime

ownerids = [
    '267207628965281792',
    '99965250052300800',
    '170991374445969408',
    '188663897279037440'
]

class Owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def owner(self, ctx):
        member = ctx.message.author
        console = discord.Object('316688736089800715')

        if member.id not in ownerids:
            await self.bot.say(":x: You do not have permission to execute this command.")
        else:
            try:
                args = ctx.message.content
                args = args.split(' ')
                if args[1] == "shutdown":
                    await self.bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
                    await self.bot.send_message(console, ':warning: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] `' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
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
                        await self.bot.say(":x: You must specify a game or `reset`!")
                    elif gargs == " reset":
                        await self.bot.change_presence(game=discord.Game(name='g_help | with '+str(server_count)+' servers and '+str(member_count)+' users!'))
                        await self.bot.say(":white_check_mark: Reset my playing status.")
                    else:
                        await self.bot.change_presence(game=discord.Game(name='g_help |' + str(gargs)))
                        await self.bot.say(":white_check_mark: Set my playing status to `g_help |" + str(gargs) + "`!")
                elif args[1] == "leaveserver":
                    await self.bot.say(":white_check_mark: I have left this server. Bye! :wave:")
                    await self.bot.leave_server(ctx.message.server)
                    # It's just us now. Just be calm and it shall all be over soon...
                elif args[1] == "todo":
                    todoChannel = discord.Object('316638257104551946')
                    targs = ctx.message.content
                    targs = targs.replace(self.bot.command_prefix[0]+"owner todo", "")
                    targs = targs.replace(self.bot.command_prefix[1]+"owner todo", "")
                    if targs == "":
                        await self.bot.say(':x: Couldn\'t add your message to the todo list. Reason: Cannot send an empty message.')
                    else:
                        await self.bot.send_message(todoChannel, "-"+str(targs))
                        await self.bot.say(':white_check_mark: Successfully added your message to the to-do list!')
                        # Va, je ne te hais point. 
                elif args[1] == "nick":
                    nargs = ctx.message.content
                    nargs = nargs.replace(self.bot.command_prefix[0]+"owner nick", "")
                    nargs = nargs.replace(self.bot.command_prefix[1]+"owner nick", "")
                    if nargs == "":
                        await self.bot.say(":x: You must specify either a nickname or `reset`!")
                    elif nargs == " reset":
                        await self.bot.change_nickname(ctx.message.server.me, "")
                        await self.bot.say(":white_check_mark: My nickname was reset!")
                    else:
                        await self.bot.change_nickname(ctx.message.server.me, str(nargs))
                        await self.bot.say(":white_check_mark: My nickname was changed to `"+str(nargs)+"` successfully!")
                elif args[1] == "status":
                    sargs = ctx.message.content
                    sargs = sargs.replace(self.bot.command_prefix[0]+"owner status", "")
                    sargs = sargs.replace(self.bot.command_prefix[1]+"owner status", "")
                    if sargs == "":
                        await self.bot.say(":x: You must specify a status to set to!")
                    elif sargs == " online":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.online)
                        await self.bot.say("Done! Set my status to `online`!")
                    elif sargs == " idle":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.idle)
                        await self.bot.say("Done! Set my status to `idle`!")
                    elif sargs == " dnd":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.dnd)
                        await self.bot.say("Done! Set my status to `dnd`!")
                    elif sargs == " invisible":
                        await self.bot.change_presence(game=ctx.message.server.me.game, status=discord.Status.invisible)
                        await self.bot.say("Done! Set my status to `invisible`!")
                    else:
                        await self.bot.say(":x: Not a valid status. Valid statuses are: `online`, `idle`, `dnd`, `invisible`")
                        # Les chefs-d'oeuvre ne sont jamais que des tentatives heureuses
                elif args[1] == "name":
                    unargs = ctx.message.content
                    unargs = sargs.replace(self.bot.command_prefix[0]+"owner name", "")
                    unargs = sargs.replace(self.bot.command_prefix[1]+"owner name", "")
                    if unargs == "":
                        await self.bot.say(x+"You must specify a name")
                    else:
                        await self.bot.edit_profile(username=str(unargs))
                        await self.bot.say("Done! Changed my name successfully to `"+str(unargs)+"`")
                        await self.bot.send_message("`"+str(ctx.message.author)+"` changed my username to `"+str(unargs)+"`")
                elif args[1] == "eval":
                    try:
                        if args[2] != "":
                            code = ctx.message.content.replace(self.bot.command_prefix[0]+"owner eval ", "")
                            code = ctx.message.content.replace(self.bot.command_prefix[1]+"owner eval ", "")
                            code = code.strip('` ')
                            python = '```py\n{}\n```'
                            result = None

                            env = {
                                'bot': self.bot,
                                'ctx': ctx,
                                'message': ctx.message,
                                'server': ctx.message.server,
                                'channel': ctx.message.channel,
                                'author': ctx.message.author
                            }

                            env.update(globals())

                            try:
                                result = eval(code, env)
                                if inspect.isawaitable(result):
                                    result = await result
                            except Exception as e:
                                await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
                                return

                            if type(result) is discord.Message:
                                await self.bot.say(python.format("Successfully evaluated."))
                            else:
                                await self.bot.say(python.format(result))
                    except IndexError:
                        await self.bot.say(":x: Specify code to evaluate!")
                else:
                    await self.bot.say(":x: Not a valid owner subcommand.")
            except IndexError:    
                embed = discord.Embed(title="Owner Commands",description="```css\n  ===== [OwnerCmds] =====\nThe following are subcommands, meaning they are used with g_owner <subcommand> <args>\n  ===== ===== ===== =====\n.game        | Set my playing status.\n.nick        | Set my nickname on the current server.\n.name        | Set my username.\n.eval        | Evaluate Python code.\n.status      | Set my status.\n.shutdown    | Shutdown the bot.\n.leaveserver | Leave the current server.\n  ===== ===== ===== ===== \nThese are commands that sit on their own and are not owner subcommands.\n  ===== ===== ===== =====\n.load        | Load a cog.\n.reload      | Reload a cog.\n.unload      | Unload a cog.```", color=ctx.message.author.color).set_footer(text="Commands created in Discord.py")
                await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        
def setup(bot):
    bot.add_cog(Owner(bot))
