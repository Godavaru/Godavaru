import discord
import random
import time
from discord.ext import commands

class Fun():
    def __init__(self, bot):
        self.bot = bot

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
        console = discord.Object("316688736089800715")
        saythis = ctx.message.content[6:]
        saythis = saythis.replace("`", "")
        if saythis == "":
            await self.bot.say('Specify something for me to say!')
        elif '--s' in saythis:
            silentsay = ctx.message.content[6:]
            silentsay = silentsay.replace("--s", "")
            await self.bot.say(silentsay)
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(console, "My `say` command was used by `" + ctx.message.author.name + '#' + ctx.message.author.discriminator + "` in channel `" + ctx.message.channel.name + "` in server `" + ctx.message.server.name + "` with the parameters of: ```css\n" + saythis + "```")
        else:
            await self.bot.say(ctx.message.content[6:])
            await self.bot.send_message(console, "My `say` command was used by `" + ctx.message.author.name + '#' + ctx.message.author.discriminator + "` in channel `" + ctx.message.channel.name + "` in server `" + ctx.message.server.name + "` with the parameters of: ```css\n" + saythis + "```")

    @commands.command(pass_context = True)
    async def year(self, ctx):
        await self.bot.say ("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send " + ctx.message.author.mention + " nudes :3")

    @commands.command(pass_context = True)
    async def f(self, ctx):
        embed = discord.Embed(title='Press F to pay respects!',description='**' + ctx.message.author.display_name + '** has paid their respects successfully :eggplant:',color=ctx.message.author.color).set_footer(text='f')
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        
    @commands.command(pass_context = True, aliases=["mb", "8ball"])
    async def magicball(self, ctx):
        random.seed(time.time())
        var = int(random.random() * 20)

        if (ctx.message.content == self.bot.command_prefix +"mb" or ctx.message.content == self.bot.command_prefix+"magicball" or ctx.message.content == self.bot.command_prefix+"8ball"):
            await self.bot.say("I can't be a magician unless you ask me a question! <:thonk:316105720548556801>")
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
    async def love(self, ctx):
        random.seed(time.time())
        var = int(random.random() * 101)

        msg1 = ctx.message.content
        msg1 = msg1.replace(self.bot.command_prefix+"love", "")
        if (var < 10):
            msg = "Try again next time."
        elif (var < 30 and var > 9):
            msg = "You could do better."
        elif (var < 50 and var > 29):
            msg = "Are you sure about these two?"
        elif (var == 69):
            msg = "L-lewd!"
        elif (var < 70 and var != 69 and var > 49):
            msg = "Not bad!"
        elif (var < 90 and var > 69):
            msg = "Almost perfect!"
        elif (var < 100 and var > 89):
            msg = "So close to perfection, it hurts."
        elif (var == 100):
            msg = "Literal perfection!!"
    
        if msg1 == "":
            await self.bot.say(":x: You need to specify who you want to love!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**100%**\n`You are very important and should love yourself!`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            elif ctx.message.mentions[0].id == "311810096336470017" and ctx.message.author.id == "267207628965281792":
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**-9000%**\n`Pure hatred. They absolutely hate eachother.`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            elif ctx.message.mentions[0].id == "132584525296435200" and ctx.message.author.id == "155867458203287552":
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**9000%**\n`There is no love that is stronger!`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            elif ctx.message.mentions[0].id == "155867458203287552" and ctx.message.author.id == "132584525296435200":
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**9000%**\n`There is no love that is stronger!`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            else:
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**" + str(var) + "%**\n`" + str(msg) + "`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
        else:
            embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + msg1 + "`",color=ctx.message.author.color).add_field(name="Result",value="**" + str(var) + "%**\n`" + str(msg) + "`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context=True)
    async def flip(self, ctx, user : discord.Member=None):
        if user != None:
            msg = ""
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "Don't you dare try and flip me. Just for that, take this!\n"
            elif user.id == "267207628965281792":
                user = ctx.message.author
                msg = "Don't flip my master! Hyah!\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await self.bot.say("Who do you want me to flip? :thinking:")

    @commands.command(pass_context = True)
    async def lenny(self, ctx):
        await self.bot.say ("( ͡° ͜ʖ ͡°)")
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context = True)
    async def nonowa(self, ctx):
        await self.bot.say("のワの")
        await self.bot.delete_message(ctx.message)
			
def setup(bot):
    bot.add_cog(Fun(bot))
