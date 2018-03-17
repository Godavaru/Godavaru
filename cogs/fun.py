import asyncio
import os
import random
import string
import discord
import re
import requests
import aiohttp
from discord.ext import commands

import config
from cogs.utils import image
from cogs.utils.tools import *


class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, args: str):
        """Make me say something.
        You can also use me to edit a message and you can use the silentsay variable as well.
        **FLAGS**:
            If you use `--s` as a flag, your arguments are simply what you want the bot to say and have it remove your message afterwards.
            If you use `--e` as a flag, the arguments are the message id you want to edit and the new content.
            If no flag is passed, the bot will simply send the message like normal excluding the actual command."""
        args = args.replace("@everyone", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        args = args.replace("@here", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        if args.startswith("--s"):
            if args == "--s":  # --s == silentsay
                await ctx.send("You can't silently send an empty message!")
            else:
                args = args[4:]
                await ctx.send(str(args))
                try:
                    await ctx.message.delete()
                except:
                    pass
        elif args.startswith("--e"):
            if args == "--e":  # --e == edit
                return await ctx.send("You can't edit nothingness.")
            try:
                args = args[4:]
                mid = args.split(' ')
                to_edit = await ctx.message.channel.get_message(int(mid[0]))
                content = args.replace(mid[0] + " ", "")
                try:
                    await to_edit.edit(content=content)
                except discord.Forbidden:
                    await ctx.send("Can't edit that message.")
                await ctx.message.delete()
            except discord.NotFound:
                not_found = await ctx.send("Couldn't find the message.")
                await asyncio.sleep(5)
                await not_found.delete()
                await ctx.message.delete()
            except (IndexError, ValueError):
                indx_err = await ctx.send("Usage: `g_say --e <id> <content>`")
                await asyncio.sleep(5)
                await indx_err.delete()
                await ctx.message.delete()
            except discord.Forbidden:
                err = await ctx.send("I don't have permission to delete your message.")
                await asyncio.sleep(5)
                await err.delete()
        else:
            await ctx.send(str(args))

    @commands.command(aliases=["memes"])
    @commands.bot_has_permissions(embed_links=True)
    async def meme(self, ctx):
        """This command gives you a random discord meme, powered by weeb.sh"""
        em = discord.Embed(title="Here's a random discord meme for ya", color=ctx.author.color)
        em.set_image(url=(await self.bot.weeb.get_image("discord_memes"))[0])
        em.set_footer(text="Powered by weeb.sh")
        await ctx.send(embed=em)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def delet(self, ctx):
        """This command gives you a random delet this meme, powered by weeb.sh"""
        em = discord.Embed(title="Delet this!!1!", color=ctx.author.color)
        em.set_image(url=(await self.bot.weeb.get_image("delet_this"))[0])
        em.set_footer(text="Powered by weeb.sh")
        await ctx.send(embed=em)

    @commands.command(aliases=["awooo"])
    @commands.bot_has_permissions(embed_links=True)
    async def awoo(self, ctx, face_colour: str = None, hair_colour: str = None):
        """Generate an awoo image with customizable face & hair colours.
        The colours must be hex codes."""
        face_colour = face_colour.replace('#', '') if face_colour else ''
        hair_colour = hair_colour.replace('#', '') if hair_colour else ''
        face = 'fff0d3'
        if re.compile(r'^[0-9a-fA-F]{6}$').match(face_colour):
            face = face_colour
        hair = 'cc817c'
        if re.compile(r'^[0-9a-fA-F]{6}$').match(hair_colour):
            hair = hair_colour
        with open("./images/awoo.png", "wb") as img:
            img.write(await self.bot.weeb.generate_image(imgtype="awooo", face=face, hair=hair))
            img.close()
        await ctx.send(file=discord.File('./images/awoo.png'))
        os.remove('./images/awoo.png')

    @commands.command()
    async def eyes(self, ctx):
        """Generate some random facing eyes!"""
        with open("./images/eyes.png", "wb") as img:
            img.write(await self.bot.weeb.generate_image(imgtype="eyes"))
            img.close()
        await ctx.send(file=discord.File('./images/eyes.png'))
        os.remove('./images/eyes.png')

    @commands.command()
    async def won(self, ctx):
        """Generate a won image with randomly facing eyes."""
        with open("./images/won.png", "wb") as img:
            img.write(await self.bot.weeb.generate_image(imgtype='won'))
            img.close()
        await ctx.send(file=discord.File('./images/won.png'))
        os.remove('./images/won.png')

    @commands.command(aliases=['insult', 'waifu', 'shitwaifu', 'garbage'])
    async def waifuinsult(self, ctx, *, member: discord.Member = None):
        """Generate a waifu insult of someone."""
        if member is None:
            member = ctx.author
        with open("./images/waifuinsult.png", "wb") as img:
            img.write(await self.bot.weeb.generate_waifu_insult(avatar=member.avatar_url))
            img.close()
        await ctx.send(file=discord.File('./images/waifuinsult.png'))
        os.remove('./images/waifuinsult.png')

    @commands.command(aliases=["weeb"])
    @commands.bot_has_permissions(embed_links=True)
    async def image(self, ctx, type: str = None):
        """Get an image with the specified type, powered by weeb.sh"""
        if type not in self.bot.weeb_types or type.lower() is None:
            return await ctx.send(f"Valid types: ```\n{', '.join(self.bot.weeb_types)}\n``` Use these like `{ctx.prefix}{ctx.command} <type>`")
        em = discord.Embed(color=ctx.author.color)
        em.set_image(url=(await self.bot.weeb.get_image(type.lower()))[0])
        em.set_footer(text="Powered by weeb.sh")
        await ctx.send(embed=em)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def year(self, ctx, *, member: discord.Member = None):
        # *sheds a tear* my little baby is still alive :)
        # yes i am crazy
        # no do not ask
        """The very first command that was ever added.
        It's nothing special, but it's a nice lil joke :eyes:"""
        if member is None:
            member = ctx.author
        await ctx.send(
            "A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send **" + str(
                member) + "** nudes :3")

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def f(self, ctx):
        """Pay your respects."""
        embed = discord.Embed(title='Press F to pay respects!',
                              description='**' + ctx.message.author.display_name + '** has paid their respects successfully :eggplant:',
                              color=ctx.message.author.color).set_footer(text='f')
        await ctx.send(content=None, embed=embed)

    # If you're looking for the code for 8ball, it was moved to cog_utils
    # hey Desii from the past... do you really think anyone reads this?
    # If they do, send a message in #general of my bot hub saying: "card games on motorcycles"
    # ... yes i'm bored
    # why did i make this comment block
    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # memes
    # imma just add a single line of comments everytime i see this owo
    # im a meme
    # Lars is cute
    # hello there human being
    # oh my gOD I MADE AN API WRAPPER
    # no im not crazy dont look at me like that
    # awau
    # hi

    @commands.command()
    async def slots(self, ctx):
        """Roll the slot machine and try your luck."""
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
        await ctx.send(
            "{0}\n\n{1}{2}{3}\n{4}{5}{6} :arrow_left:\n{7}{8}{9}".format(msg, col[var1], col[var2], col[var3],
                                                                         col[var4], col[var5], col[var6], col[var7],
                                                                         col[var8], col[var9]))

    @commands.command()
    async def bowling(self, ctx):
        """Play a game of bowling!"""
        init = int(random.random() * 10) + 1
        if init == 10:
            await ctx.send(":bowling: It's a strike! You hit all the pins on your first try.")
            return
        else:
            await ctx.send(
                ":bowling: You knocked down `{}` pins. Let's try to knock the other `{}` down.".format(init, 10 - init))
            await asyncio.sleep(2)
            finisher = int(random.random() * (10 - init)) + 1
            if finisher + init >= 10:
                await ctx.send(":bowling: You won! You knocked down all pins on the second try.")
            else:
                await ctx.send(
                    ":bowling: You didn't win, but you tried and knocked down `{}/10` in the meantime.".format(
                        finisher + init))

    @commands.command(aliases=["number"])
    async def numbers(self, ctx, num=None):
        """Get a random fact about a number or specify a number to get a fact about it.
        If your number is invalid, a random number will be used."""
        if num:
            try:
                num = int(num)
            except:
                num = int(random.random() * 2000) + 1
        else:
            num = int(random.random() * 2000) + 1
        if num > 100:
            types = ["math", "year"]
        else:
            types = ["trivia", "math", "date", "year"]
        x = requests.get("http://numbersapi.com/{}/{}".format(num, types[int(random.random() * len(types))]))
        await ctx.send(":mega: {}".format(x.text))

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def love(self, ctx, *members: discord.Member):
        """Use some magic numbers to calculate the compatibility between two users.
        If only one user is given, you will be used as the second."""
        l = members
        if len(members) > 2:
            l = [members[0], members[1]]
        if len(members) == 1:
            l = [ctx.author, members[0]]
        if len(members) == 0:
            return await ctx.send(":x: You need to specify the two users or one to compare with yourself.")
        if (l[0].id == l[1].id) and l[0].id != ctx.author.id:
            sum = 101
            msg = f"Be sure to tell {l[0].display_name} that they should love themself!"
        elif (l[0].id == l[1].id) and l[0].id == ctx.author.id:
            sum = 9001
            msg = "You are a special creature and should love yourself <3"
        else:
            sum = (l[0].id + l[1].id) % 101
            if sum == 69:
                msg = "L-lewd!"
            elif sum == 0:
                msg = "Horrible match."
            elif 0 < sum < 21:
                msg = "Kinda bad."
            elif 20 < sum < 41:
                msg = "Could be much better."
            elif 40 < sum < 61:
                msg = "Not bad, not bad at all."
            elif 60 < sum < 81 and sum != 69:
                msg = "Pretty good if you ask me."
            elif 80 < sum < 91:
                msg = "Really, really good."
            elif 90 < sum < 100:
                msg = "As close to perfect as you can get!"
            else:
                msg = "Absolutely ideal and perfect!"
        names = [l[0].display_name, l[1].display_name]
        shipname = names[0][:int(len(names[0]) / 2)] + names[1][int(len(names[1]) / 2):]
        em = discord.Embed(
            title="Love Meter",
            description=f"\N{TWO HEARTS} **{l[0].display_name}**\n\N{TWO HEARTS} **{l[1].display_name}**",
            color=ctx.author.color)
        em.add_field(name="Result", value=f"**{sum}%**\n`{msg}`", inline=False)
        em.add_field(name="Shipname", value=shipname)
        em.set_thumbnail(url="https://www.emojibase.com/resources/img/emojis/hangouts/1f49c.png")
        await ctx.send(embed=em)

    @commands.command()
    async def flip(self, ctx, *, user: discord.Member):
        """Flip people! Because flipping them off is not enough."""
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
        await ctx.send(msg + "(╯°□°）╯︵ " + name[::-1])

    @commands.command()
    async def roll(self, ctx):
        """Roll a generic six-sided die."""
        await ctx.send(":game_die: You rolled a **{}**!".format(random.randint(1, 6)))

    @commands.command()
    async def person(self, ctx):
        """Generate a random person's information.
        Note: This information is 100% fake and provided by randomuser.me."""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://randomuser.me/api') as resp:
                js = await resp.json()
        person = js['results'][0]
        em = discord.Embed(colour=int("".join([random.choice('ABCDEF0123456789') for _ in range(6)]), 16)) \
            .set_author(
            name=f"{person['name']['title'].capitalize()} {person['name']['first'].capitalize()} {person['name']['last'].capitalize()}",
            icon_url=person['picture']['thumbnail']) \
            .set_thumbnail(url=person['picture']['large']) \
            .add_field(name="Gender", value=person['gender'].capitalize()) \
            .add_field(name="Date of Birth", value=person['dob']) \
            .add_field(name="Location", value=", ".join(
            [string.capwords(person['location']['street']), string.capwords(person['location']['city']),
             string.capwords(person['location']['state']), str(person['location']['postcode']), person['nat']])) \
            .add_field(name="Email", value=person['email'].replace('example.com', 'gmail.com')) \
            .add_field(name="Account", value="**Username:** {}\n**Password:** {}\n**Registered At:** {}".format(person['login']['username'], person['login']['password'], person['registered'])) \
            .add_field(name="Phone", value=f"**Home:** {person['phone']}\n**Cell:** {person['cell']}")
        await ctx.send(embed=em)

    @commands.command()
    async def rps(self, ctx, choice: str):
        """Play a game of rock paper scissors against the bot.
        The choice parameter should be either rock, paper, or scissors, case insensitive."""
        opts = ["rock", "paper", "scissors"]
        emotes = ["🗿", "📰", "✂"]
        bot_choice = random.choice(opts)
        user_choice = choice.lower()
        if user_choice not in opts:
            return await ctx.send(":x: That is not rock, paper, or scissors.")
        bot_index = opts.index(bot_choice)
        user_index = opts.index(user_choice)
        win = False
        if bot_index < user_index != 2:
            win = True
        elif user_index == 2 and bot_index == 1:
            win = True
        await ctx.send(f"{emotes[bot_index]} You {'won' if win is True else 'lost'}!")

    @commands.command()
    async def lenny(self, ctx, *, msg: str = ""):
        """Make a lenny face."""
        await ctx.send(msg + " ( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def nonowa(self, ctx, *, msg: str = ""):
        """Make a nonowa face."""
        await ctx.send(msg + " のワの")

    @commands.command(aliases=["nc"])
    async def nightcore(self, ctx):
        """Get a random nightcore song."""
        r = requests.get('https://api.apithis.net/nightcore.php')
        song = r.text
        await ctx.send(song)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def trivia(self, ctx, *, difficulty: str = None):
        """Play a game of trivia."""
        url = "https://opentdb.com/api.php?amount=1"
        if difficulty:
            url += "&difficulty=" + difficulty
        r = requests.get(url)
        j = r.json()
        correct = remove_html(j['results'][0]['correct_answer'])
        x = j['results'][0]['incorrect_answers']
        x.append(correct)
        y = []
        for val in x:
            val = remove_html(val)
            y.append(val)
        z = sorted(y, key=lambda l: l.lower())
        em = discord.Embed(description=remove_html(j['results'][0]['question']), color=ctx.author.color)
        em.add_field(name="Category", value=j['results'][0]['category'])
        em.add_field(name="Difficulty", value=j['results'][0]['difficulty'])
        em.add_field(name="Answers", value=("\n".join(z)), inline=False)
        await ctx.send(embed=em)

        def check1(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel

        try:
            msg = await self.bot.wait_for('message', check=check1, timeout=120.0)
        except asyncio.TimeoutError:
            await ctx.send("You didnt answer in time, the correct answer was `{}`".format(correct))
            return
        if msg.content.lower() == correct.lower():
            await ctx.send(":white_check_mark: **{}** got the correct answer!".format(
                ctx.author.display_name))
            return
        elif msg.content.lower() == "end":
            await ctx.send(f":ok_hand: Ended your game, the correct answer was `{correct}`")
            return
        else:
            if len(j['results'][0]['incorrect_answers']) > 2:
                await ctx.send(":x: That isn't right. You have one more try.")

                def check2(m):
                    return m.author.id == ctx.author.id and m.channel == ctx.channel

                try:
                    msg2 = await self.bot.wait_for('message', check=check2, timeout=120.0)
                except asyncio.TimeoutError:
                    await ctx.send("You didnt answer in time, the correct answer was `{}`".format(correct))
                    return
                if msg2.content.lower() == correct.lower():
                    await ctx.send(":white_check_mark: **{}** got the correct answer!".format(
                        ctx.author.display_name))
                    return
                elif msg2.content.lower() == "end":
                    await ctx.send(f":ok_hand: Ended your game, the correct answer was `{correct}`")
                    return
                else:
                    await ctx.send(":x: That's not right. The correct answer was `{}`".format(correct))
            else:
                await ctx.send(":x: That's not right. The correct answer was `{}`".format(correct))

    @commands.command()
    async def joke(self, ctx, *, phrase: str = None):
        """Make a somewhat Chuck Norris related joke."""
        if phrase is None:
            phrase = ctx.author.display_name
        r = requests.get('http://api.icndb.com/jokes/random')
        js = r.json()
        j = str(js['value']['joke'])
        j = j.replace("Chuck Norris", phrase)
        j = j.replace("Chuck", phrase)
        j = j.replace('&quot;', "\"")
        await ctx.send(j)

    @commands.command()
    async def ttb(self, ctx, *, text: str):
        """Use the text to brick feature."""
        bricks = "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"
        text = text.lower()
        for b in bricks:
            index = bricks.index(b)
            text = text.replace(string.ascii_lowercase[index], b)
        # Yes, replace spam here because I can't figure out another way.
        # If you have one pls tell me.
        # I'm too tired for this shit.
        msg1 = text.replace("#", ":hash:")
        msg2 = msg1.replace("1", ":one:")
        msg3 = msg2.replace("2", ":two:")
        msg4 = msg3.replace("3", ":three:")
        msg5 = msg4.replace("4", ":four:")
        msg6 = msg5.replace("5", ":five:")
        msg7 = msg6.replace("6", ":six:")
        msg8 = msg7.replace("7", ":seven:")
        msg9 = msg8.replace("8", ":eight:")
        msg10 = msg9.replace("9", ":nine:")
        msg11 = msg10.replace("0", ":zero:")
        msg12 = msg11.replace(" ", "   ")
        msg13 = msg12.replace("?", ":grey_question:")
        msg14 = msg13.replace("!", ":grey_exclamation:")
        await ctx.send(msg14)


def setup(bot):
    bot.add_cog(Fun(bot))

# Yes, oddly enough, there are no leftovers in this cog. It was one of the more less effort to convert.
