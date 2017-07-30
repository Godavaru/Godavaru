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

        if member.id not in ownerids:
            await self.bot.say(":x: You do not have permission to execute this command.")
        else:
            embed = discord.Embed(title="Owner Commands",description=self.bot.command_prefix + "shutdown - Shutdown the bot.\n" + self.bot.command_prefix + "game - Set the bot's playing status.\n" + self.bot.command_prefix + "reload - Reload a cog\n" + self.bot.command_prefix + "unload - Unload a cog.\n" + self.bot.command_prefix + "leaveserver - Leave the server in which this command was executed.\n" + self.bot.command_prefix + "todo - Add a message to the todo list.", color=ctx.message.author.color).set_footer(text="Commands created in Discord.py")
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
            
    @commands.command(pass_context = True)
    async def shutdown(self, ctx):
        member = ctx.message.author
        console = discord.Object('316688736089800715')
        
        if member.id not in ownerids:
            await self.bot.say(":x: You do not have permission to execute this command.")
            await self.bot.send_message(console, '`' +  str(ctx.message.author) + '` tried to shut me down! :frowning:')
        else:
            await self.bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
            await self.bot.send_message(console, '`' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
            raise SystemExit

    @commands.command(pass_context = True)
    async def game(self, ctx, *, setGame: str):
        member = ctx.message.author
        console = discord.Object('316688736089800715')
        
        if member.id not in ownerids:
            await self.bot.say(":x: You do not have permission to execute this command.")
        else:
            server_count = 0
            member_count = 0
            for server in self.bot.servers:
                server_count += 1
                for member in server.members:
                    member_count += 1
            if ctx.message.content[7:] == "":
                await self.bot.say(":x: You must specify a game or `reset`!")
            elif ctx.message.content[7:] == "reset":
                await self.bot.change_presence(game=discord.Game(name='g!help | with '+str(server_count)+' servers and '+str(member_count)+' users!'))
                await self.bot.say(":white_check_mark: Reset my playing status.")
                await self.bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` reset my playing status.')
            else:
                await self.bot.change_presence(game=discord.Game(name='g!help | ' + setGame))
                await self.bot.say(":white_check_mark: Set my playing status to `g!help | " + setGame + "`!")
                await self.bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` changed my playing status to `g!help | ' + setGame + '`.')

    @commands.command(pass_context = True)
    async def leaveserver(self, ctx):
        member = ctx.message.author

        if member.id not in ownerids:
            await self.bot.say(":x: You do not have permission to execute this command.")
        else:
            await self.bot.say(":white_check_mark: I have left this server. Bye! :wave:")
            await self.bot.leave_server(ctx.message.server)

    @commands.command(pass_context = True)
    async def todo(self, ctx):
        testing = discord.Object('316638257104551946')
        msg = ctx.message.content[7:]
        member = ctx.message.author
        if member.id not in ownerids:
            await self.bot.say(':x: You do not have permission to execute this command.')
        else:
            await self.bot.send_message(testing, content=msg)
            await self.bot.say(':white_check_mark: Successfully added your message to the to-do list!')

    @commands.command(pass_context = True)
    async def nick(self, ctx):
        member = ctx.message.author
        if member.id not in ownerids:
            await self.bot.say(':x: You do not have permission to execute this command.')
        elif ctx.message.content[7:] == "":
            await self.bot.change_nickname(ctx.message.server.me, str(ctx.message.content[7:]))
            await self.bot.say(":white_check_mark: My nickname was reset!")
        else:
            await self.bot.change_nickname(ctx.message.server.me, str(ctx.message.content[7:]))
            await self.bot.say(":white_check_mark: My nickname was changed to `" + ctx.message.content[7:] + "` successfully!")
        
def setup(bot):
    bot.add_cog(Owner(bot))
