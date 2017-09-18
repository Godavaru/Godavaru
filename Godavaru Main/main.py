import discord
import asyncio
from discord.ext import commands
import random
import string
import time
import datetime, re
import configparser
import aiohttp

config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix=[config['Main']['prefix'], config['Main']['prefix2']])
bot.remove_command("help")
startup_extensions = ["cog_info", "cog_fun", "cog_action", "cog_owner", "cog_mod", "cog_utils"]
console = discord.Object('316688736089800715')

ownerids = [
    '267207628965281792',
    '99965250052300800',
    '170991374445969408',
    '188663897279037440'
]
blacklist = [
    "",
]

larsLolCounter = 0

messageCount = 0
commandsExecuted = 0
totalErrors = 0

# ready
@bot.event
async def on_ready():
    commands = len(bot.commands)
    server_count = 0
    member_count = 0
    for server in bot.servers:
        server_count += 1
        for member in server.members:
            member_count += 1
    print("["+str(datetime.datetime.now().strftime("%H:%M:%S"))+"][Godavaru]")
    print("===============")
    print("Logged in as")
    print(str(bot.user))
    print("===============")
    print('Ready for use.')
    print("Servers: "+str(server_count))
    print("Members: "+str(member_count))
    print("===============")
    print('Loaded up `'+str(commands)+"` commands in `"+str(len(bot.cogs))+"` cogs.")
    print('===============')
    await bot.change_presence(game=discord.Game(name='{0}help | with {1} servers and {2} users!'.format(bot.command_prefix[0], server_count, member_count)))
    await bot.send_message(console, '[`'+str(datetime.datetime.now().strftime("%H:%M:%S"))+'`][`Godavaru`]\n===============\nLogged in as:\n'+str(bot.user)+'\n===============\nReady for use.\nServers: `' + str(server_count) + '`\nMembers: `' + str(member_count) + '`\n===============\nLoaded up `'+str(commands)+"` commands in `"+str(len(bot.cogs))+"` cogs.\n===============")
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()
    
# server join
@bot.event
async def on_server_join(server):
    await bot.send_message(console, ':tada: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] I joined the server `' + server.name + '` ('+ server.id + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ').')
    guild_count = len(bot.servers)
    headers = {'Authorization': config['Main']['dbotstoken']}
    data = {'server_count': guild_count}
    api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
    async with aiohttp.ClientSession() as session:
        await session.post(api_url, data=data, headers=headers)

# server leave
@bot.event
async def on_server_remove(server):
    await bot.send_message(console, ':frowning: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] I left the server `' + server.name + '` ('+ server.id + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')
    guild_count = len(bot.servers)
    headers = {'Authorization': config['Main']['dbotstoken']}
    data = {'server_count': guild_count}
    api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
    async with aiohttp.ClientSession() as session:
        await session.post(api_url, data=data, headers=headers)

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
    if message.author.bot == False and message.server is not None:
        if message.server.id == "213468583252983809":
            if message.author.id == "132584525296435200":
                if "lol" in message.content.lower():
                    global larsLolCounter
                    larsLolCounter += 1
        if "\uD83D\uDD95" in message.content:
            if message.author.id == "232542027550556160":
                await bot.add_reaction(message, 'itstimetostop:358957198866644992')
        args = message.content
        if message.content.lower() == "f":
            if message.author.id == "267207628965281792":
                await bot.send_message(channel, "You have paid your respects. :eggplant:")
        elif message.content.lower().startswith('aaa'):
            if message.author.id == "267207628965281792":
                await bot.send_message(channel, "You're cute, Desii.")
        ### = = = = = removed deprecated prefix warning = = = = = ###
        if message.author.id not in blacklist:
            await bot.process_commands(message)
            args = message.content
            args = args.replace(bot.command_prefix[0], "")
            args = args.replace(bot.command_prefix[1], "")
            args = args.split(' ')
            if message.content.startswith(bot.command_prefix[0]) or message.content.startswith(bot.command_prefix[1]):
                if args[0] in bot.commands:
                    global commandsExecuted
                    commandsExecuted += 1
                    if args[0] != "owner" and args[0] != "ping" and args[0] != "reload" and args[0] != "unload" and args[0] != "load":
                        await bot.send_message(console, ":warning: [`"+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+"`] **{0.author.name}#{0.author.discriminator}** (`{0.author.id}`) issued my `{1}` command in **{0.server.name}** (`{0.server.id}`) owned by **{0.server.owner.name}#{0.server.owner.discriminator}** (`{0.server.owner.id}`) in channel **#{0.channel.name}** (`{0.channel.id}`)".format(message, args[0]))
    check = 'true'
    try:
	    if (message.server.name != ''):
		    check = 'true'
    except AttributeError:
	    if (message.author.bot == False):
		    await bot.send_message(console, ":warning: [`"+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+"`] A user sent me a direct message!\n\n**User**: `" + message.author.name + '#' + message.author.discriminator + '`\n**Content**: ```css\n' + message.content + "```")
		    check = 'false'

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# error handler
@bot.event
async def on_command_error(error, ctx):
    args = ctx.message.content
    args = args.split(' ')
    command = args[0][2:]
    errid = id_generator()
    if isinstance(error, commands.CommandNotFound):
        return
    global totalErrors
    totalErrors += 1
    await bot.send_message(ctx.message.channel, ":x: I ran into an error! Please report this on the support guild with the error ID, which is **{1}**. ```py\n{0}```".format(str(error)[29:], errid))
    await bot.send_message(console, ":warning: [`"+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+"`][`Cmd:{1}:{2}`] Ignoring exception on command `{0}`:\n{3}\n\n**Error ID:** {4}".format(command, str(ctx.message.author), ctx.message.clean_content, str(error)[29:], errid))

# help command
@bot.command(pass_context = True)
async def help(ctx):
    args = ctx.message.content
    args = args.split(' ')
    try:
        if args[1] == "lewd":
            embed = discord.Embed(title="Lewd Command",description="Believe it or not, it's completely sfw...",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"lewd").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "lood":
            embed = discord.Embed(title="Lood Command",description="Believe it or not, it's completely sfw...",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"lood").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "say":
            embed = discord.Embed(title="Say Command",description="Make me say something!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"say [--s] <message>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "year":
            embed = discord.Embed(title="Year Command",description="The first command on this bot. You wont regret it :eyes:",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"year").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "f":
            embed = discord.Embed(title="F Command",description="Pay your respects",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"f").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "8ball" or args[1] == "mb" or args[1] == "magicball":
            embed = discord.Embed(title="8ball Command",description="Ask the magic 8ball a question!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+args[1]+" <question>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "love":
            embed = discord.Embed(title="Love Command",description="Use the love meter to find compatibility between you and something :eyes:",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"love <@user or thing>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "flip":
            embed = discord.Embed(title="Flip Command",description="Flip someone!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"flip <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "lenny":
            embed = discord.Embed(title="Lenny Command",description="Make a lenny face.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"lenny").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "nonowa":
            embed = discord.Embed(title="Nonowa Command",description="Make a nonowa face.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"nonowa").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "cuddle":
            embed = discord.Embed(title="Cuddle Command",description="Cuddle someone! Awww!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"cuddle <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "hug":
            embed = discord.Embed(title="Hug Command",description="Hug someone! How cute!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"hug <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "slap":
            embed = discord.Embed(title="Slap Command",description="Is someone annoying you? Slap them!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"slap <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "kiss":
            embed = discord.Embed(title="Kiss Command",description="Do you know that special someone? Just kiss them already!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"kiss <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "pat":
            embed = discord.Embed(title="Pat Command",description="*pats*",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"pat <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "poke":
            embed = discord.Embed(title="Poke Command",description="What is this, Facebook? ",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"poke <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "wakeup":
            embed = discord.Embed(title="Wakeup Command",description="Someone needs to wake the hell up :eyes:",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"wakeup <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "cry":
            embed = discord.Embed(title="Cry Command",description="Do you need to cry? :<",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"cry [@user]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "kill":
            embed = discord.Embed(title="Kill Command",description="When in doubt, kill your enemies... i mean wut\n\n**NOTE:** Has a slight chance of failing and backfiring on you. Kill with caution ;)",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"kill <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "shrug":
            embed = discord.Embed(title="Shrug Command",description="¯\_(ツ)_/¯",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"shrug").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "about":
            embed = discord.Embed(title="About Command",description="Display some things about me!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "invite":
            embed = discord.Embed(title="Invite Command",description="Displays some important links, most importantly the invite links",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "request":
            embed = discord.Embed(title="Request Command",description="Request some new features for the bot!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"request <feature>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "ping":
            embed = discord.Embed(title="Ping Command",description="Play ping-pong with the bot and print the result.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"ping").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "info":
            embed = discord.Embed(title="Info Command",description="STAAAATTTTTTTSSSS. SSSSSSSSSSTTTTTTTTTTTTTTAAAAAAAAAAAAAAAATTTTTTTTTTTTTSSSSSSSSSSSSSS\n\n... so just display some stats about me",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"info").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "avatar":
            embed = discord.Embed(title="Avatar Command",description="Get someone's avatar!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"avatar [@user]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "help":
            embed = discord.Embed(title="Help Command",description="Uhm... Is this what you were looking for?",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"help [command]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "sleep":
            embed = discord.Embed(title="Sleep Command",description="The literal opposite of wakeup. This is also based off of my best friend, Kitty#4867, who would always tell me to go to bed. Love ya, Kat! ~Desii",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"sleep <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "kick":
            embed = discord.Embed(title="Kick Command",description="Kick someone from the current server.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"kick <@user> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "ban":
            embed = discord.Embed(title="Ban Command",description="Ban someone from the current server.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"ban <@user> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "hackban":
            embed = discord.Embed(title="Hackban Command",description="Ban someone from the current server by ID.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"hackban <user id> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "unban":
            embed = discord.Embed(title="Unban Command",description="Unban someone from the current server by ID.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"unban <user id> ").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "softban":
            embed = discord.Embed(title="Softban Command",description="Effectively kick someone while pruning all previous messages.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"softban <@user> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "prune" or args[1] == "purge" or args[1] == "clean":
            embed = discord.Embed(title="Prune Command",description="Prune a certain number of messages!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+args[1]+" <number>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "roll":
            embed = discord.Embed(title="Roll Command",description="Roll a six sided die!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"roll").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "slots":
            embed = discord.Embed(title="Slots Command",description="Play a game of slots!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"slots").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "rps":
            embed = discord.Embed(title="Rock/paper/scissors Command",description="Play a game of rock/paper/scissors with the bot!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"rps <rock|paper|scissors>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "len" or args[1] == "length":
            embed = discord.Embed(title="Length Command",description="Determine the length of a message.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+args[1]+" <content>").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "dog":
            embed = discord.Embed(title="Dog Command",description="Woof.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"dog").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "cat":
            embed = discord.Embed(title="Cat Command",description="Meow.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"cat").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "urban":
            embed = discord.Embed(title="Urban Command",description="Search urban dictionary",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+"slots").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "nekos" or args[1] == "catgirls":
            embed = discord.Embed(title="Catgirl/Neko Command",description="Get some images of catgirls! (AKA nekos. Whatever you wanna call em)",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+args[1]+" [nsfw]").set_footer(text="Requested by "+ctx.message.author.display_name)
        elif args[1] == "embed":
            embed = discord.Embed(title="Embed Command",description="Build an embed!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix[0]+args[1]+" <args>\n\n    `(Guide coming soon)`").set_footer(text="Requested by "+ctx.message.author.display_name)
        else:
            await bot.send_message(ctx.message.channel, ":x: That command doesn't exist or there is no extended help!")
            return
    except IndexError:
        commands = len(bot.commands)
        embed = discord.Embed(title="The bot prefix is: "+bot.command_prefix[0],color=ctx.message.author.color)
        embed.set_author(name="For more help, do "+bot.command_prefix[0]+"help <command>",icon_url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png')
        embed.add_field(name="Action",value="`cuddle`, `cry`, `hug`, `kiss`, `pat`, `poke`, `slap`, `sleep`, `shrug`, `wakeup`",inline=False)
        embed.add_field(name="Fun",value="`f`, `flip`, `lewd`, `lood`, `love`, `nonowa`, `rps`, `roll`, `say`, `slots`, `year`",inline=False)
        embed.add_field(name="Info",value="`about`, `avatar`, `info`, `invite`, `ping`, `request`, `roleinfo`",inline=False)
        embed.add_field(name="Utils",value="`8ball`, `banlist`, `cat`, `dog`, `embed`, `len`, `nekos`, `urban`",inline=False)
        embed.set_footer(text="Requested by "+ctx.message.author.display_name+" | Total commands: "+str(commands))
        if ctx.message.author.id in ownerids:
            embed.add_field(name="Owner",value="`load`, `owner`, `reload`, `unload`", inline=False) # adds field if you have access to this. prep for mod cmds
        if ctx.message.author.server_permissions.ban_members == True or ctx.message.author.server_permissions.kick_members == True:
            embed.add_field(name="Mod",value="`ban`, `disconnect`, `kick`, `prune`, `softban`, `unban`",inline=False) #mod cmds
    await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context=True)
async def stats(ctx):
        allMembers = 0
        allChannels = 0
        onlineUsers = 0
        over50 = 0
        over100 = 0
        over500 = 0
        over1000 = 0
        m = []
        c = []
        for server in bot.servers:
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
        ua = uma / umi
        ca = cma / cmi
        em = discord.Embed(title="Well, I did my maths!",color=ctx.message.author.color)
        em.set_thumbnail(url=ctx.message.server.me.avatar_url)
        em.add_field(name="Messages Seen",value=str(messageCount))
        em.add_field(name="Commands Executed",value=str(commandsExecuted))
        em.add_field(name="Total Errors",value=str(totalErrors))
        em.add_field(name="Guilds",value=str(len(bot.servers)))
        em.add_field(name="Guilds > 50",value=str(over50))
        em.add_field(name="Guilds > 100",value=str(over100))
        em.add_field(name="Guilds > 500",value=str(over500))
        em.add_field(name="Guilds > 1000",value=str(over1000))
        em.add_field(name="Users",value=str(allMembers))
        em.add_field(name="Channels",value=str(allChannels))
        em.add_field(name="Users Per Server",value="Min: {0}\nMax: {1}\nAverage: {2}".format(umi, uma, ua))
        em.add_field(name="Channels Per Server",value="Min: {0}\nMax: {1}\nAverage: {2}".format(cmi, cma, ca))
        await bot.say(embed=em)

# This is a meme now
@bot.command(pass_context = True)
async def test(ctx):
    await bot.say("hey look, you found a dead meme that isn't even in the help menu. now stop stalking the github :eyes:")

# Mantaro Hub Memes
@bot.command(pass_context=True)
async def lol(ctx):
    if ctx.message.server.id == "213468583252983809":
        await bot.say("Lars' total lol counter since my startup is `{}`!".format(larsLolCounter))

# force update
@bot.command(pass_context=True)
async def update(ctx):
    if ctx.message.author.id in ownerids:
        guild_count = len(bot.servers)
        headers = {'Authorization': config['Main']['dbotstoken']}
        data = {'server_count': guild_count}
        api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)
        await bot.say("Sent stats to discordbots.org")
    else:
        return
    
# cog commands
@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
    if ctx.message.author.id not in ownerids:
        await bot.say(":x: You do not have permission to execute this command.")
    else:
        try:
            bot.load_extension("cog_"+extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say(":white_check_mark: Cog **`{}`** loaded.".format(extension_name))

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
    if ctx.message.author.id not in ownerids:
        await bot.say(":x: You do not have permission to execute this command.")
    else:
        bot.unload_extension("cog_"+extension_name)
        await bot.say(":white_check_mark: Cog **`{}`** unloaded.".format(extension_name))

@bot.command(pass_context=True)
async def reload(ctx, extension_name : str):
    if ctx.message.author.id not in ownerids:
        await bot.say(":x: You do not have permission to execute this command.")
    else:
        try:
            bot.unload_extension("cog_"+extension_name)
            bot.load_extension("cog_"+extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say(":white_check_mark: Cog **`{}`** reloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))
            
bot.run(config['Main']['token'])
