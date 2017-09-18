import discord
import random
import time
import asyncio
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
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix[0]+"say", "")
        args = args.replace(self.bot.command_prefix[1]+"say", "")
        args = args.replace("@everyone", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        args = args.replace("@here", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        args = args[1:]
        if args == "":
            await self.bot.say("I can't send an empty message!")
        elif args.startswith("--s"):
            if args == "--s": # --s == silentsay
                await self.bot.say("You can't silently send an empty message!")
            else:
                args = args[4:]
                await self.bot.say(str(args))
                await self.bot.delete_message(ctx.message)
        elif args.startswith("--e"):
            if args == "--e": # --e == edit
                await self.bot.say("You can't edit nothingness.")
            try:
                args = args[4:]
                mid = args.split(' ')
                toEdit = await self.bot.get_message(ctx.message.channel, str(mid[0])) 
                content = args.replace(mid[0]+" ", "")
                await self.bot.edit_message(toEdit, new_content=content)
                await self.bot.delete_message(ctx.message)
            except discord.NotFound:
                notFound = await self.bot.say("Couldn't find the message.")
                await asyncio.sleep(5)
                await self.bot.delete_message(notFound)
                await self.bot.delete_message(ctx.message)
            except IndexError:
                indxErr = await self.bot.say("Usage: `g_say --e <id> <content>`")
                await asyncio.sleep(5)
                await self.bot.delete_message(indxErr)
                await self.bot.delete_message(ctx.message)
        else:
            await self.bot.say(str(args))

    @commands.command(pass_context = True)
    async def year(self, ctx):
        if len(ctx.message.mentions) > 0:
            u = ctx.message.mentions[0]
        else:
            u = ctx.message.author
        await self.bot.say ("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send " + u.mention + " nudes :3")

    @commands.command(pass_context = True)
    async def f(self, ctx):
        embed = discord.Embed(title='Press F to pay respects!',description='**' + ctx.message.author.display_name + '** has paid their respects successfully :eggplant:',color=ctx.message.author.color).set_footer(text='f')
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

        
    # If you're looking for the code for 8ball, it was moved to cog_utils


    @commands.command(pass_context=True)
    async def slots(self, ctx):
        try:
            var1 = int(random.random() * 5)
            var2 = int(random.random() * 5)
            var3 = int(random.random() * 5)
            var4 = int(random.random() * 5)
            var5 = int(random.random() * 5)
            var6 = int(random.random() * 5)
            var7 = int(random.random() * 5)
            var8 = int(random.random() * 5)
            var9 = int(random.random() * 5)
            col = [":moneybag:", ":cherries:", ":carrot:", ":popcorn:", ":seven:"]
            if var6 == var5 and var5 == var4 and var4 == var6:
                msg = "**You won!**"
            else:
                msg = "**You lost!**"
            await self.bot.say("{0}\n\n{1}{2}{3}\n{4}{5}{6} :arrow_left:\n{7}{8}{9}".format(msg, col[var1], col[var2], col[var3], col[var4], col[var5], col[var6], col[var7], col[var8], col[var9]))
        except Exception as e:
            await self.bot.say(":x: `ERROR` ```py\n{}```".format(type(e).__name__ + ': ' + str(e)))

    @commands.command(pass_context = True)
    async def love(self, ctx):
        random.seed(time.time())
        var = int(random.random() * 101)

        msg1 = ctx.message.content
        msg1 = msg1.replace(self.bot.command_prefix[0]+"love", "")
        msg1 = msg1.replace(self.bot.command_prefix[1]+"love", "")
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
            content=":x: You need to specify who you want to love!"
            embed=None
        elif len(ctx.message.mentions) > 0:
            content=None
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
            content=None
            embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + msg1 + "`",color=ctx.message.author.color).add_field(name="Result",value="**" + str(var) + "%**\n`" + str(msg) + "`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
        await self.bot.send_message(ctx.message.channel, content=content, embed=embed)

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0]
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

    @commands.command(pass_context=True)
    async def roll(self, ctx):
        var = int(random.random() * 6)
        num = ["1", "2", "3", "4", "5", "6"]
        await self.bot.send_message(ctx.message.channel, ":game_die: You rolled a **{}**!".format(num[var]))

    @commands.command(pass_context=True)
    async def rps(self, ctx):
        umsg = ctx.message.content
        args = umsg.split(' ')
        args = umsg.replace(args[0], "")
        args = args[1:]
        var = int(random.random() * 3)
        if args == "paper" or args == "rock" or args == "scissors":
            if (var == 0):
                if args == "paper":
                    await self.bot.send_message(ctx.message.channel, ":moyai: You win!")
                elif args == "rock":
                    await self.bot.send_message(ctx.message.channel, ":moyai: It's a draw!")
                elif args == "scissors":
                    await self.bot.send_message(ctx.message.channel, ":moyai: You lose!")
            elif (var == 1):
                if args == "paper":
                    await self.bot.send_message(ctx.message.channel, ":newspaper: It's a draw!")
                elif args == "rock":
                    await self.bot.send_message(ctx.message.channel, ":newspaper: You lose!")
                elif args == "scissors":
                    await self.bot.send_message(ctx.message.channel, ":newspaper: You win!")
            elif (var == 2):
                if args == "paper":
                    await self.bot.send_message(ctx.message.channel, ":scissors: You lose!")
                elif args == "rock":
                    await self.bot.send_message(ctx.message.channel, ":scissors: You win!")
                elif args == "scissors":
                    await self.bot.send_message(ctx.message.channel, ":scissors: It's a draw!")
        else:
            await self.bot.say(":x: You must specify either rock, paper, or scissors!")

    @commands.command(pass_context = True)
    async def lenny(self, ctx):
        umsg = ctx.message.content
        args = umsg.split(' ')
        msg = umsg.replace(args[0], "")
        await self.bot.say (str(msg)+"( ͡° ͜ʖ ͡°)")
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context = True)
    async def nonowa(self, ctx):
        umsg = ctx.message.content
        args = umsg.split(' ')
        msg = umsg.replace(args[0], "")
        await self.bot.say(str(msg)+"のワの")
        await self.bot.delete_message(ctx.message)
			
def setup(bot):
    bot.add_cog(Fun(bot))
