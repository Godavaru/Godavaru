import discord
from discord.ext import commands
import time

class Mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def kick(self):
        await self.bot.say("[**Godavaru**] Hi there! Looks like you've found a lil easter egg. This command is planned, be patient!")

def setup(bot):
    bot.add_cog(Mod(bot))
