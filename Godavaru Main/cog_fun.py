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
class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def say(self, ctx):
        """Make me say something.
        You can also use me to edit a message and you can use the silentsay variable as well.

        **Usage:** `g_say [flag] <arguments>`
            If you use `--s` as a flag, your arguments are simply what you want the bot to say and have it remove your message afterwards.
            If you use `--e` as a flag, the arguments are the message id you want to edit and the new content.
            If no flag is passed, the bot will simply send the message like normal excluding the actual command.

        **Permission:** User"""
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix[0]+"say", "")
        args = args.replace(self.bot.command_prefix[1]+"say", "")
        args = args.replace("@everyone", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        args = args.replace("@here", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        args = args[1:]
        if args == "":
            await ctx.send("I can't send an empty message!")
        elif args.startswith("--s"):
            if args == "--s": # --s == silentsay
                await ctx.send("You can't silently send an empty message!")
            else:
                args = args[4:]
                await ctx.send(str(args))
                await ctx.message.delete()
        elif args.startswith("--e"):
            if args == "--e": # --e == edit
                await ctx.send("You can't edit nothingness.")
            try:
                args = args[4:]
                mid = args.split(' ')
                toEdit = await ctx.message.channel.get_message(int(mid[0])) 
                content = args.replace(mid[0]+" ", "")
                await toEdit.edit(content=content)
                await ctx.message.delete()
            except discord.NotFound:
                notFound = await ctx.send("Couldn't find the message.")
                await asyncio.sleep(5)
                await notFound.delete()
                await ctx.message.delete()
            except (IndexError, ValueError):
                indxErr = await ctx.send("Usage: `g_say --e <id> <content>`")
                await asyncio.sleep(5)
                await indxErr.delete()
                await ctx.message.delete()
        else:
            await ctx.send(str(args))

    @commands.command(pass_context = True)
    async def year(self, ctx):
        """The very first command that was ever added.
        It's nothing special, but it's a nice lil joke :eyes:

        **Usage:** `g_year [member]`

        **Permission:** User"""
        if len(ctx.message.mentions) > 0:
            u = ctx.message.mentions[0]
        else:
            u = ctx.message.author
        await ctx.send("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send **"+str(u)+"** nudes :3")

    @commands.command(pass_context = True)
    async def f(self, ctx):
        """Pay your respects.

        **Usage:** `g_f`

        **Permission:** User"""
        embed = discord.Embed(title='Press F to pay respects!',description='**' + ctx.message.author.display_name + '** has paid their respects successfully :eggplant:',color=ctx.message.author.color).set_footer(text='f')
        await ctx.send(content=None, embed=embed)

        
    # If you're looking for the code for 8ball, it was moved to cog_utils


    @commands.command(pass_context=True)
    async def slots(self, ctx):
        """Roll the slot machine and try your luck.

        **Usage:** `g_slots`

        **Permission:** User"""
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
            await ctx.send("{0}\n\n{1}{2}{3}\n{4}{5}{6} :arrow_left:\n{7}{8}{9}".format(msg, col[var1], col[var2], col[var3], col[var4], col[var5], col[var6], col[var7], col[var8], col[var9]))
        except Exception as e:
            await ctx.send(":x: `ERROR` ```py\n{}```".format(type(e).__name__ + ': ' + str(e)))


    @commands.command()
    async def bowling(self, ctx):
        """Play a game of bowling!

        **Usage:** `g_bowling`

        **Permission:** User"""
        init = int(random.random() * 10) + 1
        if (init == 10):
            await ctx.send(":bowling: It's a strike! You hit all the pins on your first try.")
            return
        else:
            await ctx.send(":bowling: You knocked down `{}` pins. Let's try to knock the other `{}` down.".format(init, 10 - init))
            finisher = int(random.random() * (10 - init)) + 1
            if (finisher + init >= 10):
                await ctx.send(":bowling: You won! You knocked down all pins on the second try.")
            else:
                await ctx.send(":bowling: You didn't win, but you tried and knocked down `{}/10` in the meantime.".format(finisher + init))

    @commands.command(aliases=["number"])
    async def numbers(self, ctx):
        """Get a random fact about a number or specify a number to get a fact about it.

        **Usage:** `g_numbers [number]`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(args) > 1:
            try:
                num = int(args[1])
            except:
                num = int(random.random() * 2000)+1
        else:
            num = int(random.random() * 2000)+1
        if num > 100:
            types = ["math", "year"]
        else:
            types = ["trivia", "math", "date", "year"]
        x = requests.get("http://numbersapi.com/{}/{}".format(num, types[int(random.random() * len(types))]))
        await ctx.send(":mega: {}".format(x.text))

    @commands.command(pass_context = True)
    async def love(self, ctx):
        """Determine the love between you and that special someone :eyes:
        Note that user does not have to even be a user, it can also just be a word.

        **Usage:** `g_love <user>`

        **Permission:** User"""
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
            elif ctx.message.mentions[0].id == 311810096336470017 and ctx.message.author.id == 267207628965281792:
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**-9000%**\n`Pure hatred. They absolutely hate eachother.`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            elif ctx.message.mentions[0].id == 132584525296435200 and ctx.message.author.id == 267207628965281792:
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**9000%**\n`There is no love that is stronger!`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            elif ctx.message.mentions[0].id == 267207628965281792 and ctx.message.author.id == 132584525296435200:
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**9000%**\n`There is no love that is stronger!`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
            else:
                embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + ctx.message.mentions[0].display_name + "`",color=ctx.message.author.color).add_field(name="Result",value="**" + str(var) + "%**\n`" + str(msg) + "`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
        else:
            content=None
            embed = discord.Embed(title=":two_hearts: Love meter :two_hearts:",description="<:in_love_heart:335217899885297664> `" + ctx.message.author.display_name + "`\n<:in_love_heart:335217899885297664> `" + msg1 + "`",color=ctx.message.author.color).add_field(name="Result",value="**" + str(var) + "%**\n`" + str(msg) + "`").set_footer(text="Requested by " + ctx.message.author.display_name).set_thumbnail(url="http://i.imgur.com/ND0m992.png")
        await ctx.send(content=content, embed=embed)

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        """Flip people! Because flipping them off is not enough.

        **Usage:** `g_flip <user>`

        **Permission:** User"""
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
            await ctx.send(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await ctx.send("Who do you want me to flip? :thinking:")

    @commands.command(pass_context=True)
    async def roll(self, ctx):
        """Roll a generic six-sided die.

        **Usage:** `g_roll`

        **Permission:** User"""
        var = int(random.random() * 6)
        await ctx.send(":game_die: You rolled a **{}**!".format(var+1))

    @commands.command(pass_context=True)
    async def rps(self, ctx):
        """Play a game of rock paper scissors against the bot.
        The choice parameter should be either rock, paper, or scissors, case insensitive.

        **Usage:** `g_rps <choice>

        **Permission:** User"""
        umsg = ctx.message.content.lower()
        args = umsg.split(' ')
        args = umsg.replace(args[0], "")
        args = args[1:]
        var = int(random.random() * 3)
        if args == "paper" or args == "rock" or args == "scissors":
            if (var == 0):
                if args == "paper":
                    await ctx.send(":moyai: You win!")
                elif args == "rock":
                    await ctx.send(":moyai: It's a draw!")
                elif args == "scissors":
                    await ctx.send(":moyai: You lose!")
            elif (var == 1):
                if args == "paper":
                    await ctx.send(":newspaper: It's a draw!")
                elif args == "rock":
                    await ctx.send(":newspaper: You lose!")
                elif args == "scissors":
                    await ctx.send(":newspaper: You win!")
            elif (var == 2):
                if args == "paper":
                    await ctx.send(":scissors: You lose!")
                elif args == "rock":
                    await ctx.send(":scissors: You win!")
                elif args == "scissors":
                    await ctx.send(":scissors: It's a draw!")
        else:
            await ctx.send(":x: You must specify either rock, paper, or scissors!")

    @commands.command(pass_context = True)
    async def lenny(self, ctx):
        """Make a lenny face.
        Note that this deletes the invoker's message.

        **Usage:** `g_lenny [message]`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        msg = umsg.replace(args[0], "")
        await ctx.send(str(msg)+"( ͡° ͜ʖ ͡°)")
        await ctx.message.delete()

    @commands.command(pass_context = True)
    async def nonowa(self, ctx):
        """Make a nonowa face.
        Note that this deletes the invoker's message.

        **Usage:** `g_nonowa [message]`

        **Permission:** User"""
        umsg = ctx.message.content
        args = umsg.split(' ')
        msg = umsg.replace(args[0], "")
        await ctx.send(str(msg)+"のワの")
        await ctx.message.delete()

    @commands.command(aliases=["nc"])
    async def nightcore(self, ctx):
        """Get a random nightcore song.

        **Usage:** `g_nightcore`

        **Permission:** User"""
        r = requests.get('https://api.apithis.net/nightcore.php')
        song = r.text
        await ctx.send(song)

    @commands.command()
    async def trivia(self, ctx):
        """Play a game of trivia!
        Note that some answers may be bugged out, there will be an alternative answering system soon:tm:

        **Usage:** `g_trivia [difficulty]`

        **Permission:** User"""
        link = 'https://opentdb.com/api.php?amount=1'
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(args) > 1:
            if args[1].lower() in ["easy", "medium", "hard"]:
                link = link+"&difficulty="+args[1].lower()
        r = requests.get(link)
        js = r.json()
        cat = js['results'][0]['category']
        dif = js['results'][0]['difficulty']
        que = js['results'][0]['question']
        que = que.replace('&quot;','"')
        que = que.replace('&ldquo;', "")
        que = que.replace('&#039;', "'")
        que = que.replace('&Aring;', 'Å')
        que = que.replace('&eacute;', 'é')
        inc = js['results'][0]['incorrect_answers']
        a = [js['results'][0]['correct_answer']]
        for i in range(0, len(inc)):
            a += [inc[i]]
        an = ""
        answ = sorted(a, key=str.lower)
        for ans in answ:
            an += ans+"\n"
        await ctx.send("**Trivia Question**\n"
                       +"**Category:** {}\n".format(cat)
                       +"**Difficulty:** {}\n".format(dif)
                       +"**Question:** {}\n\n".format(que)
                       +str(an))
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        try:
            msg = await self.bot.wait_for('message', check=check, timeout=120.0)
        except asyncio.TimeoutError:
            await ctx.send("**{}**: You ran out of time!".format(ctx.message.author.name))
            return
        if msg.content.lower() != "end":
            if msg.content.lower() == str(js['results'][0]['correct_answer']).lower():
                await ctx.send("**{}**: You won! ".format(ctx.message.author.name))
            else:
                v = "**{}**: You lost! ".format(ctx.message.author.name)
                if len(inc) > 1:
                    v = v+"You have one more try!"
                else:
                    v = v+"Correct answer was `{}`".format(js['results'][0]['correct_answer'])
                await ctx.send(v)
                if len(inc) > 1:
                    try:
                        msg2 = await self.bot.wait_for('message',check=check, timeout=120.0)
                    except asyncio.TimeoutError:
                        await ctx.send("**{}**: You ran out of time!".format(ctx.message.author.name))
                        return
                    if msg2.content.lower() != "end":
                        if msg2.content.lower() == str(js['results'][0]['correct_answer']).lower():
                            await ctx.send("**{}**: You won! ".format(ctx.message.author.name))
                        else:
                            v = "**{}**: You lost! Correct answer was `{}`".format(ctx.message.author.name, js['results'][0]['correct_answer'])
                            await ctx.send(v)
                    else:
                        await ctx.send("**{}**: Ended your game. Correct answer was `{}`".format(ctx.message.author.name, js['results'][0]['correct_answer']))
        else:
            await ctx.send("**{}**: Ended your game. Correct answer was `{}`".format(ctx.message.author.name, js['results'][0]['correct_answer']))

    @commands.command()
    async def joke(self, ctx):
        """Make a somewhat Chuck Norris related joke.

        **Usage:** `g_joke [word or phrase]`

        **Permission:** User"""
        r = requests.get('http://api.icndb.com/jokes/random')
        js = r.json()
        j = str(js['value']['joke'])
        a = ctx.message.content
        b = a.split(' ')
        p = a.replace(b[0], "")
        p = p[1:]
        if p == "":
            p = ctx.message.author.mention
        j = j.replace("Chuck Norris", p)
        j = j.replace("Chuck", p)
        j = j.replace('&quot;', "\"")
        await ctx.send(j)

    @commands.command()
    async def ttb(self, ctx):
        """Use the text to brick feature.

        **Usage:** `g_ttb <text>`

        **Permission:** User"""
        umsg = ctx.message.clean_content.lower()
        args = umsg.split(' ')
        l = "abcdefghijklmnopqrstuvwxyz"
        if len(args) > 1:
            m = umsg.replace(args[0]+" ", "")
            msg = ""
            for x in range(0, len(m)):
                if m[x:x+1] in l:
                    msg += ":regional_indicator_{}:".format(m[x:x+1])
                else:
                    msg += m[x:x+1]
            msg1 = msg.replace("#", ":hash:")
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
        else:
            await ctx.send("Specify words to brickify.")
			
def setup(bot):
    bot.add_cog(Fun(bot))
