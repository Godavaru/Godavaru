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
            await self.bot.say("No need to be looking at owner commands :eyes: (access denied)")
        else:
            await self.bot.say("**Owner commands!**\n\n`--shutdown` - Shutdown the bot.\n`--game` - Set the bot's playing status\n`--serverlist` - List all servers the bot is in.\n`--reload` - Reload a cog.\n`--unload` - Unload a cog.")
    
    @commands.command(pass_context = True)
    async def shutdown(self, ctx):
        member = ctx.message.author
        console = discord.Object('316688736089800715')
        
        if member.id not in ownerids:
            await self.bot.say("Y-you want me gone? That's just rude! (access denied)")
            await self.bot.send_message(console, '`' +  str(ctx.message.author) + '` tried to shut me down! :frowning:')
        else:
            await self.bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
            await self.bot.send_message(console, '`' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
            raise SystemExit

    @commands.command(pass_context = True)
    async def game(self, ctx, *, setGame: str):
        member = ctx.message.author

        if member.id not in ownerids:
            await self.bot.say("No changey my gamey :rage: (access denied)")
        else:
            await self.bot.change_presence(game=discord.Game(name='--help | ' + setGame))
            await self.bot.say("Set my playing status to `--help | " + setGame + "`!")
            console = discord.Object('316688736089800715')
            await self.bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` changed my playing status to `--help | ' + setGame + '`.')

    @commands.command(pass_context = True)
    async def serverlist(self, ctx):
        msg = '**Godavaru Server List**'
        channel = ctx.message.channel
        member = ctx.message.author
        for server in self.bot.servers:
            msg = msg + '\n`' + server.name + '` owned by `' + server.owner.name + '#' + server.owner.discriminator + '`'
        
        if member.id not in ownerids:
            await self.bot.say("My mommy says giving strangers information is bad! (access denied)")
        else:
            await self.bot.send_message(channel, msg)

def setup(bot):
    bot.add_cog(Owner(bot))
