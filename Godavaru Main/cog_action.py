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
# import js2py

class Action():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def cuddle(self, ctx):
        """For when you just need to cuddle someone uwu

        **Usage:** `g_cuddle <user(s)>`

        **Permission:** User"""
        img = ["./images/cuddlea.gif", "./images/cuddleb.gif", "./images/cuddlec.gif", "./images/cuddled.gif", "./images/cuddlee.gif", "./images/cuddlef.gif", "./images/cuddleg.gif", "./images/cuddleh.gif", "./images/cuddlei.gif", "./images/cuddlej.gif"]
        var = int(random.random() * len(img))
        
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = '<:godavarublobhug:318227863646109696> Aww, are you lonely? I\'ll cuddle with you, **'+ctx.message.author.display_name+'**!'
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            if len(ctx.message.mentions) == 1:
                pr = "was"
            else:
                pr = "were"
            msg = '<:godavarublobhug:318227863646109696> **' + ments + '** '+pr+' cuddled by **' + ctx.message.author.display_name +'**!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def hug(self, ctx):
        """Give a person a big fat hug! Awww!

        **Usage:** `g_hug <user(s)>`

        **Permission:** User"""
        img = ["./images/huga.gif", "./images/hugb.gif", "./images/hugc.gif", "./images/hugd.gif", "./images/huge.gif", "./images/hugf.gif", "./images/hugg.gif", "./images/hugh.gif", "./images/hugi.gif", "./images/hugj.gif"]
        var = int(random.random() * len(img))
        
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = ':hugging: Aww, are you lonely? I\'ll cuddle with you, **'+ctx.message.author.display_name+'**!'
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            if len(ctx.message.mentions) == 1:
                pr = "was"
            else:
                pr = "were"
            msg = ':hugging: **' + ments + '** '+pr+' hugged by **' + ctx.message.author.display_name +'**!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def slap(self, ctx):
        """What the hell did you just say to me? I'm gonna slap you to the moon for that comment!

        **Usage:** `g_slap <user(s)>`

        **Permission:** User"""
        img = ["./images/slapa.gif", "./images/slapb.gif", "./images/slapc.gif", "./images/slapd.gif", "./images/slape.gif", "./images/slapf.gif", "./images/slapg.gif", "./images/slaph.gif", "./images/slapi.gif"]
        var = int(random.random() * len(img))

        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = ':raised_hand: This makes no sense... Oh well'
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            msg = ':raised_hand: Hyaah! **' + ctx.message.author.display_name + '** has slapped **' + ments + '**!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def kiss(self, ctx):
        """Give that special someone a kiss! <3

        **Usage:** `g_kiss <user(s)>`

        **Permission:** User"""
        img = ["./images/kissa.gif", "./images/kissb.gif", "./images/kissc.gif", "./images/kissd.gif", "./images/kisse.gif", "./images/kissf.gif", "./images/kissg.gif", "./images/kissh.gif", "./images/kissi.gif", "./images/kissj.gif", "./images/kissk.gif"]
        var = int(random.random() * len(img))

        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = ":kissing_heart: I don't think you can kiss yourself... I'll kiss you instead!"
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            
            if len(ctx.message.mentions) == 1:
                pr = "was"
            else:
                pr = "were"
            msg = ':kissing_heart: **' + ments + '** ' + pr + ' kissed by **' + ctx.message.author.display_name +'**!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug
            
    @commands.command(pass_context = True)
    async def pat(self, ctx):
        """Send a pat over to a person or a few people. Sometimes a pat speaks words that words cannot.
        Or maybe I just really like pats so I endorse them. Whichever one it is.

        **Usage:** `g_pat <user(s)>`

        **Permission:** User"""
        img = ["./images/pata.gif", "./images/patb.gif", "./images/patc.gif", "./images/patd.gif", "./images/pate.gif", "./images/patf.gif", "./images/patg.gif", "./images/path.gif", "./images/pati.gif", "./images/patj.gif", "./images/patk.gif"]
        var = int(random.random() * len(img))
            
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            if len(ctx.message.mentions) == 1:
                pr = "was"
            else:
                pr = "were"
            msg = '<:patemote:318592885090156544> **' + ments + '** ' + pr + ' pat by **' + ctx.message.author.display_name + '**!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def poke(self, ctx):
        """Do you ever have a friend who just wont stop ignoring you? Just poke them. :eyes:

        **Usage:** `g_poke <user(s)>`

        **Permission:** User"""
        img = ["./images/pokea.gif", "./images/pokeb.gif", "./images/pokec.gif", "./images/poked.gif", "./images/pokee.gif", "./images/pokef.gif", "./images/pokeg.gif", "./images/pokeh.gif", "./images/pokei.gif", "./images/pokej.gif"]
        var = int(random.random() * len(img))

        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = ":eyes: You can't poke nothing! I'll poke you instead!"
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            if len(ctx.message.mentions) == 1:
                pr = "was"
            else:
                pr = "were"
            msg = ':eyes: **' + ments + '** ' + pr + ' poked by **' + ctx.message.author.display_name +'**!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def wakeup(self, ctx):
        """A way to get your friends off of their lazy butts and wake up.

        **Usage:** `g_wakeup <user(s)>`

        **Permission:** User"""
        img = ["./images/wakeupa.gif", "./images/wakeupb.gif", "./images/wakeupc.gif", "./images/wakeupd.gif", "./images/wakeupe.gif", "./images/wakeupf.gif", "./images/wakeupg.gif", "./images/wakeuph.gif"]
        var = int(random.random() * len(img))

        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = '<:morning:319631823766552597> What are you trying to wake up? Well, you do you I guess.'
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            msg = '<:morning:319631823766552597> **' + ments + '**, rise and shine! **' + ctx.message.author.display_name + '** wants you to wake up!'
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context=True)
    async def sleep(self, ctx):
        """The literal opposite of wakeup. This is also based off of my best friend, Kitty#4867, who would always tell me to go to bed. Love ya, Kat! ~Desii

        **Usage:** `g_sleep <user(s)>`

        **Permission:** User"""
        img = ["./images/sleepa.gif", "./images/sleepb.gif", "./images/sleepc.gif", "./images/sleepd.gif", "./images/sleepe.gif", "./images/sleepf.gif", "./images/sleepg.gif", "./images/sleeph.gif", "./images/sleepi.gif", "./images/sleepj.gif", "./images/sleepk.gif", "./images/sleepl.gif"]
        var = int(random.random() * len(img))
        
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = "<:night:319631860512587776> Hmm. Telling yourself to sleep. Self-discipline. I like it. Go slep!1!!"
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            msg = "<:night:319631860512587776> **"+ctx.message.author.display_name+"** is telling **"+ments+"** to go to sleep!"
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context=True)
    async def cry(self, ctx):
        """When life gets at you and you just wanna let it all out.

        **Usage:** `g_cry [user(s)]`

        **Permission:** User"""
        img = ["./images/crya.gif", "./images/cryb.gif", "./images/cryc.gif", "./images/cryd.gif", "./images/crye.gif", "./images/cryf.gif", "./images/cryg.gif", "./images/cryh.gif", "./images/cryi.gif", "./images/cryj.gif", "./images/cryk.gif"]
        var = int(random.random() * len(img))
        
        if len(ctx.message.mentions) == 0:
            msg = ":cry: **"+ctx.message.author.display_name+"** just started to cry!"
            await ctx.send(file=discord.File(img[var]), content=msg) # desii do not touch this command again
        elif len(ctx.message.mentions) > 0:
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = ":cry: **"+ctx.message.author.display_name+"** just started to cry!"
                    await ctx.send(file=discord.File(img[var]), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            else:
                msg = ":cry: **"+ments+"** just made **"+ctx.message.author.display_name+"** cry!"
            await ctx.send(file=discord.File(img[var]), content=msg)
        else:
            await ctx.send("An unexpected error occurred.") # i mean it
        
    @commands.command(pass_context=True)
    async def kill(self, ctx):
        """Attempt to kill people. Has a chance of failing. Also, you may only kill one user at a time, so this command does not (and will never) have multi mention support.

        **Usage:** `g_kill <user>`

        **Permission:** User"""
        killmsg = ["**"+ctx.message.mentions[0].display_name+"** was stabbed by **"+ctx.message.author.display_name+"**", "You tried to kill **"+ctx.message.mentions[0].display_name+"**, but you got caught by the police :<", "**"+ctx.message.mentions[0].display_name+"** disintegrated.", "While trying to kill **"+ctx.message.mentions[0].display_name+"**, **"+ctx.message.author.display_name+"** accidentally killed themselves.", "**"+ctx.message.mentions[0].display_name+"** drowned.", "Hahahaha nice try. You just tried to kill a cop. You're in jail now.", "While trying to kill **"+ctx.message.mentions[0].display_name+"**, you accidentally pinged b1nzy. Ouch.", "You pushed **"+ctx.message.mentions[0].display_name+"** into a river with crocodiles.", "You made **"+ctx.message.mentions[0].display_name+"** listen to KidzBop, so they bled out of their ears and died.", "Meh. I don't feel like helping a murder today. Try again.", "**"+ctx.message.mentions[0].display_name+"** was thrown into a pit of snakes.", "**"+ctx.message.author.display_name+"** threw **"+ctx.message.mentions[0].display_name+"** into a pit of snakes, but fell in as well.", "**"+ctx.message.mentions[0].display_name+"** was given the death sentence after **"+ctx.message.author.display_name+"** framed them for murder.", "**"+ctx.message.mentions[0].display_name+"** was forced to use Kotlin by **"+ctx.message.author.display_name+"**, so they died.", "**"+ctx.message.author.display_name+"** tried to kill someone, but found their way into Mantaro Hub and gave into the memes.", "**"+ctx.message.mentions[0].display_name+"** was killed by a sentient robot... Why are you looking at me? I didn't do it...", "**"+ctx.message.author.display_name+"** tried to kill someone and got away from the police. However, the FBI jailed them.", "You don't have a weapon. Oops. Was I supposed to bring it? I think I was...", "When **"+ctx.message.author.display_name+"** tried to kill **"+ctx.message.mentions[0].display_name+"**, they were disappointed to find they were already dead.", "**"+ctx.message.mentions[0].display_name+"** took an arrow to the knee! Well, actually it was a gunshot. And it was actually to the heart."]
        var = int(random.random() * len(killmsg))
        
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                await ctx.send("Don't kill yourself! I love you!")
            elif ctx.message.mentions[0].id == ctx.message.guild.me.id:
                await ctx.send("You tried to kill me, but you realised I'm a bot. So I killed you instead.")
            else:
                await ctx.send(killmsg[var])
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def shrug(self, ctx):
        """When you have no idea what is going on.

        **Usage: `g_shrug`

        **Permission:** User"""
        embed = discord.Embed(title='Welp', description='*shrugs*', color=ctx.message.author.color).set_image(url='https://i.imgur.com/TPyz6lH.gif')
        await ctx.send(content=None, embed=embed)

    @commands.command()
    async def fuck(self, ctx):
        """Feeling lewd? Why don't you go and fuck a person :eyes:
        Note: This command does include NSFW content, meaning it can only be used in NSFW marked channels. For a reference on how to set channels as NSFW, [here is a general idea of where the button usually is.](https://i.imgur.com/ZisyibJ.png)

        **Usage:** `g_fuck <user(s)>`

        **Permission:** User"""
        gifs = ["http://x.imagefapusercontent.com/u/TrickyLouse/3985842/42565623/Slow-Fuck-Hentai-GIF-TheHentaiWorld-6.gif",
                "http://www.hentairider.com/media/images/5/hentai-fuck-images/hentai-fuck-images-134125.gif",
                "https://media.tenor.com/images/965a2bf373b32091041e901ef0f247cb/tenor.gif",
                "https://s.smutty.com/media_smutty/e/v/i/l/b/evilbaroness-z9hrj-a6a24c.gif",
                "https://ii.yuki.la/1/10/86f3aec8549511d0ec67dceef1d8c8124e0e7f50bb442d70bed825cf1d1ff101.gif",
                "https://danbooru.donmai.us/data/__kanaya_azami_ukagaka_drawn_by_zee_zee_sub__b9442481a2d7fd6dcf3c74280822237e.gif",
                "https://danbooru.donmai.us/data/__little_boy_admiral_and_ooi_kantai_collection_drawn_by_hangaku__8e81bf57306a4fdf326da4214ef3aa35.gif",
                "https://danbooru.donmai.us/data/__admiral_and_murakumo_kantai_collection_drawn_by_hangaku__7e555705d880142de82bbac193ebc73d.gif",
                "https://danbooru.donmai.us/data/__okumura_haru_persona_and_persona_5_drawn_by_bard_bot__21850b2448462ce7d9a544c02a4ba7f3.gif",
                "https://danbooru.donmai.us/data/__hagikaze_kantai_collection_drawn_by_hangaku__e621e283aab8a39da57b6629779525c4.gif",
                "https://danbooru.donmai.us/data/__stocking_panty_stocking_with_garterbelt_drawn_by_phanpix__b5506ab4ddf63686df9492bd9cf79400.gif",
                "https://simg3.gelbooru.com/images/3a/1e/3a1e7fc0b758814be7363813588cc3aa.gif",
                "https://danbooru.donmai.us/data/__2627973__dae809c5f38fcfe532ef8f798eacae63.gif",
                "https://danbooru.donmai.us/data/__hikigaya_hachiman_yahari_ore_no_seishun_lovecome_wa_machigatteiru_drawn_by_cr_r__3275c23d93b7c6e48fd87cff297b03eb.jpg"]
        v = int(random.random() * len(gifs))
        args = ctx.message.content
        if ctx.message.channel.is_nsfw() == False:
            await ctx.send(":x: Y-you lewdie! Go get a room!")
        else:
            if len(ctx.message.mentions) == 0:
                await ctx.send(":x: You can't fuck the air... well, you can try.")
            else:
                ments = ""
                for x in range(0, len(ctx.message.mentions)):
                    if ctx.message.mentions[x].id == ctx.message.author.id:
                        await ctx.send(":x: I know people get lonely, but jeez...")
                        return
                    if x == 0:
                        ments = ctx.message.mentions[x].display_name
                    elif x == len(ctx.message.mentions) - 1:
                        if len(ctx.message.mentions) == 2:
                            ments = ments+" and "+ctx.message.mentions[x].display_name
                        else:
                            ments = ments+", and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", "+ctx.message.mentions[x].display_name
                em = discord.Embed(description=":eggplant: **{0}** just fucked **{1}**!".format(ctx.message.author.display_name, ments),color=ctx.message.author.color)
                em.set_image(url=gifs[v])
                em.set_footer(text="You lewdie o.o")
                await ctx.send(embed=em)

        
def setup(bot):
    bot.add_cog(Action(bot))
