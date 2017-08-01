import discord
from discord.ext import commands

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
            await self.bot.send_message(console, '`' +  str(ctx.message.author) + '` tried to use an owner command!')
        else:
            args = ctx.message.content
            args = args.replace(self.bot.command_prefix+"owner", "")
            if args == "":
                embed = discord.Embed(title="Owner Commands",description="These commands are subcommands of the owner command. Use them with `"+self.bot.command_prefix+"owner <command> <args>`\nshutdown - Shutdown the bot.\ngame - Set the bot's playing status.\nleaveserver - Leave the server in which this command was executed.\ntodo - Add a message to the todo list.", color=ctx.message.author.color).add_field(name="Other Commands",value="These commands are alone, meaning they are not owner subcommands.\nreload - Reload a cog.\nload - Load a cog.\nunload - Unload a cog.").set_footer(text="Commands created in Discord.py")
                await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
            elif args == " shutdown":
                await self.bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
                await self.bot.send_message(console, '`' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
                raise SystemExit
            elif args.startswith(" game"):
                gargs = ctx.message.content
                gargs = gargs.replace(self.bot.command_prefix+"owner game", "")
                server_count = 0
                member_count = 0
                for server in self.bot.servers:
                    server_count += 1
                    for member in server.members:
                        member_count += 1
                if gargs == "":
                    await self.bot.say(":x: You must specify a game or `reset`!")
                elif gargs == " reset":
                    await self.bot.change_presence(game=discord.Game(name='g!help | with '+str(server_count)+' servers and '+str(member_count)+' users!'))
                    await self.bot.say(":white_check_mark: Reset my playing status.")
                    await self.bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` reset my playing status.')
                else:
                    await self.bot.change_presence(game=discord.Game(name='g!help |' + str(gargs)))
                    await self.bot.say(":white_check_mark: Set my playing status to `g!help |" + str(gargs) + "`!")
                    await self.bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` changed my playing status to `g!help |' + str(gargs) + '`.')
            elif args == " leaveserver":
                await self.bot.say(":white_check_mark: I have left this server. Bye! :wave:")
                await self.bot.leave_server(ctx.message.server)
                # It's just us now. Just be calm and it shall all be over soon...
            elif args.startswith(" todo"):
                todoChannel = discord.Object('316638257104551946')
                targs = ctx.message.content
                targs = targs.replace(self.bot.command_prefix+"owner todo", "")
                if targs == "":
                    await self.bot.say(':x: Couldn\'t add your message to the todo list. Reason: Cannot send an empty message.')
                else:
                    await self.bot.send_message(todoChannel, "-"+str(targs))
                    await self.bot.say(':white_check_mark: Successfully added your message to the to-do list!')
                    # Va, je ne te hais point. 
            elif args.startswith(" nick"):
                nargs = ctx.message.content
                nargs = nargs.replace(self.bot.command_prefix+"owner nick", "")
                if nargs == "":
                    await self.bot.say(":x: You must specify either a nickname or `reset`!")
                elif nargs == " reset":
                    await self.bot.change_nickname(ctx.message.server.me, "")
                    await self.bot.say(":white_check_mark: My nickname was reset!")
                else:
                    await self.bot.change_nickname(ctx.message.server.me, str(nargs))
                    await self.bot.say(":white_check_mark: My nickname was changed to `"+str(nargs)+"` successfully!")
            else:
                await self.bot.say(":x: Not a valid owner subcommand.")
        
def setup(bot):
    bot.add_cog(Owner(bot))
