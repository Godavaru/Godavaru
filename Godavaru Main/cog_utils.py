# -*- coding: UTF-8 -*-
# Discord
import discord
from discord.ext import commands
from utils.tools import *
from discord import Webhook, RequestsWebhookAdapter

# Useful
import os
import re
import json
import asyncio
import random
import math
import time
import traceback
import platform
import datetime
import requests
import inspect

# Other
import pytz
import aiohttp
import configparser
import sqlite3
import threading
import urllib
import hastebin

# Code Interpreters
#import js2py

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

class Utils():
    def __init__(self, bot):
        self.bot = bot

    def randomColour(self):
        co = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = int(random.random() * len(co))
        b = int(random.random() * len(co))
        c = int(random.random() * len(co))
        d = int(random.random() * len(co))
        e = int(random.random() * len(co))
        f = int(random.random() * len(co))
        col = "{}{}{}{}{}{}".format(co[a], co[b], co[c], co[d], co[e], co[f])
        return discord.Colour(int(col, 16))

    @commands.command(name="time")
    async def _time(self, ctx):
        """Determine the current time in a timezone specified.
        The timezone is case sensitive as seen in [this list](https://pastebin.com/B5tLQdEY).

        **Usage:** `g_time <timezone>

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(args) > 1:
            try:
                if args[1].startswith('GMT'):
                    if args[1].startswith('GMT+'):
                        t = args[1].replace('+', '-')
                    elif args[1].startswith('GMT-'):
                        t = args[1].replace('-', '+')
                    tz = pytz.timezone('Etc/'+t)
                else:
                    tz = pytz.timezone(args[1])
                await ctx.send("The time in **{0}** is {1}".format(args[1], datetime.datetime.now(tz).strftime("`%H:%M:%S` on `%d-%b-%Y`")))
            except pytz.UnknownTimeZoneError:
                await ctx.send('Couldn\'t find that timezone, make sure to use one from this list: <https://pastebin.com/B5tLQdEY>\nAlso remember that timezones are case sensitive.')
        else:
            await ctx.send(":x: Usage: `{}time <timezone>`".format(self.bot.command_prefix[0]))

    @commands.command(name="embed")
    async def _embed(self, ctx):
        """Create an embed using the embed builder.

        Note that this feature is 100% experimental and probably will not work. A tutorial will be provided soon.

        **Usage:** `g_embed <args split with an |>`

        **Permission:** User"""
        umsg = ctx.message.content
        smsg = umsg.split(' ')
        msg = umsg.replace(smsg[0], "")
        msg = msg[1:]
        args = msg.split(' | ')
        if not msg == "":
            for i in range(0, len(args)):
                if args[i].startswith('title:'):
                    t = args[i].replace('title:', "")
                if args[i].startswith('description:'):
                    d = args[i].replace('description:', '')
                if args[i].startswith('color:'):
                    c = args[i].replace('color:', '')
                    co = discord.Color(int(str(c), 16))
            try:
                t
            except NameError:
                t = None
            try:
                d
            except NameError:
                d = None
            try:
                co
            except NameError:
                co = 0x000000
            em = discord.Embed(title=t,description=d,color=co)
            for x in range(0, len(args)):
                if args[x].startswith('addfield:'):
                    addfieldname = args[x].replace('addfield:', "")
                    fieldargs = addfieldname.split(',')
                    if len(fieldargs) > 2:
                        if fieldargs[2] == "False":
                            isInline = False
                        else:
                            isInline = True
                    else:
                        isInline = True
                    em.add_field(name=fieldargs[0],value=fieldargs[1],inline=isInline)
                if args[x].startswith('footer:'):
                    f = args[x].replace('footer:', '')
                    footerargs = f.split(',')
                    if len(footerargs) > 1:
                        iconURL = footerargs[1]
                    else:
                        iconURL = None
                    em.set_footer(icon_url=iconURL,text=footerargs[0])
                if args[x].startswith('image:'):
                    img = args[x].replace('image:', '')
                    em.set_image(url=img)
                if args[x].startswith('thumbnail:'):
                    thumb = args[x].replace('thumbnail:', '')
                    em.set_thumbnail(url=thumb)
                if args[x].startswith('author:'):
                    auth = args[x].replace('author:', '')
                    authargs = auth.split(',')
                    if len(authargs) > 1:
                        iconURL = authargs[1]
                    else:
                        iconURL = None
                    em.set_author(name=authargs[0],icon_url=iconURL)
            await ctx.send(embed=em)
        else:
            await ctx.send(":x: You need at least one argument, split with `|` (guide coming soon)")

    @commands.command()
    async def quote(self, ctx):
        """Get a message from either the current channel or a specified channel.

        **Usage:** `g_quote [channel id] <message id>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if '--s' in umsg:
            await ctx.message.delete()
        if len(args) > 1:
            try:
                if len(args) > 2:
                    channel = self.bot.get_channel(int(args[1]))
                    msg = await channel.get_message(int(args[2]))
                else:
                    channel = ctx.message.channel
                    msg = await channel.get_message(int(args[1]))
                em = discord.Embed(title="Found message!",description=msg.content,color=self.randomColour())
                em.set_footer(text='Author: {}'.format(str(msg.author)))
                em.timestamp = msg.created_at
                await ctx.send(embed=em)
            except ValueError:
                await ctx.send(":x: Please enter an id (or multiple) to find a message.")
            except discord.NotFound:
                await ctx.send(":x: I'm sorry, but I couldn't find that message. :sob:")
        else:
            await ctx.send("Improper arguments.")

    @commands.command()
    async def list(self, ctx):
        """List something that is in the following list.

        You can list from: `bans` `channels` `emojis` `users` `roles`
        Note that sometime, listing will throw a `Forbidden` error. This means that the bot cannot access what you are trying to list. To fix this, just give the bot the needed permissions.

        **Usage:** `g_list <item>`

        **Permission:** User"""
        args = ctx.message.content
        args = args.split(' ')
        allBots = 0
        allUsers = 0
        for member in ctx.message.guild.members:
            if member.bot == True:
                allBots += 1
            if member.bot == False:
                allUsers += 1
        try:
            if args[1] == "bans":
                banned = await ctx.message.guild.bans()
                msg = "**All Banned Users** -- ({})\n".format(len(banned))
                for bu in sorted(banned, key=lambda x: x.user.name):
                    msg = msg+"`"+str(bu.user)+" - "+str(bu.reason)+"`\n"
                if len(msg) > 2000:
                    msg = msg.encode('utf-8')
                    await ctx.send(hastebin.post(msg))
                    return
                await ctx.send(msg)
            elif args[1] == "channels":
                msg = "**All Channels** -- ({})\n".format(len(ctx.message.guild.channels))
                vcmsg = "**Voice Channels**\n"
                for channel in sorted(ctx.message.guild.channels, key=lambda x: x.position):
                    if isinstance(channel, discord.TextChannel):
                        msg = msg+"#"+channel.name+"\n"
                    if isinstance(channel, discord.VoiceChannel):
                        vcmsg = vcmsg+channel.name+"\n"
                sendThis = msg+vcmsg
                if len(sendThis) > 2000:
                    sendThis = sendThis.encode('utf-8')
                    await ctx.send(hastebin.post(sendThis))
                    return
                await ctx.send(sendThis)
            elif args[1] == "emojis":
                msg = "**All Emojis** -- ({})\n".format(len(ctx.message.guild.emojis))
                for emoji in sorted(ctx.message.guild.emojis, key=lambda x: x.name):
                    msg = msg+":"+emoji.name+": - "+str(emoji)+"\n"
                if len(msg) > 2000:
                    msg = msg.encode('utf-8')
                    await ctx.send(hastebin.post(msg))
                    return
                await ctx.send(msg)
            elif args[1] == "users":
                try:
                    if args[2] == "all":
                        msg = "**All Users** -- ({})\n".format(len(ctx.message.guild.members))
                        for member in sorted(ctx.message.guild.members, key=lambda x: x.name.lower()):
                            msg = msg+"`{}`\n".format(str(member))
                        if len(msg) > 2000:
                            msg = msg.encode('utf-8')
                            await ctx.send(hastebin.post(msg))
                            return
                        await ctx.send(msg)
                        return
                    else:
                        msg = ""
                        c = 0
                        for member in sorted(ctx.message.guild.members, key=lambda x: x.name.lower()):
                            if member.name.lower().startswith(args[2].lower()):
                                msg += "`{}`\n".format(str(member))
                                c += 1
                        if len(msg) > 2000:
                            msg = msg.encode('utf-8')
                            await ctx.send(hastebin.post("**All Users With Names Starting With `{0}`** -- ({1})\n".format(args[2], c)+msg))
                            return
                        await ctx.send("**All Users With Names Starting With `{0}`** -- ({1})\n".format(args[2], c)+msg)
                        return
                except IndexError:
                    pass
                msg = "**All Users** -- ({})\n".format(allUsers)
                for member in sorted(ctx.message.guild.members, key=lambda x: x.name.lower()):
                    if member.bot == False:
                        msg = msg+"`{}`\n".format(str(member))
                if len(msg) > 2000:
                    msg = msg.encode('utf-8')
                    await ctx.send(hastebin.post(msg))
                    return
                await ctx.send(msg)
            elif args[1] == "bots":
                msg = "**All Bots** -- ({})\n".format(allBots)
                for member in sorted(ctx.message.guild.members, key=lambda x: x.name.lower()):
                    if member.bot == True:
                        msg = msg+"`{}`\n".format(str(member))
                if len(msg) > 2000:
                    msg = msg.encode('utf-8')
                    await ctx.send(hastebin.post(msg))
                    return
                await ctx.send(msg)
            elif args[1] == "roles":
                msg = "**All Roles** -- ({})\n".format(len(ctx.message.guild.roles)-1)
                for role in sorted(ctx.message.guild.roles, key=lambda x: -x.position):
                    if role.is_default():
                        continue
                    msg = msg+"`{}`\n".format(role.name)
                if len(msg) > 2000:
                    msg = msg.encode('utf-8')
                    await ctx.send(hastebin.post(msg))
                    return
                await ctx.send(msg)
            else:
                await ctx.send(":x: Not a valid thing I can list.")
            if '--s' in ctx.message.content:
                await bot.delete_message(ctx.message)
        except IndexError:
            await ctx.send(":x: You can list `bans` `channels` `emojis` `users` `roles`")

    @commands.command(aliases=["ud"])
    async def urban(self, ctx):
        """Search a word on urban dictionary.

        **Usage:** `g_urban <word>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(args) > 1:
            try:
                num = int(args[1]) - 1
                word = umsg.replace(args[0]+" "+args[1], "")
                word = word[1:]
            except ValueError:
                num = 0
                word = umsg.replace(args[0], "")
                word = word[1:]
            r = requests.get('http://api.urbandictionary.com/v0/define?term='+word)
            js = r.json()
            if js['result_type'] == "no_results":
                await ctx.send(":x: No results for `{}`.".format(word))
            else:
                if num > -1:
                    try:
                        define = js['list'][num]['definition']
                        example = js['list'][num]['example']
                        perma = js['list'][num]['permalink']
                        up = js['list'][num]['thumbs_up']
                        down = js['list'][num]['thumbs_down']
                        defWord = js['list'][num]['word']
                        author = js['list'][num]['author']
                    except IndexError:
                        await ctx.send(":x: There are no more definitions. Try with a lower number.")
                        return
                elif num < -1:
                    await ctx.send(":x: Nice try, don't search for negative numbers.")
                    return
                elif num == -1:
                    await ctx.send(":x: Nice try, don't search for the 0th definition.")
                    return
                if num == 0:
                    desc = "Main definition."
                else:
                    desc = "Definition "+str(num+1)
                em = discord.Embed(description=desc,colour=0x66daff)
                if len(str(define)) > 1000:
                    define = define[:996]+"... (continued in permalink)"
                else:
                    define = define
                em.add_field(name="Definition",value=define,inline=False)
                if example == "":
                    example = "‎"
                elif len(str(example)) > 1000:
                    example = example[:996]+"... (continued in permalink)"
                else:
                    example = example
                em.add_field(name="Example",value=example,inline=False)
                em.add_field(name="Permalink",value=perma,inline=False)
                em.add_field(name="\uD83D\uDC4D",value=str(up))
                em.add_field(name="\uD83D\uDC4E",value=str(down))
                em.set_author(name="Urban Dictionary definition for "+defWord, url=perma)
                em.set_thumbnail(url="http://www.socialbookshelves.com/wp-content/uploads/2015/04/UD-logo.jpg")
                em.set_footer(text="Author: "+author+" | Powered by http://api.urbandictionary.com")
                try:
                    await ctx.send(embed=em)
                except Exception as e:
                    await ctx.send("`ERROR` ```py\n{}```".format(type(e).__name__+": "+str(e)))
        else:
            await ctx.send("Search for a word!")


    @commands.command(aliases=["length"])
    async def len(self, ctx):
        """Get the length of a string, as provided by the `len()` function in Python.

        **Usage:** `g_len <content>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        toLen = umsg.replace(args[0], "")
        toLen = toLen[1:]
        if toLen == "":
            await ctx.send(":x: Specify a message that I can find the length of.")
            return
        await ctx.send(":white_check_mark: The message you gave me is `{}` characters long.".format(len(toLen)))


    @commands.command(aliases=["nekos"])
    async def catgirls(self, ctx):
        """Get some neko images from nekos.life

        Make sure to specify the second parameter as `nsfw` if you want it to be lewd images. (only in NSFW channels)

        **Usage:** `g_catgirls [nsfw]`

        **Permission:** User"""
        args = ctx.message.content
        args = args.split(' ')
        if len(args) > 1:
            if args[1] == "nsfw":
                if ctx.message.channel.is_nsfw():
                    r = requests.get('http://nekos.life/api/lewd/neko')
                    js = r.json()
                    img = js['neko']
                else:
                    await ctx.send(":x: Can't send lewd/questionable images in a non-nsfw channel.")
                    return
            else:
                r = requests.get('http://nekos.life/api/neko')
                js = r.json()
                img = js['neko']
        else:
            r = requests.get('http://nekos.life/api/neko')
            js = r.json()
            img = js['neko']
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        em = discord.Embed(color=colours[col])
        em.set_image(url=img)
        await ctx.send(embed=em)


    @commands.command(name="8ball",aliases=["mb", "magicball"])
    async def _8ball(self, ctx):
        """Consult the magic 8ball with a question.

        **Usage:** `g_8ball <question>`

        **Permission:** User"""
        umsg = ctx.message.content
        omsg = umsg.split(' ')
        args = umsg.replace(omsg[0], "")
        args = args[1:]
        if args != "":
            r = requests.get('https://8ball.delegator.com/magic/JSON/'+args)
            js = r.json()
            answer = js['magic']['answer']
            await ctx.send(":crystal_ball: {}.".format(answer))
        else:
            await ctx.send(":x: Specify a question.")


    @commands.command()
    async def cat(self, ctx):
        """Get a random cat image!

        **Usage:** `g_cat`

        **Permission:** User"""
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        content = [";w; Don't be sad, here's a cat!", "You seem lonely, {0.mention}. Here, have a cat".format(ctx.message.author), "Meeeooowwww!", "Awww, so cute! Look at the kitty!!1!", "Woof... wait wrong animal."]
        con = int(random.random() * len(content))
        r = requests.get('http://random.cat/meow')
        js = r.json()
        em = discord.Embed(color=colours[col])
        em.set_image(url=js['file'])
        await ctx.send(content=content[con], embed=em)


    @commands.command()
    async def dog(self, ctx):
        """Get a random cat image!

        **Usage:** `g_dog`

        **Permission:** User"""
        isVideo = True
        while isVideo:
            r = requests.get('https://random.dog/woof.json')
            js = r.json()
            if js['url'].endswith('.mp4'):
                pass
            else:
                isVideo = False
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        content = [":dog: Don't be sad! This doggy wants to play with you!", "You seem lonely, {0.mention}. Here, have a dog. They're not as nice as cats, but enjoy!".format(ctx.message.author), "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait wrong animal."]
        con = int(random.random() * len(content))
        em = discord.Embed(color=colours[col])
        em.set_image(url=js['url'])
        await ctx.send(content=content[con], embed=em)

    @commands.command()
    async def jumbo(self, ctx):
        """Get a closer look at a custom emoji.

        **Usage:** `g_jumbo <custom emoji>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        try:
            emote = args[1]
        except IndexError:
            await ctx.send(":x: That is not a custom emote.")
            return
        emote_id = None
        try:
            if extract_emote_id(emote) is not None:
                emote_id = extract_emote_id(emote)
        except:
            pass
        if emote_id is None:
            await ctx.send(":x: That is not a custom emote.")
            return
    
        emote_url = "https://cdn.discordapp.com/emojis/{}.png".format(emote_id)
        o = AppURLopener()
        r = o.open(emote_url)
        data = r.read()
        with open("./images/emotes/{}.png".format(emote_id), "wb") as avatar:
            avatar.write(data)
            avatar.close()
        await ctx.send(file=discord.File("./images/emotes/{}.png".format(emote_id)))

    @commands.command()
    async def discrim(self, ctx):
        """Find users with the discriminator provided.
        If you are unaware, a discriminator is the 4 didgit number following your discord name, as seen [here](https://i.imgur.com/kdbY9Nx.png).

        **Usage:** `g_discrim <discrim>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(args) > 1:
            da = []
            for guild in self.bot.guilds:
                for member in guild.members:
                    if str(member.discriminator) == str(args[1]):
                        if str(member)+" ({})\n".format(str(member.id)) not in da:
                            if len(da) < 7:
                                da += [str(member)+" ({})\n".format(str(member.id))]
            d = ""
            for i in range(0, len(da)):
                d += da[i]
            if d == "":
                await ctx.send("Couldn't find a user with that discriminator.")
                return
            em = discord.Embed(title="Sorted with: User tag (User id)",description=d, color=ctx.message.author.color)
            em.set_author(name="First 6 users found matching discriminator #{}".format(args[1]), icon_url=ctx.message.author.avatar_url.replace("?size=1024", ""))
            em.set_footer(text="Requested by {}".format(str(ctx.message.author)))
            await ctx.send(embed=em)
        else:
            await ctx.send("Specify a discriminator")

    @commands.command()
    async def math(self, ctx):
        """Evaluate complex mathematical equations (or simple ones, whatever you prefer).
        The available operations are as follows:```
        simplify, factor, derive, integrate, zeroes, tangent, area, cos, tan, arccos, arcsin, arctan, abs, log```
        **Usage:** `g_math <equation> -operation [operation]`
            For example, `g_math 5(x+5)^2 -operation factor` or simply `g_math 5*5` to leave the operation as `simplify`

        **Permission:** User"""
        availableEndpoints = ["simplify", "factor", "derive", "integrate", "zeroes", "tangent", "area", "cos", "tan", "arccos", "arcsin", "arctan", "abs", "log"]
        umsg = ctx.message.content
        args = umsg.split(' ')
        ex = umsg.replace(args[0], "")
        ex = ex[1:]
        oper = ex.split('-operation ')
        if len(oper) > 1:
            if oper[1].lower() in availableEndpoints:
                op = oper[1].lower()
            else:
                await ctx.send(":x: The operation you gave me was invalid.")
                return
        else:
            if "-operation" in umsg:
                ol = ""
                for operation in availableEndpoints:
                    ol += operation+"\n"
                await ctx.send(":x: You never gave me an operation. Choose from:\n`\n{}\n`".format(ol))
                return
            else:
                op = "simplify"
        expr = oper[0]
        if '/' in expr:
            n = expr.split('/')
            x = expr.replace(n[0]+'/', "")
            if x.startswith(' '):
                x = x[1:]
            y = x.split(' ')
            try:
                z = x.replace(y[1], "")
            except IndexError:
                z = x
            expr = expr.replace("/"+z, "* {}^(-1)".format(z))
            expr = expr.replace("/ "+z, "* {}^(-1)".format(z))
        r = requests.get("https://newton.now.sh/"+op+"/"+expr)
        try:
            js = r.json()
        except json.decoder.JSONDecodeError:
            await ctx.send(":x: I-I'm sorry! Something happened with the api.")
            return
        em = discord.Embed(title="Expression Evaluation",color=ctx.message.author.color)
        em.add_field(name="Operation",value=js['operation'],inline=False)
        em.add_field(name="Expression",value=js['expression'],inline=False)
        em.add_field(name="Result",value=js['result'],inline=False)
        em.set_footer(text="Requested by "+str(ctx.message.author))
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)

    @commands.command()
    async def ytmp3(self, ctx):
        """Convert a youtube link to an MP3 file download.
        Some videos do not work purely due to how the API works. This cannot be helped.

        **Usage:** `g_ytmp3 <link>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        msg = umsg.replace(args[0], "")
        msg = msg[1:]
        if msg == "":
            await ctx.send(":x: Give me a link.")
            return
        else:
            try:
                link = msg.replace('https://youtu.be/', 'https://www.youtube.com/watch?v=')
                link = link.replace('https://m.youtube.com/', 'https://www.youtube.com/')
                r = requests.get('http://www.youtubeinmp3.com/fetch/?format=JSON&video='+link)
                js = r.json()
                title = js['title']
                timestamp = int(js['length'])
                dllink = js['link']
            except KeyError:
                await ctx.send(":x: That doesn't seem to be a valid link :<")
                return
            except json.decoder.JSONDecodeError:
                await ctx.send(":x: Something happened with the api. Please try again with a different link.")
                return
            em = discord.Embed(color=0x66dffa)
            em.set_author(name=title, icon_url=ctx.message.author.avatar_url.replace('?size=1024', ''), url=link)
            em.add_field(name="Video Length", value=time.strftime("%M minutes, %S seconds.", time.gmtime(timestamp)),inline=False)
            em.add_field(name="Download Link",value="[Click this link!]({})".format(dllink),inline=False)
            em.set_footer(text="Powered by http://www.youtubeinmp3.com/")
            await ctx.send(embed=em)

    @commands.command(aliases=["define"])
    async def dictionary(self, ctx):
        """Define a word.

        **Usage:** `g_dictionary <word>`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(args) > 1:
            word = args[1]
            r = requests.get('http://api.pearson.com/v2/dictionaries/laes/entries?headword='+word)
            js = r.json()
            if len(js['results']) > 0:
                try:
                    define = js['results'][0]['senses'][0]['definition'][0]
                    pos = js['results'][0]['part_of_speech']
                    ex = js['results'][0]['senses'][0]['translations'][0]['example'][0]['text']
                    word = js['results'][0]['headword']
                    em = discord.Embed(description="**Part Of Speech:** `{1}`\n**Headword:** `{0}`".format(word, pos),color=0x8181ff)
                    em.set_thumbnail(url="https://www.shareicon.net/download/2016/05/30/575440_dictionary_512x512.png")
                    em.set_footer(text="Requested by {} | Powered by http://api.pearson.com/".format(str(ctx.message.author)))
                    em.add_field(name="Definition",value="**{}**".format(define))
                    em.add_field(name="Example",value="**{}**".format(ex))
                    em.set_author(name="Definition for {}".format(word), icon_url=ctx.message.author.avatar_url.replace('?size=1024', ''))
                    await ctx.send(embed=em)
                except KeyError:
                    await ctx.send(":x: No results found.")
            else:
                await ctx.send(":x: No results found.")
        else:
            await ctx.send(":x: Specify a word to define.")

    @commands.command(name="permissions",aliases=["perms"])
    async def _permissions(self, ctx):
        """Get a user's server permissions via either mention or id, or leave blank to get your own permissions.

        **Usage:** `g_permissions [user]`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0]
        else:
            try:
                user = ctx.message.guild.get_member(args[1])
            except (IndexError, discord.NotFound):
                user = ctx.message.author
        em = discord.Embed(title="Server Permissions for {}".format(str(user)),color=user.color)
        emb = discord.Embed(title="Server Permissions for {} (cont.)".format(str(user)),color=user.color)
        up = user.guild_permissions
        # Embed #1
        em.add_field(name="Can create invite",value=up.create_instant_invite)
        em.add_field(name="Can Kick Members",value=up.kick_members)
        em.add_field(name="Can Ban Members",value=up.ban_members)
        em.add_field(name="Is Administrator",value=up.administrator)
        em.add_field(name="Can Manage Channels",value=up.manage_channels)
        em.add_field(name="Can Manage Server",value=up.manage_guild)
        em.add_field(name="Can Add Reactions",value=up.add_reactions)
        em.add_field(name="Can View Audit Logs",value=up.view_audit_log)
        em.add_field(name="Can Read Messages",value=up.read_messages)
        em.add_field(name="Can Send Messages",value=up.send_messages)
        em.add_field(name="Can Send TTS Messages",value=up.send_tts_messages)
        em.add_field(name="Can Manage Messages",value=up.manage_messages)
        em.add_field(name="Can Embed Links",value=up.embed_links)
        em.add_field(name="Can Attach Files",value=up.attach_files)
        em.add_field(name="Can Read Message History",value=up.read_message_history)
        em.add_field(name="Is Owner",value=(ctx.message.guild.owner == user))
        # Embed #2
        emb.add_field(name="Can Mention Everyone",value=up.mention_everyone)
        emb.add_field(name="Can Use External Emojis",value=up.external_emojis)
        emb.add_field(name="Can Connect to VCs",value=up.connect)
        emb.add_field(name="Can Speak in VCs",value=up.speak)
        emb.add_field(name="Can Mute Members",value=up.mute_members)
        emb.add_field(name="Can Deafen Members",value=up.deafen_members)
        emb.add_field(name="Can Move Members",value=up.mute_members)
        emb.add_field(name="Can Change Nickname",value=up.change_nickname)
        emb.add_field(name="Can Manage Nicknames",value=up.manage_nicknames)
        emb.add_field(name="Can Manage Roles",value=up.manage_roles)
        emb.add_field(name="Can Manage Webhooks",value=up.manage_webhooks)
        emb.add_field(name="Can Manage Emojis",value=up.manage_emojis)
        await ctx.send(embed=em)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Utils(bot))
