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
import re

import pytz
from discord.ext import commands
from PIL import ImageColor

from cogs.utils.tools import resolve_emoji
from cogs.utils.checks import is_nsfw


class Utils:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="time")
    async def _time(self, ctx, *, timezone: str):
        """Determine the current time in a timezone specified.
        The timezone is case sensitive as seen in [this list](https://pastebin.com/B5tLQdEY)."""
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
            await ctx.send(resolve_emoji('ERROR',
                                         ctx) + ' Couldn\'t find that timezone, make sure to use one from this list: <https://pastebin.com/B5tLQdEY>\nAlso remember that timezones are case sensitive.')

    @commands.command()
    @is_nsfw()
    @commands.bot_has_permissions(embed_links=True)
    async def urban(self, ctx, *, params):
        """Search up a word on urban dictionary.
        To get another result for the same argument, simply use `urban <word> -number <int>`"""
        params = params.split(' -number ')
        word = params[0]
        if len(params) > 1:
            try:
                num = int(params[1]) - 1
            except:
                await ctx.send(resolve_emoji('ERROR', ctx) + " You gave me an improper number!")
                return
        else:
            num = 0
        r = await self.bot.session.get(f"http://api.urbandictionary.com/v0/define?term={word}")
        j = await r.json()
        try:
            request = j['list'][num]
        except IndexError:
            await ctx.send(resolve_emoji('ERROR', ctx) + " There are no more results.")
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
            await ctx.send(resolve_emoji('ERROR', ctx) + " I-I need at least two things to choose!")
            return
        await ctx.send(f":thinking: O-oh, you want me to choose? I guess I choose `{random.choice(choices)}`")

    @commands.command(aliases=["len"])
    async def length(self, ctx, *, string: str):
        """Determine the length of a string.
        Note that this does have a joke if the word "dick" is included. To avoid this, end the string with '--bypass'"""
        if 'dick' in string.lower():
            if not string.lower().endswith('--bypass'):
                await ctx.send(resolve_emoji('ERROR', ctx) + " That is too " + (
                    "small" if 'lars' not in string.lower() else 'long'))
            else:
                await ctx.send(resolve_emoji('SUCCESS', ctx) + f" That string is `{len(string) - 9}` characters long "
                                                               "(excluding the bypass)")
        else:
            await ctx.send(
                resolve_emoji('SUCCESS', ctx) + f" The string you gave me is `{len(string)}` characters long.")

    @commands.command(name="8ball", aliases=['mb', 'magicball'])
    async def _8ball(self, ctx, *, question):
        """Consult the magic 8ball (tsundere edition) with a question!"""
        answers = [
            'Y-yes...',  # y
            'U-uh, sure!',  # y
            'I mean, n-not like I want to say y-yes or anything... b-baka!',  # y
            'S-Sure, you baka!',  # y
            'O-of course!',  # y
            'I-I don\'t know, b-baka!',  # i
            'I\'m not all-knowing, you baka tako!',  # i
            'Baka! How am I supposed to know that?',  # i
            'I-I\'m b-busy right now, you baka...',  # i
            'N-not like I want to g-give you an answer or anything!',  # i
            'B-baka!',  # i
            'B-Baka! Don\'t make me slap you!',  # n
            'N-no...',  # n
            'I t-told you no, b-baka!',  # n
            'Are you dumb?',  # n
            'N-no... I-it\'s not like I\'m s-sorry about that or anything!',  # n
            'No, you b-baka tako!',  # n
            'N-no, you baka!',  # n
            'Geez, stop pushing yourself! You\'re going to get yourself hurt one day, you idiot!'  # n
        ]
        if re.compile('will you go out with me\??').match(question.lower()):
            return await ctx.send(resolve_emoji('TSUNDERE',
                                                ctx) + ' W-why are y-you asking! I-it\'s not like I l-like you or anything...')
        await ctx.send(resolve_emoji('TSUNDERE', ctx) + ' ' + random.choice(answers))

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cat(self, ctx):
        """Get a random cat image!"""
        content = [";w; Don't be sad, here's a cat!",
                   "You seem lonely, {0.display_name}. Here, have a cat".format(ctx.author),
                   "Meeeooowwww!",
                   "Awww, so cute! Look at the kitty!!1!",
                   "Woof... wait wrong animal."]
        async with self.bot.session.get('https://nekos.life/api/v2/img/meow') as resp:
            try:
                js = await resp.json()
                em = discord.Embed(
                    color=discord.Colour(int(''.join([random.choice('0123456789ABCDEF') for _ in range(6)]), 16)))
                em.set_image(url=js['url'])
                await ctx.send(content=random.choice(content), embed=em)
            except:
                await ctx.send(resolve_emoji('ERROR', ctx) + " Error retrieving cat image :<")

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def dog(self, ctx):
        """Get a random dog image!"""
        is_video = True
        url = None
        while is_video:
            r = await self.bot.session.get('https://random.dog/woof.json')
            js = await r.json()
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
    @commands.bot_has_permissions(attach_files=True)
    async def jumbo(self, ctx, emote: str):
        """Get a larger version of a custom emote."""
        match = re.compile(r"<(a)?:(\w*):(\d*)>").match(emote)
        if match:
            anim = False if not match.group(1) else True
            suffix = ".png" if not anim else ".gif"
            url = f"https://cdn.discordapp.com/emojis/{match.group(3)}{suffix}?size=1024"
            img = await (await self.bot.session.get(url)).read()
            await ctx.send(file=discord.File(img, filename=f'{match.group(2)}{suffix}'))
        else:
            try:
                em = str(emote.encode('unicode_escape'))
                uni = em[2:len(em) - 1].replace('\\\\u', '-').replace('\\\\U000', '-')[1:]
                cairosvg.svg2png(url="https://twemoji.maxcdn.com/2/svg/{}.svg".format(uni),
                                 write_to="./images/emote.png", parent_width=256, parent_height=256)
                await ctx.send(file=discord.File('./images/emote.png'))
                os.remove('./images/emote.png')
            except urllib.error.HTTPError:
                await ctx.send(resolve_emoji('ERROR', ctx) + " That is not a custom or unicode emoji!")

    @commands.command(aliases=["color"])
    @commands.bot_has_permissions(embed_links=True)
    async def colour(self, ctx, hexcode: str):
        """Show a preview of a hex colour."""
        if hexcode.startswith("0x") or hexcode.startswith("#"):
            hexcode = hexcode.strip("0x#")
        match = re.compile(r'^[^g-zG-Z]{6}$').match(hexcode)
        if not match:
            return await ctx.send(
                resolve_emoji('ERROR', ctx) + " I-I'm sorry, that doesn't look like a hex colour to me.")
        hexcode = f'{match.group()}'
        try:
            rgb = ImageColor.getrgb('#' + hexcode)
        except ValueError:
            return await ctx.send(resolve_emoji('ERROR',
                                                ctx) + " S-sorry! Something happened parsing this hexcode. I'll be better next time!")
        c = discord.Color(int(match.group(), 16))
        em = discord.Embed(color=c)
        em.set_image(
            url="https://crimsonxv.pro/rendercolour?rgb={r},{g},{b}".format(r=rgb[0], g=rgb[1], b=rgb[2]))
        em.set_author(name="Here's the colour you wanted!", icon_url=ctx.author.avatar_url_as(format='png'))
        await ctx.send(embed=em)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def discrim(self, ctx, *, discrim: str):
        """Find users with the discriminator provided.
        If you are unaware, a discriminator is the 4 digit number following your discord name, as seen [here](https://i.imgur.com/kdbY9Nx.png)."""
        discrim = discrim.replace('#', '')
        num = 0
        msg = ""
        for user in filter(lambda u: u.discriminator == discrim, self.bot.users):
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
    @commands.bot_has_permissions(embed_links=True)
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
                    return await ctx.send(resolve_emoji('ERROR', ctx) + " S-Sorry! That operation seems invalid")
            except:
                return await ctx.send(
                    resolve_emoji('ERROR',
                                  ctx) + " Y-you need to give me a valid operation! I made a list for you in the command help.")
        expr = oper[0].replace('/', '%2F')
        r = requests.get("https://newton.now.sh/" + op + "/" + expr)
        try:
            js = r.json()
        except json.decoder.JSONDecodeError:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " I-I'm sorry! Something happened with the api.")
        em = discord.Embed(title="Expression Evaluation", color=ctx.message.author.color)
        em.add_field(name="Operation", value=js['operation'], inline=False)
        em.add_field(name="Expression", value=js['expression'], inline=False)
        em.add_field(name="Result", value=js['result'], inline=False)
        em.set_footer(text="Requested by " + str(ctx.message.author))
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)

    @commands.command(aliases=["request"])
    @commands.cooldown(rate=2, per=86400, type=commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion: str):
        """Suggest a feature to be added!
        Has a cooldown of 2 requests per day to prevent spamming."""
        request_channel = self.bot.get_channel(316674935898636289)
        if request_channel is None:  # shouldn't happen but /shrug
            return await ctx.send(
                resolve_emoji('ERROR', ctx) + " Um, I'm sorry? The suggestions channel seems to be missing. "
                + "My owner must have deleted it. Sorry. :/ "
                + "Feel free to suggest your idea in person at my support server "
                + "in **#suggestions**! (https://discord.gg/ewvvKHM)")
        suggestion = suggestion.replace('@everyone', '@\u200Beveryone').replace('@here', '@\u200Bhere')
        await request_channel.send(f"**User Suggestion By:** {ctx.author} ({ctx.author.id})\n"
                                   + f"**Guild:** {ctx.guild} ({ctx.guild.id})\n"
                                   + f"**Suggestion:** {suggestion}")
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
                await ctx.send(resolve_emoji('ERROR', ctx) + " No results found.")
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + " No results found.")

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
            return await ctx.send(resolve_emoji('ERROR', ctx) + " That's too little time!")
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
        try:
            await ctx.author.send(":wave: You asked me to remind you of: " + msg)
        except:
            await ctx.send(ctx.author.mention + ': Sorry, I couldn\'t DM you, but you asked to be reminded of: ' + msg)

    @commands.command()
    async def unicode(self, ctx, *, character: str):
        """Get the unicodes for the input you give me!"""
        b_string = str(character.encode('unicode_escape'))
        unicode_chars = b_string[2:len(b_string) - 1]
        await ctx.send(f"The unicode for `{character}` is: `{unicode_chars}`")

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def snipe(self, ctx):
        """Snipe a recently deleted message in this channel."""
        try:
            snipe = self.bot.snipes[str(ctx.channel.id)]
        except KeyError:
            return await ctx.send(resolve_emoji('ERROR', ctx) + f' No recently deleted messages found here.')
        em = discord.Embed(description=snipe['message'], color=ctx.author.color)
        em.set_author(name=str(snipe['author']), icon_url=snipe['author'].avatar_url)
        em.set_footer(text=f'Sniped by {ctx.author} | Sniped at', icon_url=ctx.author.avatar_url)
        em.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=em)

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.bot_has_permissions(embed_links=True)
    async def iam(self, ctx, *, name: str):
        """Claim a self assignable role.
        Do `iam list` for a list of all."""
        results = self.bot.query_db(f'''SELECT self_roles FROM settings WHERE guildid={ctx.guild.id};''')
        selfroles = json.loads(results[0][0].replace("'", '"')) if results and results[0][0] else json.loads('{}')
        if name in ['list', 'ls']:
            msg = ''
            for key in selfroles.keys():
                if discord.utils.get(ctx.guild.roles, id=selfroles[key]):
                    msg += f'**Self role name:** {key} | **Gives:** {discord.utils.get(ctx.guild.roles, id=selfroles[key])}\n'
            em = discord.Embed(title='All Self Assignable Roles', description=msg if msg != '' else 'None (yet!)',
                               color=ctx.author.color)
            em.set_footer(text='Requested by ' + ctx.author.display_name)
            return await ctx.send(embed=em)
        try:
            role = discord.utils.get(ctx.guild.roles, id=selfroles[name])
            if role:
                if role not in ctx.author.roles:
                    await ctx.author.add_roles(role, reason='Self Assignable Role')
                    await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Gave you the **{role}** role.')
                else:
                    await ctx.send(resolve_emoji('ERROR', ctx) + ' Silly, I can\'t give you a role you already have.')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + ' The role corresponding to this self role was deleted.')
        except discord.Forbidden:
            await ctx.send(resolve_emoji('ERROR',
                                         ctx) + ' I could not give you that role. Make sure to contact an admin to check that my highest role is above the role trying to be assigned.')

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    async def iamnot(self, ctx, *, name: str):
        """Remove a self assignable role."""
        results = self.bot.query_db(f'''SELECT self_roles FROM settings WHERE guildid={ctx.guild.id};''')
        selfroles = json.loads(results[0][0].replace("'", '"')) if results and results[0][0] else json.loads('{}')
        try:
            role = discord.utils.get(ctx.guild.roles, id=selfroles[name])
            if role:
                if role in ctx.author.roles:
                    await ctx.author.remove_roles(role, reason='Self Assignable Role')
                    await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Removed the **{role}** role from you.')
                else:
                    await ctx.send(resolve_emoji('ERROR', ctx) + ' Silly, I can\'t take a role that you don\'t have.')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + ' The role corresponding to this self role was deleted.')
        except discord.Forbidden:
            await ctx.send(resolve_emoji('ERROR',
                                         ctx) + ' I could not take that role from you. Make sure to contact an admin to check that my highest role is above the role trying to be assigned.')


def setup(bot):
    bot.add_cog(Utils(bot))
