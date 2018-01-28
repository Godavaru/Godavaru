import datetime
lt = datetime.datetime.now()
# Discord
import discord
from discord.ext import commands
from utils.tools import *
from utils.version import *
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
import requests
import datetime
import inspect

# Other
import pytz
import aiohttp
import configparser
import sqlite3
import threading
import urllib
import hastebin
import string

# Code Interpreters
import js2py

config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot([config['Main']['prefix'], config['Main']['prefix2']])
bot.remove_command("help")
startup_extensions = ["cog_info", "cog_fun", "cog_action", "cog_owner", "cog_mod", "cog_utils"]

ownerids = [
    267207628965281792,
    99965250052300800,
    170991374445969408,
    188663897279037440,
    132584525296435200
]
blacklist = []

larsLolCounter = 0

webhook = Webhook.partial(int(config['Main']['webhook-id']), config['Main']['webhook-token'], adapter=RequestsWebhookAdapter())

messageCount = 0
commandsExecuted = 0
totalErrors = 0

# ready
@bot.event
async def on_ready():
    server_count = len(bot.guilds)
    member_count = 0
    for server in bot.guilds:
        for member in server.members:
            member_count += 1
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()
    if not hasattr(bot, 'version'):
        bot.version = getBotVersion()
    console = bot.get_channel(316688736089800715)
    commands = len(bot.commands)
    startupMessage = """[`{}`][`Godavaru`]
===============
Logged in as:
{}
===============
Ready for use.
Servers: `{}`
Users: `{}`
===============
Loaded up `{}` commands in `{}` cogs in `{:.2f}` seconds.
===============
""".format(datetime.datetime.now().strftime("%H:%M:%S"), str(bot.user), server_count, member_count, commands, len(bot.cogs), (datetime.datetime.now() - lt).total_seconds())
    print(startupMessage.replace('`', ''))
    webhook.send(startupMessage)
    await bot.change_presence(game=discord.Game(name=bot.command_prefix[0]+"help | {} guilds with {} members.".format(server_count, member_count)))
    
# server join
@bot.event
async def on_guild_join(server):
    server_count = len(bot.guilds)
    member_count = 0
    for server in bot.guilds:
        for member in server.members:
            member_count += 1
    await bot.change_presence(game=discord.Game(name=bot.command_prefix[0]+"help | {} guilds with {} members.".format(server_count, member_count)))
    webhook.send(':tada: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] I joined the server `' + server.name + '` ('+ str(server.id) + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + str(server.owner.id) + ').')
    guild_count = len(bot.guilds)
    headers = {'Authorization': config['Main']['dbotstoken']}
    data = {'server_count': guild_count}
    api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
    async with aiohttp.ClientSession() as session:
        await session.post(api_url, data=data, headers=headers)

# server leave
@bot.event
async def on_guild_remove(server):
    server_count = len(bot.guilds)
    member_count = 0
    for server in bot.guilds:
        for member in server.members:
            member_count += 1
    await bot.change_presence(game=discord.Game(name=bot.command_prefix[0]+"help | {} guilds with {} members.".format(server_count, member_count)))
    webhook.send(content=':frowning: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] I left the server `' + server.name + '` ('+ server.id + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')
    guild_count = len(bot.guilds)
    headers = {'Authorization': config['Main']['dbotstoken']}
    data = {'server_count': guild_count}
    api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
    async with aiohttp.ClientSession() as session:
        await session.post(api_url, data=data, headers=headers)

@bot.event
async def on_message_edit(before, after):
    if after.content.startswith(bot.command_prefix[0]):
        if after.guild.name is not None and str(after.content) != str(before.content):
            await bot.process_commands(after)

# on message and dm
@bot.event
async def on_message(message):
    global messageCount
    messageCount += 1
    dm = message.content
    dm = dm.replace("`", "")
    channel = message.channel
    content = message.content
    author = message.author
    if message.author.bot == False and message.guild is not None:
        if message.content.lower() == "f":
            if message.author.id == 267207628965281792:
                await bot.send_message(channel, "You have paid your respects. :eggplant:")
        elif message.content.lower().startswith('aaa'):
            if message.author.id == 132584525296435200:
                await channel.send("Hey there, cutie.")
            elif message.author.id == 267207628965281792:
                await channel.send("You're cute, Desii.")
        elif message.content.startswith(message.guild.me.mention):
            await channel.send("H-hi there! If you're trying to use one of my commands, my prefix is `{0}`! Use it like: `{0}help`".format(bot.command_prefix[0]))
        if message.author.id not in blacklist:
            await bot.process_commands(message)
    if message.author.bot == False:
        if message.guild is None:
            await message.channel.send("Hey! Weirdo! Stop sending me dms. If you're trying to use commands, use it in a server.")
            webhook.send(content="[`"+str(datetime.datetime.now().strftime("%H:%M:%S"))+"`][`Godavaru`]\n"
                               +"[`CommandHandler`][`InterceptDirectMessage`]\n"
                               +"[`AuthorInformation`]: {} ({})\n".format(str(message.author), str(message.author.id))
                               +"[`MessageInformation`]: {} ({})\n".format(message.clean_content, str(message.id))
                               +"Intercepted direct message and sent alternate message.")
            print("["+str(datetime.datetime.now().strftime("%H:%M:%S"))+"][Godavaru]\n"
                  +"[CommandHandler][InterceptDirectMessage]\n"
                  +"[AuthorInformation]: {} ({})\n".format(str(message.author), str(message.author.id))
                  +"[MessageInformation]: {} ({})\n".format(message.clean_content, str(message.id))
                  +"Intercepted direct message and sent alternate message.\n")
            return

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# CommandHandler
@bot.event
async def on_command(ctx):
    global commandsExecuted
    commandsExecuted += 1
    global commandTime
    commandTime = datetime.datetime.now()
    webhook.send(content="[`"+str(datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S"))+"`][`Godavaru`]\n"
                       +"[`CommandHandler`][`Pre-Invoke`]\n"
                       +"[`GuildInformation`]: {}\n".format(ctx.message.guild.name+" ("+str(ctx.message.guild.id)+") owned by "+str(ctx.message.guild.owner)+" ("+str(ctx.message.author.id)+")")
                       +"[`AuthorInformation`]: {} ({})\n".format(str(ctx.message.author), str(ctx.message.author.id))
                       +"[`MessageInformation`]: {} ({})\n".format(ctx.message.clean_content, str(ctx.message.id)))
    print("["+str(datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S"))+"][Godavaru]\n"
                       +"[CommandHandler][Pre-Invoke]\n"
                       +"[GuildInformation]: {}\n".format(ctx.message.guild.name+" ("+str(ctx.message.guild.id)+") owned by "+str(ctx.message.guild.owner)+" ("+str(ctx.message.author.id)+")")
                       +"[AuthorInformation]: {} ({})\n".format(str(ctx.message.author), str(ctx.message.author.id))
                       +"[MessageInformation]: {} ({})\n".format(ctx.message.clean_content, str(ctx.message.id)))

@bot.event
async def on_command_completion(ctx):
    console = bot.get_channel(358776134243975169)
    latency = (datetime.datetime.now() - commandTime) * 1000
    webhook.send(content="[`"+str(datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S"))+"`][`Godavaru`][:white_check_mark:]\n"
                       +"[`CommandHandler`][`Completion`]\n"
                       +"Successfully processed command in message {0} in {1:.0f}ms".format(ctx.message.id, latency.total_seconds()))
    print("["+str(datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S"))+"][Godavaru]\n"
                       +"[CommandHandler][Completion]\n"
                       +"Successfully processed command in message {0} in {1:.0f}ms\n".format(ctx.message.id, latency.total_seconds()))

@bot.event
async def on_command_error(ctx, error):
    console = bot.get_channel(358776134243975169)
    errid = id_generator()
    if isinstance(error, commands.CommandNotFound):
        return
    global totalErrors
    totalErrors += 1
    await ctx.send(":x: I ran into an error! Please report this on the support guild with the error ID, which is **{1}**. ```py\n{0}```".format(str(error)[29:], errid))
    webhook.send(content="[`"+str(datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S"))+"`][`Godavaru`][:x:]\n"
                       +"[`CommandHandler`][`Error`]\n"
                       +"[`ErrorInformation`][`{}`]: {}\n".format(errid, str(error)[29:])
                       +"[`GuildInformation`]: {}\n".format(ctx.message.guild.name+" ("+str(ctx.message.guild.id)+") owned by "+str(ctx.message.guild.owner)+" ("+str(ctx.message.author.id)+")")
                       +"[`AuthorInformation`]: {} ({})\n".format(str(ctx.message.author), str(ctx.message.author.id))
                       +"[`MessageInformation`]: {} ({})\n".format(ctx.message.clean_content, str(ctx.message.id)))
    print("["+str(datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S"))+"][Godavaru]\n"
                       +"[CommandHandler][Error]\n"
                       +"[ErrorInformation]: {}\n".format(str(error)[29:])
                       +"[GuildInformation]: {}\n".format(ctx.message.guild.name+" ("+str(ctx.message.guild.id)+") owned by "+str(ctx.message.guild.owner)+" ("+str(ctx.message.author.id)+")")
                       +"[AuthorInformation]: {} ({})\n".format(str(ctx.message.author), str(ctx.message.author.id))
                       +"[MessageInformation]: {} ({})\n".format(ctx.message.clean_content, str(ctx.message.id)))


# help command
@bot.command()
async def help(ctx):
    """Shows a list of commands that I have or requests extra help on a command.

    **Usage:** `g_help [command]`

    **Permission:** User"""
    umsg = ctx.message.content
    args = umsg.split(' ')
    if len(args) > 1:
        cmd = bot.all_commands.get(args[1])
        if cmd == None:
            await ctx.send(":x: A command with that name doesn't exist.")
            return
        if cmd.hidden:
            await ctx.send(":x: You cannot request help on a hidden command, you baka. Stop being nosy.")
            return
        desc = cmd.help
        if desc is None:
            desc = "There is no extended help set for this command."
        em = discord.Embed(title="Extended help for: {}".format(args[1]),description=desc+"\n\nNote that arguments surrounded with `[]` are not required while arguments surrounded by `<>` are required. Do not include either of these in the command.",color=ctx.message.author.color)
        em.set_thumbnail(url="https://d30y9cdsu7xlg0.cloudfront.net/png/4439-200.png")
        await ctx.send(embed=em)
        return
    em = discord.Embed(title="Godavaru Help",description="The prefix is `{0}`. Do `{0}help <command>` without the brackets for extended help.".format(bot.command_prefix[0]),color=ctx.message.author.color)
    em.set_thumbnail(url=ctx.message.guild.me.avatar_url)
    for cog in sorted(bot.cogs, key=str.lower):
        if str(cog) == "Owner" and ctx.message.author.id not in ownerids:
            continue
        cog_commands = ""
        for command in sorted(bot.commands, key=lambda x: x.name):
            if command.cog_name == str(cog) and command.hidden == False:
                cog_commands += "`{}` ".format(str(command))
        if len(cog_commands) > 1024:
            cog_commands = hastebin.post(cog_commands)
        em.add_field(name=str(cog), value=cog_commands,inline=False)
    no_cog_commands = ""
    for command in sorted(bot.commands, key=lambda x: x.name):
        if command.cog_name == None and command.hidden == False:
            no_cog_commands += "`{}` ".format(str(command))
    if len(no_cog_commands) > 1024:
        no_cog_commands = hastebin.post(no_cog_commands)
    em.add_field(name="No Category",value=no_cog_commands,inline=False)
    em.set_footer(icon_url=ctx.message.author.avatar_url.replace("?size=1024", ""), text="Requested by {} | Total commands: {}".format(ctx.message.author.display_name, len(bot.commands)))
    await ctx.send(embed=em)


@bot.command(pass_context=True)
async def stats(ctx):
    """Get statistics about me.

    **Usage:** `g_stats`
    
    **Permission:** User"""
    allMembers = 0
    allChannels = 0
    onlineUsers = 0
    over50 = 0
    over100 = 0
    over500 = 0
    over1000 = 0
    m = []
    c = []
    for server in bot.guilds:
        m += [len(server.members)]
        c += [len(server.channels)]
        if len(server.members) > 50:
            over50 += 1
        if len(server.members) > 100:
            over100 += 1
        if len(server.members) > 500:
            over500 += 1
        if len(server.members) > 1000:
            over1000 += 1
        for member in server.members:
            allMembers += 1
        for channel in server.channels:
            allChannels += 1
    uma = max(m)
    cma = max(c)
    umi = min(m)
    cmi = min(c)
    ua = round(allMembers / len(bot.guilds), 2)
    ca = round(allChannels / len(bot.guilds), 2)
    em = discord.Embed(title="Well, I did my maths!",color=ctx.message.author.color)
    em.set_thumbnail(url=ctx.message.guild.me.avatar_url)
    em.add_field(name="Messages Seen",value=str(messageCount))
    em.add_field(name="Commands Executed",value=str(commandsExecuted))
    em.add_field(name="Total Errors",value=str(totalErrors))
    em.add_field(name="Guilds",value=str(len(bot.guilds)))
    em.add_field(name="Guilds > 50",value=str(over50))
    em.add_field(name="Guilds > 100",value=str(over100))
    em.add_field(name="Guilds > 500",value=str(over500))
    em.add_field(name="Guilds > 1000",value=str(over1000))
    em.add_field(name="Users",value=str(allMembers))
    em.add_field(name="Channels",value=str(allChannels))
    em.add_field(name="Users Per Server",value="Min: {0}\nMax: {1}\nAverage: {2}".format(umi, uma, ua))
    em.add_field(name="Channels Per Server",value="Min: {0}\nMax: {1}\nAverage: {2}".format(cmi, cma, ca))
    await ctx.send(embed=em)

# This is a meme now
@bot.command(hidden=True)
async def test(ctx):
    await ctx.send("hey look, you found a dead meme that isn't even in the help menu. now stop stalking the github :eyes:")

# Mantaro Hub Memes
@bot.command(hidden=True)
async def lol(ctx):
    if ctx.message.guild.id == 213468583252983809:
        msg = await ctx.send("Searching channels... (this may take a while)")
        l = 0
        for c in ctx.message.guild.channels:
            if isinstance(c, discord.TextChannel):
                if c.permissions_for(ctx.message.guild.me).read_messages:
                    async for m in c.history():
                        if m.author.id == 132584525296435200 and "lol" in m.content.lower():
                            l = l+1
        await msg.edit(content="Lars' total lol counter so far is: `{}`".format(l))

# force update
@bot.command(hidden=True)
async def update(ctx):
    if ctx.message.author.id in ownerids:
        guild_count = len(bot.guilds)
        headers = {'Authorization': config['Main']['dbotstoken']}
        data = {'server_count': guild_count}
        api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)
        await ctx.send("Sent stats to discordbots.org")
    else:
        return
    
# cog commands
@bot.command(hidden=True)
async def load(ctx, extension_name : str):
    if ctx.message.author.id not in ownerids:
        await ctx.send(":x: You do not have permission to execute this command.")
    else:
        try:
            bot.load_extension("cog_"+extension_name)
        except Exception as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await ctx.send(":white_check_mark: Cog **`{}`** loaded.".format(extension_name))

@bot.command(hidden=True)
async def unload(ctx, extension_name : str):
    if ctx.message.author.id not in ownerids:
        await ctx.send(":x: You do not have permission to execute this command.")
    else:
        bot.unload_extension("cog_"+extension_name)
        await ctx.send(":white_check_mark: Cog **`{}`** unloaded.".format(extension_name))

@bot.command(hidden=True)
async def reload(ctx, extension_name : str):
    if ctx.message.author.id not in ownerids:
        await ctx.send(":x: You do not have permission to execute this command.")
    else:
        try:
            bot.unload_extension("cog_"+extension_name)
            bot.load_extension("cog_"+extension_name)
        except Exception as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await ctx.send(":white_check_mark: Cog **`{}`** reloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))
            
bot.run(config['Main']['token'])
