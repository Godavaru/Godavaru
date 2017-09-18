import os
from discord.ext import commands
import datetime, re
import json
import discord
import asyncio
import random
import time
import platform
import datetime
import inspect
import requests
import pytz

class Utils():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,name="time")
    async def _time(self, ctx):
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
                await self.bot.say("The time in **{0}** is {1}".format(args[1], datetime.datetime.now(tz).strftime("`%H:%M:%S` on `%d-%b-%Y`")))
            except pytz.UnknownTimeZoneError:
                await self.bot.say('Couldn\'t find that timezone, make sure to use one from this list: https://pastebin.com/B5tLQdEY\nAlso remember that timezones are case sensitive.')
        else:
            await self.bot.say(":x: Usage: `{}time <timezone>`".format(self.bot.command_prefix[0]))

    @commands.command(pass_context=True,name="embed")
    async def _embed(self, ctx):
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
            await self.bot.say(embed=em)
        else:
            await self.bot.say(":x: You need at least one argument, split with `|` (guide coming soon)")

    @commands.command(pass_context=True)
    async def banlist(self, ctx):
        banned = await self.bot.get_bans(ctx.message.server)
        msg = "**All Banned Users** -- ({})\n".format(len(banned))
        for user in sorted(banned, key=lambda x: x.name):
            msg = msg+"`"+str(user)+"`\n"
        await self.bot.say(msg)

    @commands.command(pass_context=True,aliases=["ud"])
    async def urban(self, ctx):
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
                await self.bot.say(":x: No results for `{}`.".format(word))
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
                        await self.bot.say(":x: There are no more definitions. Try with a lower number.")
                        return
                elif num < -1:
                    await self.bot.say(":x: Nice try, don't search for negative numbers.")
                    return
                elif num == -1:
                    await self.bot.say(":x: Nice try, don't search for the 0th definition.")
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
                    await self.bot.send_message(ctx.message.channel, embed=em)
                except Exception as e:
                    await self.bot.say("`ERROR` ```py\n{}```".format(type(e).__name__+": "+str(e)))
        else:
            await self.bot.say("Search for a word!")


    @commands.command(pass_context=True,aliases=["length"])
    async def len(self, ctx):
        umsg = ctx.message.content
        args = umsg.split(' ')
        toLen = umsg.replace(args[0], "")
        toLen = toLen[1:]
        if toLen == "":
            await self.bot.say(":x: Specify a message that I can find the length of.")
            return
        await self.bot.say(":white_check_mark: The message you gave me is `{}` characters long.".format(len(toLen)))


    @commands.command(pass_context=True, aliases=["nekos"])
    async def catgirls(self, ctx):
        args = ctx.message.content
        args = args.split(' ')
        if len(args) > 1:
            if args[1] == "nsfw":
                if ctx.message.channel.name.startswith('nsfw'):
                    r = requests.get('http://catgirls.brussell98.tk/api/nsfw/random')
                    js = r.json()
                    img = js['url']
                else:
                    await self.bot.say(":x: Can't send lewd/questionable images in a non-nsfw channel. (if this is an nsfw channel, make sure it has `nsfw` at the front.)")
                    return
            else:
                r = requests.get('http://catgirls.brussell98.tk/api/random')
                js = r.json()
                img = js['url']
        else:
            r = requests.get('http://catgirls.brussell98.tk/api/random')
            js = r.json()
            img = js['url']
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        em = discord.Embed(color=colours[col])
        em.set_image(url=img)
        await self.bot.send_message(ctx.message.channel, embed=em)


    @commands.command(pass_context=True, name="8ball",aliases=["mb", "magicball"])
    async def _8ball(self, ctx):
        umsg = ctx.message.content
        omsg = umsg.split(' ')
        args = umsg.replace(omsg[0], "")
        args = args[1:]
        if args != "":
            r = requests.get('https://8ball.delegator.com/magic/JSON/'+args)
            js = r.json()
            answer = js['magic']['answer']
            await self.bot.say(":crystal_ball: {}.".format(answer))
        else:
            await self.bot.say(":x: Specify a question.")


    @commands.command(pass_context=True)
    async def cat(self, ctx):
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        content = [";w; Don't be sad, here's a cat!", "You seem lonely, {0.mention}. Here, have a cat".format(ctx.message.author), "Meeeooowwww!", "Awww, so cute! Look at the kitty!!1!", "Woof... wait wrong animal."]
        con = int(random.random() * len(content))
        r = requests.get('http://random.cat/meow')
        js = r.json()
        em = discord.Embed(color=colours[col])
        em.set_image(url=js['file'])
        await self.bot.send_message(ctx.message.channel, content=content[con], embed=em)


    @commands.command(pass_context=True)
    async def dog(self, ctx):
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
        await self.bot.send_message(ctx.message.channel, content=content[con], embed=em)

def setup(bot):
    bot.add_cog(Utils(bot))
