import asyncio
import datetime
import json
import discord
import os
import cairosvg
import random
import requests
import urllib
import urllib.parse

import aiohttp
import pytz
from discord.ext import commands

from cogs.utils import image
from cogs.utils.tools import *


class Utils:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="time")
    async def _time(self, ctx, *, timezone: str):
        """Determine the current time in a timezone specified.
        The timezone is case sensitive as seen in [this list](https://pastebin.com/B5tLQdEY)."""
        timezone = timezone.upper()
        try:
            if timezone.startswith('GMT'):
                t = timezone
                if timezone.startswith('GMT+'):
                    t = timezone.replace('+', '-')
                elif timezone.startswith('GMT-'):
                    t = timezone.replace('-', '+')
                tz = pytz.timezone('Etc/' + t)
            else:
                tz = pytz.timezone(timezone)
            await ctx.send("The time in **{0}** is {1}".format(timezone, datetime.datetime.now(tz).strftime(
                "`%H:%M:%S` on `%d-%b-%Y`")))
        except pytz.UnknownTimeZoneError:
            await ctx.send(
                'Couldn\'t find that timezone, make sure to use one from this list: <https://pastebin.com/B5tLQdEY>\nAlso remember that timezones are case sensitive.')

    @commands.command()
    async def urban(self, ctx, *, params):
        """Search up a word on urban dictionary.
        To get another result for the same argument, simply use `urban <word> -number <int>`"""
        params = params.split(' -number ')
        word = params[0]
        if len(params) > 1:
            try:
                num = int(params[1]) - 1
            except:
                await ctx.send(":x: You gave me an improper number!")
                return
        else:
            num = 0
        r = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
        j = r.json()
        try:
            request = j['list'][num]
        except IndexError:
            await ctx.send(":x: There are no more results.")
            return
        definition = request['definition']
        if len(definition) > 1000:
            definition = definition[:997] + "..."
        if definition == "":
            definition = "None"
        example = request['example']
        if len(example) > 1000:
            example = example[:997] + "..."
        if example == "":
            example = "None"
        em = discord.Embed(description=f"Definition #{num+1}", color=ctx.author.color)
        em.add_field(name="Definition", value=definition, inline=False)
        em.add_field(name="Example", value=example, inline=False)
        em.add_field(name="👍", value=request['thumbs_up'], inline=True)
        em.add_field(name="👎", value=request['thumbs_down'], inline=True)
        em.set_author(name=f"Urban dictionary definition for {word}", url=request['permalink'])
        em.set_footer(text=f"Author: {request['author']}")
        await ctx.send(embed=em)

    @commands.command()
    async def choose(self, ctx, *choices):
        """Choose a random item from a list."""
        if len(choices) < 2:
            await ctx.send(":x: I-I need at least two things to choose!")
            return
        await ctx.send(f":thinking: O-oh, you want me to choose? I guess I choose `{random.choice(choices)}`")

    @commands.command(aliases=["len"])
    async def length(self, ctx, *, string: str):
        """Determine the length of a string.
        Note that this does have a joke if the word "dick" is included. To avoid this, end the string with '--bypass'"""
        if 'dick' in string.lower():
            if not string.lower().endswith('--bypass'):
                await ctx.send("\N{CROSS MARK} That is too " + ("small" if 'lars' not in string.lower() else 'long'))
            else:
                await ctx.send(f"\N{WHITE HEAVY CHECK MARK} That string is `{len(string) - 9}` characters long "
                               "(excluding the bypass)")
        else:
            await ctx.send(f"\N{WHITE HEAVY CHECK MARK} The string you gave me is `{len(string)}` characters long.")

    @commands.command(name="8ball", aliases=['mb', 'magicball'])
    async def _8ball(self, ctx, *, question):
        """Consult the magic 8ball with a question!"""
        url = 'https://8ball.delegator.com/magic/JSON/' + urllib.parse.quote_plus(question)
        r = requests.get(url)
        j = r.json()
        q = j['magic']['question']
        a = j['magic']['answer']
        t = j['magic']['type']
        em = discord.Embed(description=f"**Question:** {q}\n**Answer:** {a}\n**Response Type:** {t}", color=0x00ff00)
        em.set_thumbnail(url="https://8ball.delegator.com/images/8ball.png")
        em.set_author(name="You consult the magic 8 ball...", icon_url=ctx.author.avatar_url.replace("?size=1024", ""))
        em.set_footer(text="Powered by 8ball.delegator.com")
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)

    @commands.command()
    async def cat(self, ctx):
        """Get a random cat image!"""
        content = [";w; Don't be sad, here's a cat!",
                   "You seem lonely, {0.display_name}. Here, have a cat".format(ctx.author),
                   "Meeeooowwww!",
                   "Awww, so cute! Look at the kitty!!1!",
                   "Woof... wait wrong animal."]
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/meow') as resp:
                try:
                    js = await resp.json()
                    em = discord.Embed(
                        color=discord.Colour(int(''.join([random.choice('0123456789ABCDEF') for _ in range(6)]), 16)))
                    em.set_image(url=js['url'])
                    await ctx.send(content=random.choice(content), embed=em)
                except:
                    await ctx.send(":x: Error retrieving cat image :<")

    @commands.command()
    async def dog(self, ctx):
        """Get a random cat image!"""
        is_video = True
        url = None
        while is_video:
            r = requests.get('https://random.dog/woof.json')
            js = r.json()
            if js['url'].endswith('.mp4'):
                pass
            else:
                url = js['url']
                is_video = False
        content = [":dog: Don't be sad! This doggy wants to play with you!",
                   "You seem lonely, {0.display_name}. Here, have a dog. They're not as nice as cats, but enjoy!".format(
                       ctx.author),
                   "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait wrong animal."]
        con = int(random.random() * len(content))
        em = discord.Embed(
            color=discord.Colour(int(''.join([random.choice('0123456789ABCDEF') for _ in range(6)]), 16)))
        em.set_image(url=url)
        await ctx.send(content=content[con], embed=em)

    @commands.command()
    async def jumbo(self, ctx, emote: str):
        """Get a larger version of a custom emote."""
        match = re.compile(r"<(a)?:(\w*):(\d*)>").match(emote)
        if match:
            anim = False if not match.group(1) else True
            suffix = ".png" if not anim else ".gif"
            url = f"https://cdn.discordapp.com/emojis/{match.group(3)}{suffix}?size=1024"
            image.save_to_image(url=url, name=match.group(2) + suffix)
            await ctx.send(file=discord.File(f'./images/{match.group(2)}{suffix}'))
            os.remove(f'./images/{match.group(2)}{suffix}')
        else:
            try:
                em = str(emote.encode('unicode_escape'))
                uni = em[2:len(em)-1].replace('\\\\u', '-').replace('\\\\U000', '-')[1:]
                cairosvg.svg2png(url="https://twemoji.maxcdn.com/2/svg/{}.svg".format(uni), write_to="./images/emote.png", parent_width=256, parent_height=256)
                await ctx.send(file=discord.File('./images/emote.png'))
                os.remove('./images/emote.png')
            except urllib.error.HTTPError:
                await ctx.send(":x: That is not a custom or unicode emoji!")

    @commands.command(aliases=["color"])
    async def colour(self, ctx, hexcode: str):
        """Show a preview of a hex colour."""
        colour = hexcode.replace('#', '')
        for char in colour:
            if char not in "abcdef0123456789":
                await ctx.send(":x: T-that's not a valid hex code!")
                return
        if len(colour) != 6:
            await ctx.send(":x: Hex codes are six characters long!")
            return
        c = discord.Color(int(colour, 16))
        em = discord.Embed(color=c)
        em.set_image(url='https://www.colorcombos.com/images/colors/' + colour + '.png')
        em.set_author(name="Here is a preview of your colour.", icon_url=ctx.author.avatar_url_as(format='png'))
        await ctx.send(embed=em)

    @commands.command()
    async def discrim(self, ctx, *, discrim: str):
        """Find users with the discriminator provided.
        If you are unaware, a discriminator is the 4 digit number following your discord name, as seen [here](https://i.imgur.com/kdbY9Nx.png)."""
        discrim = discrim.replace('#', '')
        num = 0
        msg = ""
        for user in self.bot.users.filter(lambda u: u.discriminator == discrim):
            num += 1
            if num == 6:
                break
            msg += f'{user} ({user.id})\n'
        if msg == "":
            return await ctx.send("Found no users with that discriminator.")
        em = discord.Embed(title="Sorted with: User tag (User id)", description=msg, color=ctx.author.color)
        em.set_author(
            name="First 6 users found matching discriminator #{}".format(discrim),
            icon_url=ctx.author.avatar_url.replace("?size=1024", ""))
        em.set_footer(text="Requested by {}".format(str(ctx.message.author)))
        await ctx.send(embed=em)

    @commands.command()
    async def math(self, ctx, *, expression: str):
        """Evaluate complex mathematical equations (or simple ones, whatever you prefer).
        The available operations are as follows:
        `simplify, factor, derive, integrate, zeroes, tangent, area, cos, tan, arccos, arcsin, arctan, abs, log`"""
        available_endpoints = ["simplify", "factor", "derive", "integrate", "zeroes", "tangent", "area", "cos", "tan",
                               "arccos", "arcsin", "arctan", "abs", "log"]
        oper = expression.split(' -operation ')
        op = "simplify"
        if len(oper) > 1:
            try:
                if oper[1].lower() in available_endpoints:
                    op = oper[1].lower()
                else:
                    return await ctx.send(":x: The operation you gave me was invalid.")
            except:
                return await ctx.send(":x: You never gave me an operation. Check the command help.")
        expr = oper[0].replace('/', '%2F')
        r = requests.get("https://newton.now.sh/" + op + "/" + expr)
        try:
            js = r.json()
        except json.decoder.JSONDecodeError:
            return await ctx.send(":x: I-I'm sorry! Something happened with the api.")
        em = discord.Embed(title="Expression Evaluation", color=ctx.message.author.color)
        em.add_field(name="Operation", value=js['operation'], inline=False)
        em.add_field(name="Expression", value=js['expression'], inline=False)
        em.add_field(name="Result", value=js['result'], inline=False)
        em.set_footer(text="Requested by " + str(ctx.message.author))
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)

    @commands.command(aliases=["request"])
    @commands.cooldown(rate=4, per=43200, type=commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion: str):
        """Suggest a feature to be added!
        Has a cooldown of 2 requests per day to prevent spamming."""
        request_channel = self.bot.get_channel(316674935898636289)
        if request_channel is None:  # shouldn't happen but /shrug
            return await ctx.send(":x: Um, I'm sorry? The suggestions channel seems to be missing. "
                                  + "My owner must have deleted it. Sorry. :/ "
                                  + "Feel free to suggest your idea in person at my support server "
                                  + "in **#{}**! (https://discord.gg/ewvvKHM)".format(
                self.bot.get_channel(315252572812214273).name))
        await request_channel.send(f"**User Suggestion By:** {ctx.author} ({ctx.author.id})\n"
                                   + f"**Guild:** {ctx.guild} ({ctx.guild.id})\n"
                                   + f"**Suggestion:** {suggestion.replace('@', '@‍')}")
        await ctx.send(":ok_hand: Got it! Your suggestion has been sent through cyberspace all the way to my owner!")

    @commands.command(aliases=["define"])
    async def dictionary(self, ctx, word: str):
        """Define a word."""
        r = requests.get('http://api.pearson.com/v2/dictionaries/laes/entries?headword=' + word)
        js = r.json()
        if len(js['results']) > 0:
            try:
                define = js['results'][0]['senses'][0]['definition'][0]
                pos = js['results'][0]['part_of_speech']
                ex = js['results'][0]['senses'][0]['translations'][0]['example'][0]['text']
                word = js['results'][0]['headword']
                em = discord.Embed(description="**Part Of Speech:** `{1}`\n**Headword:** `{0}`".format(word, pos),
                                   color=0x8181ff)
                em.set_thumbnail(url="https://www.shareicon.net/download/2016/05/30/575440_dictionary_512x512.png")
                em.set_footer(
                    text="Requested by {} | Powered by http://api.pearson.com/".format(str(ctx.message.author)))
                em.add_field(name="Definition", value="**{}**".format(define))
                em.add_field(name="Example", value="**{}**".format(ex))
                em.set_author(name="Definition for {}".format(word),
                              icon_url=ctx.message.author.avatar_url.replace('?size=1024', ''))
                await ctx.send(embed=em)
            except KeyError:
                await ctx.send(":x: No results found.")
        else:
            await ctx.send(":x: No results found.")

    @commands.command()
    async def remindme(self, ctx, time: str, *, msg: str):
        """Remind yourself of something!"""
        days_match = re.search("(\d*) ?d", time)
        hours_match = re.search("(\d*) ?h", time)
        minutes_match = re.search("(\d*) ?m", time)
        seconds_match = re.search("(\d*) ?s", time)
        days = int(days_match[1]) if days_match is not None else 0
        hours = int(hours_match[1]) if hours_match is not None else 0
        minutes = int(minutes_match[1]) if minutes_match is not None else 0
        seconds = int(seconds_match[1]) if seconds_match is not None else 0
        total = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
        if total <= 10:
            return await ctx.send(":x: That's too little time!")
        m, s = divmod(total, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        dys = round(d)
        hrs = round(h)
        mnts = round(m)
        scnds = round(s)
        t = (f"{dys} day{'s' if dys > 1 else ''} " if dys > 0 else "") + (
            f"{hrs} hour{'s' if hrs > 1 else ''} " if hrs > 0 else "") + (
                f"{mnts} minute{'s' if mnts > 1 else ''} " if mnts > 0 else "") + (
                f"{scnds} second{'s' if scnds > 1 else ''} " if scnds > 0 else "")
        await ctx.send(f":ok_hand: Okay! I'll remind you in " + t)
        await asyncio.sleep(total)
        await ctx.author.send(":wave: You asked me to remind you of: " + msg)

    @commands.command()
    async def unicode(self, ctx, *, character: str):
        """Get the unicodes for the input you give me!"""
        b_string = str(character.encode('unicode_escape'))
        unicode_chars = b_string[2:len(b_string)-1]
        await ctx.send(f"The unicode for `{character}` is: `{unicode_chars}`")


def setup(bot):
    bot.add_cog(Utils(bot))