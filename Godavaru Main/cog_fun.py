import discord
from discord.ext import commands

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def echo(self, ctx):
        if ctx.message.content[7:] == "":
            await self.bot.say (":mega: I can't echo something that isn't specified!")
        else:
            await self.bot.say(':mega:' + ctx.message.content[6:])

    @commands.command(pass_context = True)
    async def lewd(self, ctx):
        embed = discord.Embed(title='We must go lewder!', description=":eyes:").set_image(url="https://image.prntscr.com/image/4beb7e203f394913abfccc19154d994a.png")
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def lood(self, ctx):
        embed = discord.Embed(title='P-put it in me senpai...', description=':blush:').set_image(url="https://image.prntscr.com/image/8e9cad7c75d84e419a2c551c18c36427.png")
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def say(self, ctx):
        if ctx.message.content[6:] == "":
            await self.bot.say('Specify something for me to say!')
        else:
            await self.bot.say(ctx.message.content[6:])
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context = True)
    async def shru(self, ctx):
        member = ctx.message.author
   
        if member.id != "99965250052300800":
            await self.bot.say ("Who are you, Instance#2513? Messing up the spelling that bad smh >:(")
        else:
            await self.bot.say("Learn to spell, Paul. For real ;-;")

    @commands.command(pass_context = True)
    async def year(self, ctx):
        await self.bot.say ("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send " + ctx.message.author.mention + " nudes :3")

def setup(bot):
    bot.add_cog(Fun(bot))
