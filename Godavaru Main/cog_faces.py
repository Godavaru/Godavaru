import discord
from discord.ext import commands

class Faces():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def lenny(self, ctx):
        await self.bot.say ("( ͡° ͜ʖ ͡°)")
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context = True)
    async def nonowa(self, ctx):
        await self.bot.say("のワの")
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(Faces(bot))
