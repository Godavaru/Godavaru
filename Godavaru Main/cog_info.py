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

abtDesc = """
**H-hello!~~**
My name is Godavaru, but you can call me Godava, as many people do. I was named after a community guild, which I am not directly linked to anymore, but you may check out if you wish using the link [here](https://discord.gg/bxDV2yu)! I-I mean, It's not like I want you to join or anything... baka!
Below, you can find a link to the actual support guild for me, where you may tell my mom if I misbehave and throw errors around again. :< Below, you can also find a link to invite me, if you so wish! I promise that I will do you good!
I have quite a few features; I can list them for you now!

**__I come with:__**
-> Action Commands (hug, kiss, even some lewd ones :eyes:)
-> Moderation Commands (ban, kick, prune, and more!)
-> Utility Commands (urbandictionary search, normal dictionary, complex maths, and much more!)
-> Fun Commands (slots, trivia, and other miscellanious features to keep you occupied!)
-> Information Commands (userid lookup, discriminator lookup, role information, and more!)

Check all my commands with `g_help`!
"""

ownerids = [
    267207628965281792,
    99965250052300800,
    170991374445969408,
    188663897279037440
]
helperids = [
    267207628965281792,
    99965250052300800,
    170991374445969408,
    188663897279037440
]
donatorids = [
]
creditedids = [
    267207628965281792,
    99965250052300800,
    170991374445969408,
    188663897279037440,
    132584525296435200,
    155867458203287552,
    213466096718708737
]


class Info():
    def __init__(self, bot):
        self.bot = bot
        #self.webhook_class = Webhook(bot)
        #self.request_webhook = self.webhook_class.request_webhook

    @commands.command(pass_context=True)
    async def roleinfo(self, ctx):
        """Get information on a role.
        Note that the role name is case sensitive. If the role name is `Member`, then you must pass the role argument as `Member` and not `member`.

        **Usage:** `g_roleinfo <role>`

        **Permission:** User"""
        try:
            msg = ctx.message.content
            a = msg.split(' ')
            role = msg.replace(a[0], "")
            role = role[1:]
            if role == "":
                await ctx.send(":x: Specify a role to get.")
                return
            getId = discord.utils.get(ctx.message.guild.roles, name=str(role))
            em = discord.Embed(title="Role Info", description="Information for role **{}**".format(getId.name),color=getId.color)
            em.add_field(name="Permissions",value=getId.permissions.value, inline=True)
            em.add_field(name="Colour",value=getId.colour,inline=True)
            em.add_field(name="Managed",value=getId.managed, inline=True)
            em.add_field(name="Hoisted",value=getId.hoist,inline=True)
            em.add_field(name="Role ID",value=getId.id,inline=True)
            em.add_field(name="Position",value=getId.position,inline=True)
            em.add_field(name="Mentionable",value=getId.mentionable,inline=True)
            em.add_field(name="Creation Date",value=getId.created_at.strftime('%a %d %b %Y at %H:%M:%S'),inline=True)
            em.set_thumbnail(url="https://i.imgur.com/La0f2NY.png")
            await ctx.send(embed=em)
        except (discord.NotFound, AttributeError):
            await ctx.send(":x: I couldn't find that role. Make sure it has capitals in the proper place, as this is case-sensitive.")
            
        
    @commands.command(pass_context = True)
    async def about(self, ctx):
        """Show the stuff about me! I promise I'm interesting uwu

        **Usage:** `g_about [credits]`

        **Permission:** User"""
        args = ctx.message.content
        args = args.split(' ')
        member_count = 0
        server_count = len(self.bot.guilds)
        for server in self.bot.guilds:
            for member in server.members:
                member_count += 1
        abtEm = discord.Embed(title='About Godavaru!', description=abtDesc, color=0x9B59B6)
        abtEm.add_field(name='Version Number', value='{}'.format(self.bot.version), inline=False)
        abtEm.add_field(name='Servers', value=str(server_count))
        abtEm.add_field(name='Users',value=str(member_count) + '\n\n[Invite me](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)\n[Patreon page](https://www.patreon.com/godavaru)', inline=False).set_footer(text="Made with love <3 | Check out g_about credits for special credits.").set_thumbnail(url="https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png")
        try:
            if args[1] == "credits":
                embed = discord.Embed(title="Special Recognition",description=""
                                      +"**Primary Developer:** Desiree#3658\n"
                                      +"**Developers:** Yuvira#7655, AttributeError#2513, and Jonas B.#9089\n"
                                      +"**Sensei:** Yuvira#7655\n"
                                      +"**Emotional Support & Boyfriend:** MrLar#8117\n"
                                      +"**Inspiration:** Kodehawa#3457 (`and MantaroBot, if it wasn't for that project I probably would never have tried to make a bot`)\n\n"
                                      +"And thanks to everyone who has used the bot. Much love <3",
                                      color=0x1abc9c)
            else:
                embed = abtEm
        except IndexError:
            embed = abtEm
        await ctx.send(content=None, embed=embed)


    @commands.command(pass_context = True)
    async def invite(self, ctx):
        """Get some important links about me.

        **Usage:** `g_invite`

        **Permission:** User"""
        embed = discord.Embed(description='Here are some useful links for the Godavaru bot. If you have any questions at all, feel free to join the support guild and tag Desiree#3658 with your questions!\nBelow you can also find the links to the support guild itself and the Patreon URL. Thanks for using the bot!', color=0x9B59B6).set_author(name='Useful Links for Godavaru!', icon_url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Invite URL', value='http://polr.me/godavaru').add_field(name='Support Guild', value='https://discord.gg/ewvvKHM').add_field(name="Patreon URL", value='https://patreon.com/godavaru').add_field(name="Github", value="https://github.com/Desiiii/Godavaru")
        await ctx.send(content=None, embed=embed)


    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Check my response time and my websocket ping

        **Usage:** `g_ping`

        **Permission:** User"""
        console = self.bot.get_channel(316688736089800715)
        before = datetime.datetime.utcnow()
        ping_msg = await console.send(":mega: **Pinging...**")
        ping = (datetime.datetime.utcnow() - before) * 1000
        before2 = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping2 = (after - before2) * 1000
        var = int(random.random() * 5)
        v = ["a", "e", "i", "o", "u"]
        await ping_msg.edit(content=':warning: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] `' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` checked my ping in the channel `' + ctx.message.channel.name + '` in the server `' + ctx.message.guild.name + '`. The result was {:.2f}ms'.format(ping.total_seconds())+" with a websocket ping of {0:.0f}ms".format(ping2))
        await ctx.send(":mega: P"+v[var]+"ng! The message took **{:.0f}ms**!".format(ping.total_seconds())+" `Websocket: {0:.0f}ms` :thinking:".format(ping2))


    def get_bot_uptime(self, *, brief=False):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)
    

    @commands.command(pass_context = True)
    async def info(self, ctx):
        """Show some of the more statistical information about me.
        This information includes the current version(s), number of commands, amount of servers, channels, users, uptime, and average websocket ping.

        **Usage:** `g_info`

        **Permission:** User"""
        commands = len(self.bot.commands)
        cogs = len(self.bot.cogs)
        version = discord.__version__
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping = (after - before) * 1000
        pversion = platform.python_version()
        server_count = 0
        member_count = 0
        channel_count = 0
        for server in self.bot.guilds:
            server_count += 1
            for channel in server.channels:
                channel_count += 1
            for member in server.members:
                member_count += 1
        await ctx.send("""```prolog
=========[ Bot Information ]=========

Commands           :  {0}
Cogs               :  {1}
Version            :  {2}
DiscordPY Version  :  {3}
Python Version     :  {4}
Websocket Ping     :  {5:.0f}ms
Uptime             :  {6}

=========[ Guild Information ]=========

Guilds             :  {7}
Users              :  {8}
Channels           :  {9}
Host               :  heroku```""".format(commands, cogs, self.bot.version, version, pversion, ping, self.get_bot_uptime(), server_count, member_count, channel_count))

        
    @commands.command(pass_context=True)
    async def avatar(self, ctx):
        """Get a user-friendly image of the specified user's avatar.
        If no user is specified, the user is the author.

        **Usage:** `g_avatar [user]`

        **Permission:** User"""
        mavi = ctx.message.author.avatar_url
        mavi = mavi.replace("gif?size=1024", "gif")
        mavi = mavi.replace("webp?size=1024", "png?size=512")
        mavi = mavi.replace("?size=1024", "?size=512")
        if len(ctx.message.mentions) == 0:
            if mavi == "":
                embed = discord.Embed(title="Your avatar!",description="Click [here]("+ctx.message.author.default_avatar_url+")!",color=ctx.message.author.color).set_image(url=ctx.message.author.default_avatar_url).set_footer(icon_url=ctx.message.author.default_avatar_url, text="Requested by "+ctx.message.author.display_name)
            else:
                embed = discord.Embed(title="Your avatar!",description="Click [here]("+mavi+")!",color=ctx.message.author.color).set_image(url=mavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await ctx.send(content=None, embed=embed)
        elif len(ctx.message.mentions) > 0:
            yavi = ctx.message.mentions[0].avatar_url
            yavi = yavi.replace("gif?size=1024", "gif")
            yavi = yavi.replace("webp?size=1024", "png?size=512")
            yavi = yavi.replace("?size=1024", "?size=512")
            if yavi == "":
                if mavi == "":
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+ctx.message.mentions[0].default_avatar_url+")!",color=ctx.message.author.color).set_image(url=ctx.message.mentions[0].default_avatar_url).set_footer(icon_url=ctx.message.author.default_avatar_url, text="Requested by "+ctx.message.author.display_name)
                else:
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+ctx.message.mentions[0].default_avatar_url+")!",color=ctx.message.author.color).set_image(url=ctx.message.mentions[0].default_avatar_url).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            else:
                if mavi == "":
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+yavi+")!",color=ctx.message.author.color).set_image(url=yavi).set_footer(icon_url=ctx.message.author.default_avatar_url, text="Requested by "+ctx.message.author.display_name)
                else:
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+yavi+")!",color=ctx.message.author.color).set_image(url=yavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await ctx.send(content=None, embed=embed)
        else:
            await ctx.send("There was an unexpected error.")
            

    @commands.command(pass_context=True, aliases=["sinfo", "ginfo", "guildinfo"])
    async def serverinfo(self, ctx):
        """Get information about the current server.

        **Usage:** `g_serverinfo`

        **Permission:** User"""
        roles = len(ctx.message.guild.roles) - 1 # w/ role_list
        created = ctx.message.guild.created_at.strftime("%d/%m/%y %H:%M:%S") # 2
        region = ctx.message.guild.region # 3
        verification = ctx.message.guild.verification_level # 4
        text_channels = len([x for x in ctx.message.guild.channels #5
                             if isinstance(x, discord.TextChannel)])
        categories = len([c for c in ctx.message.guild.channels
                             if isinstance(c, discord.CategoryChannel)])
        voice_channels = len(ctx.message.guild.channels) - text_channels - categories # 5
        online = len([m.status for m in ctx.message.guild.members # 6
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        total_users = len(ctx.message.guild.members) # 6
        passed = (ctx.message.created_at - ctx.message.guild.created_at).days # 2
        owner = ctx.message.guild.owner # 8
        role_list = ""
        sortedRoles = sorted(ctx.message.guild.roles, key=lambda x: -x.position)
        for x in range(0, len(sortedRoles)): # alone
            if sortedRoles[x].is_default():
                continue
            elif x == len(sortedRoles) - 1:
                role_list += sortedRoles[x].name
            else:
                role_list += sortedRoles[x].name + ", "
        # start embed building
        em = discord.Embed(description="Information about the server **{}**".format(ctx.message.guild.name),color=ctx.message.author.color)
        em.set_author(name="Server information",icon_url=ctx.message.guild.icon_url)
        em.add_field(name="Region",value=str(region),inline=True)
        em.add_field(name="Users",value="{} online/{} total".format(online, total_users),inline=True)
        em.add_field(name="Verification Level",value=str(verification), inline=True)
        em.add_field(name="Channels",value="{} text/{} voice in {} categories.".format(text_channels, voice_channels, categories),inline=True)
        em.add_field(name="Owner",value=str(owner),inline=True)
        em.add_field(name="Owner ID",value=str(owner.id),inline=True)
        em.add_field(name="Created At",value="{}, around {} days ago.".format(created, passed),inline=False)
        if role_list == "":
            em.add_field(name="Roles - "+str(roles),value="None",inline=False)
        elif role_list != "":
            em.add_field(name="Roles - "+str(roles),value=str(role_list),inline=False)
        em.set_thumbnail(url=ctx.message.guild.icon_url)
        em.set_footer(text="Server ID: {}".format(ctx.message.guild.id))
        await ctx.send(embed=em)
            

    @commands.command(pass_context=True, aliases=["uinfo", "whois"])
    async def userinfo(self, ctx):
        """Get information on a user.
        The user can be defined by either a mention or an id. If left blank, the user is the author.

        **Usage:** `g_userinfo [user]`

        **Permission:** User"""
        try: # error catcher p1
            if len(ctx.message.mentions) == 0:
                try:
                    args = ctx.message.content
                    args = args.split(' ')
                    u = int(args[1])
                    try:
                        getInfo = await self.bot.get_user_info(u)
                        user = getInfo
                    except discord.NotFound:
                        user = ctx.message.author
                except IndexError:
                    user = ctx.message.author
                except ValueError:
                    user = ctx.message.author
            else:
                user = ctx.message.mentions[0]
            # wew
            try:
                if user == getInfo:                                                             
                    if getInfo.id not in [member.id for member in ctx.message.guild.members]:   # the `user == getInfo` is a check to see
                        join = "N/A"                                                            # if the user it is retrieving from an id
                        toprole = "N/A"                                                         # or not
                        color = 0x000000
                        vc = "N/A"
                        game = "None or I can't tell."
                        status = "None or I can't tell."
                        roles = "N/A"
                        role_list = "N/A"
                    else:
                        user = discord.utils.get(ctx.message.guild.members, id=getInfo.id)
                        join = user.joined_at.strftime("%d/%m/%y %H:%M:%S")
                        toprole = user.top_role.name
                        color = user.color
                        vc = user.voice
                        game = user.game
                        status = user.status
                        roles = len(user.roles) - 1
                        role_list = ""
                        for x in range(0, len(user.roles)):
                            if user.roles[x].is_default():
                                continue
                            if x == len(user.roles) - 1:
                                role_list += user.roles[x].name
                            else:
                                role_list += user.roles[x].name + ", " # hi this doesnt work
            except UnboundLocalError:
                join = user.joined_at.strftime("%d/%m/%y %H:%M:%S")
                toprole = user.top_role.name
                color = user.color
                vc = user.voice
                game = user.game
                status = user.status
                roles = len(user.roles) - 1
                role_list = ""
                for x in range(0, len(user.roles)):
                    if user.roles[x].is_default():
                        continue
                    if x == len(user.roles) - 1:
                        role_list += user.roles[x].name
                    else:
                        role_list += user.roles[x].name + ", "
            created = user.created_at.strftime("%d/%m/%y %H:%M:%S")
            uid = user.id
            isbot  = user.bot
            nick = user.display_name
            avatar = user.avatar_url.replace("?size=1024", "")
            defAvi = user.default_avatar_url
            # badges
            badges = ""
            if uid in creditedids:
                badges = ":star: "+badges
                top = "Credited in `about credits`"
            if uid in donatorids:
                badges = ":moneybag: "+badges
                top = "Donator"
            if uid in helperids:
                badges = ":wrench: "+badges
                top = "Support Server Moderator"
            if uid in ownerids:
                badges = ":tools: "+badges
                top = "Developer"
            if badges == "":
                badges = "None"
                top = "User"
            # start embed creation
            em = discord.Embed(title=str(user)+"'s user info",description="**{}**".format(top),color=color)
            em.add_field(name="Join Date",value=str(join),inline=True)
            em.add_field(name="Account Creation",value=str(created),inline=True)
            em.add_field(name="User ID",value=str(uid),inline=True)
            em.add_field(name="Is Bot",value=str(isbot),inline=True)
            # send badges
            em.add_field(name="Badges",value="{}".format(badges))
            # avatars
            if defAvi == "https://cdn.discordapp.com/embed/avatars/0.png":
                em.add_field(name="Default Avatar",value="<:avi0:343852806563692554> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/1.png":
                em.add_field(name="Default Avatar",value="<:avi1:343852807322992650> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/2.png":
                em.add_field(name="Default Avatar",value="<:avi2:343852808191344640> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/3.png":
                em.add_field(name="Default Avatar",value="<:avi3:343852808610775042> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/4.png":
                em.add_field(name="Default Avatar",value="<:avi4:343852809340583937> **[Click here!]({})**".format(defAvi))
            # status
            if status == discord.Status.online:
                em.add_field(name="Status", value="Online")
            elif status == discord.Status.idle:
                em.add_field(name="Status", value="Idle")
            elif status == discord.Status.dnd:
                em.add_field(name="Status", value="Do Not Disturb")
            elif status == discord.Status.offline:
                em.add_field(name="Status", value="Offline")
            elif status == "None or I can't tell.":
                em.add_field(name="Status", value=status)
            # nickname
            if user.name == user.display_name:
                em.add_field(name="Nickname",value="None",inline=True)
            elif user.name != user.display_name:
                em.add_field(name="Nickname",value=str(nick),inline=True)
            # standard embed creation
            em.add_field(name="Voice Channel",value=str(vc),inline=True)
            em.add_field(name="Colour",value=str(color),inline=True)
            # top role, game, and role list
            if toprole == "@everyone":
                em.add_field(name="Top Role",value="User has no roles.",inline=True)
            elif toprole != "@everyone":
                em.add_field(name="Top Role",value=str(toprole),inline=True)
            em.add_field(name="Game",value=str(game),inline=False)
            if role_list == "":
                em.add_field(name="Roles - "+str(roles),value="None",inline=False)
            elif role_list != "":
                em.add_field(name="Roles - "+str(roles),value=str(role_list),inline=False)
            # finish embed creation and send
            em.set_thumbnail(url=avatar)
            await ctx.send(embed=em)
        except Exception as e: # error catcher p2
            await ctx.send("An unexpected error occurred when running the command! `{}`".format(type(e).__name__+": "+str(e))
                          +"\nYou shouldn't receive an error like this."
                          +"\nPlease contact Desiree#3658.")

    @commands.command()
    async def status(self, ctx):
        """Display the current status of the specified member.
        If the member is not specified or an invalid member argument is passed, the member is the author.

        **Usage:** `g_status [member]`

        **Permission:** User"""
        if len(ctx.message.mentions) == 0:
            user = ctx.message.author
            a = ", you are "
        else:
            user = ctx.message.mentions[0]
            a = " is "
        if user.game is None:
            game = "Nothing."
            footer = "Maybe you should get out into the world. Meet some people. Could be good for you."
        else:
            game = str(user.game)
            footer = "Hope it's a fun one!"
        em = discord.Embed(title=user.display_name+a+"playing:",description="`{}`".format(game),color=user.color)
        em.set_footer(text=footer)
        await ctx.send(embed=em)

    @commands.command()
    async def changelog(self, ctx):
        """Check the most recent changelog for all of the newer features!

        **Usage:** `g_changelog`

        **Permission:** User"""
        changelogChannel = discord.utils.get(discord.utils.get(self.bot.guilds, id=315251940999299072).channels, id=315602734235516928)
        async for m in changelogChannel.history(limit=1):
            changelog = m.clean_content
            desii = m.author
            lastUpdate = m.created_at
        em = discord.Embed(description=changelog, color=ctx.message.author.color)
        em.set_author(icon_url=desii.avatar_url.replace("?size=1024", ""), name="Found the latest changelog from my support guild!")
        em.timestamp = lastUpdate
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Info(bot))
