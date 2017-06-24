import discord
import random
import time
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
        console = discord.Obkect("316688736089800715")
        if ctx.message.content[6:] == "":
            await self.bot.say('Specify something for me to say!')
        else:
            await self.bot.say(ctx.message.content[6:])
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(console, "My `say` command was used by `" + ctx.message.author.name + '#' + ctx.message.author.discriminator + "` in channel `" + ctx.message.channel.name + "` in server `" + ctx.message.server.name + "` with the parameters of: ```css\n" + saythis + "```")


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

    @commands.command(pass_context = True)
    async def f(self, ctx):
        embed = discord.Embed(title='Press F to pay respects!',description='**' + ctx.message.author.display_name + '** has paid their respects successfully :eggplant:',color=ctx.message.author.color).set_footer(text='f')
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        
    @commands.command(pass_context = True)
    async def magicball(self, ctx):
        random.seed(time.time())
        var = int(random.random() * 20)

        if (ctx.message.content[12:] == ""):
            await self.bot.say("I can't be a magician unless you ask me a question! <:thonking:294428719227994113>")
        elif (var == 0):
            await self.bot.say(":crystal_ball: It is certain.")
        elif (var == 1):
            await self.bot.say(":crystal_ball: It is decidedly so.")
        elif (var == 2):
            await self.bot.say(":crystal_ball: Without a doubt.")
        elif (var == 3):
            await self.bot.say(":crystal_ball: Yes, definitely.")
        elif (var == 4):
            await self.bot.say(":crystal_ball: You may rely on it.")
        elif (var == 5):
            await self.bot.say(":crystal_ball: As I see it, yes.")
        elif (var == 6):
            await self.bot.say(":crystal_ball: Most likely.")
        elif (var == 7):
            await self.bot.say(":crystal_ball: Outlook good.")
        elif (var == 8):
            await self.bot.say(":crystal_ball: Yes.")
        elif (var == 9):
            await self.bot.say(":crystal_ball: Signs point to yes.")
        elif (var == 10):
            await self.bot.say(":crystal_ball: Reply hazy, try again.")
        elif (var == 11):
            await self.bot.say(":crystal_ball: Ask again later.")
        elif (var == 12):
            await self.bot.say(":crystal_ball: Better not tell you now.")
        elif (var == 13):
            await self.bot.say(":crystal_ball: Cannot predict now.")
        elif (var == 14):
            await self.bot.say(":crystal_ball: Concentrate and ask again.")
        elif (var == 15):
            await self.bot.say(":crystal_ball: Don't count on it.")
        elif (var == 16):
            await self.bot.say(":crystal_ball: My reply is no.")
        elif (var == 17):
            await self.bot.say(":crystal_ball: My sources say no.")
        elif (var == 18):
            await self.bot.say(":crystal_ball: Outlook not so good.")
        elif (var == 19):
            await self.bot.say(":crystal_ball: Very doubtful")
        elif (var == 20):
            await self.bot.say(":crystal_ball: Congratulations, you found an easter egg. I hope you realise this doesn't answer your question...")

    @commands.command(pass_context = True)
    async def mb(self, ctx):
        random.seed(time.time())
        var = int(random.random() * 20)

        if (ctx.message.content[5:] == ""):
            await self.bot.say("I can't be a magician unless you ask me a question! <:thonking:294428719227994113>")
        elif (var == 0):
            await self.bot.say(":crystal_ball: It is certain.")
        elif (var == 1):
            await self.bot.say(":crystal_ball: It is decidedly so.")
        elif (var == 2):
            await self.bot.say(":crystal_ball: Without a doubt.")
        elif (var == 3):
            await self.bot.say(":crystal_ball: Yes, definitely.")
        elif (var == 4):
            await self.bot.say(":crystal_ball: You may rely on it.")
        elif (var == 5):
            await self.bot.say(":crystal_ball: As I see it, yes.")
        elif (var == 6):
            await self.bot.say(":crystal_ball: Most likely.")
        elif (var == 7):
            await self.bot.say(":crystal_ball: Outlook good.")
        elif (var == 8):
            await self.bot.say(":crystal_ball: Yes.")
        elif (var == 9):
            await self.bot.say(":crystal_ball: Signs point to yes.")
        elif (var == 10):
            await self.bot.say(":crystal_ball: Reply hazy, try again.")
        elif (var == 11):
            await self.bot.say(":crystal_ball: Ask again later.")
        elif (var == 12):
            await self.bot.say(":crystal_ball: Better not tell you now.")
        elif (var == 13):
            await self.bot.say(":crystal_ball: Cannot predict now.")
        elif (var == 14):
            await self.bot.say(":crystal_ball: Concentrate and ask again.")
        elif (var == 15):
            await self.bot.say(":crystal_ball: Don't count on it.")
        elif (var == 16):
            await self.bot.say(":crystal_ball: My reply is no.")
        elif (var == 17):
            await self.bot.say(":crystal_ball: My sources say no.")
        elif (var == 18):
            await self.bot.say(":crystal_ball: Outlook not so good.")
        elif (var == 19):
            await self.bot.say(":crystal_ball: Very doubtful")
        elif (var == 20):
            await self.bot.say(":crystal_ball: Congratulations, you found an easter egg. I hope you realise this doesn't answer your question...")
			
def setup(bot):
    bot.add_cog(Fun(bot))
