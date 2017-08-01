import discord
import asyncio
from discord.ext import commands
import random
import time
import datetime, re
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix=config['Main']['prefix'])
bot.remove_command("help")
startup_extensions = ["cog_info", "cog_fun", "cog_action", "cog_owner", "cog_mod"]
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

# ready
@bot.event
async def on_ready():
    server_count = 0
    member_count = 0
    for server in bot.servers:
        server_count += 1
        for member in server.members:
            member_count += 1
    print("Starting up bot:")
    print(bot.user.name)
    print(bot.user.id)
    print("====================")
    commands = len(bot.commands)
    await bot.change_presence(game=discord.Game(name='g!help | with '+str(server_count)+' servers and '+str(member_count)+' users!'))
    await bot.send_message(console, 'Godavaru now ready! Preparing for use in `' + str(server_count) + '` servers for `' + str(member_count) + '` members! Loaded up `'+str(commands)+"` commands.")
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()
    
# server join
@bot.event
async def on_server_join(server):
    await bot.send_message(console, ':tada: I joined the server `' + server.name + '` ('+ server.id + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')


# server leave
@bot.event
async def on_server_remove(server):
    await bot.send_message(console, ':frowning: I left the server `' + server.name + '` ('+ server.id + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')


# on message and dm
@bot.event
async def on_message(message):
    dm = message.content
    dm = dm.replace("`", " ")
    if message.author.bot == False:
        if message.author.id not in blacklist:
            await bot.process_commands(message)
    check = 'true'
    try:
	    if (message.server.name != ''):
		    check = 'true'
    except AttributeError:
	    if (message.author.bot == False):
		    await bot.send_message(console, "A user sent me a direct message!\n\n**User**: `" + message.author.name + '#' + message.author.discriminator + '`\n**Content**: ```css\n' + message.content + "```")
		    check = 'false'

# this will be fixed later ;-;
@bot.event
async def on_error(e):
    print("There was an error, see #console")
    await bot.send_message(console, "<@!267207628965281792>, you fucked up. Fix it. ```\n" + str(e) + "```")

# help command
@bot.command(pass_context = True)
async def help(ctx):
    args = ctx.message.content
    args = args.replace(bot.command_prefix+"help", "")
    if args == " lewd":
        embed = discord.Embed(title="Lewd Command",description="Believe it or not, it's completely sfw...",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"lewd").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " lood":
        embed = discord.Embed(title="Lood Command",description="Believe it or not, it's completely sfw...",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"lood").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " say":
        embed = discord.Embed(title="Say Command",description="Make me say something!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"say [--s] <message>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " year":
        embed = discord.Embed(title="Year Command",description="The first command on this bot. You wont regret it :eyes:",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"year").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " f":
        embed = discord.Embed(title="F Command",description="Pay your respects",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"f").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " 8ball" or args == " mb" or args == " magicball":
        embed = discord.Embed(title=args+" Command",description="Ask the magic 8ball a question!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+args+" <question>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " love":
        embed = discord.Embed(title="Love Command",description="Use the love meter to find compatibility between you and something :eyes:",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"love <@user or thing>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " flip":
        embed = discord.Embed(title="Flip Command",description="Flip someone!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"flip <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " lenny":
        embed = discord.Embed(title="Lenny Command",description="Make a lenny face.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"lenny").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " nonowa":
        embed = discord.Embed(title="Nonowa Command",description="Make a nonowa face.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"nonowa").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " cuddle":
        embed = discord.Embed(title="Cuddle Command",description="Cuddle someone! Awww!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"cuddle <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " hug":
        embed = discord.Embed(title="Hug Command",description="Hug someone! How cute!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"hug <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " slap":
        embed = discord.Embed(title="Slap Command",description="Is someone annoying you? Slap them!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"slap <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " kiss":
        embed = discord.Embed(title="Kiss Command",description="Do you know that special someone? Just kiss them already!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"kiss <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " pat":
        embed = discord.Embed(title="Pat Command",description="*pats*",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"pat <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " poke":
        embed = discord.Embed(title="Poke Command",description="What is this, Facebook? ",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"poke <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " wakeup":
        embed = discord.Embed(title="Wakeup Command",description="Someone needs to wake the hell up :eyes:",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"wakeup <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " cry":
        embed = discord.Embed(title="Cry Command",description="Do you need to cry? :<",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"cry [@user]").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " kill":
        embed = discord.Embed(title="Kill Command",description="When in doubt, kill your enemies... i mean wut\n\n**NOTE:** Has a slight chance of failing and backfiring on you. Kill with caution ;)",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"kill <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " shrug":
        embed = discord.Embed(title="Shrug Command",description="¯\_(ツ)_/¯",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"shrug").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " about":
        embed = discord.Embed(title="About Command",description="Display some things about me!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " invite":
        embed = discord.Embed(title="Invite Command",description="Displays some important links, most importantly the invite links",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " request":
        embed = discord.Embed(title="Request Command",description="Request some new features for the bot!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"request <feature>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " ping":
        embed = discord.Embed(title="Ping Command",description="Play ping-pong with the bot and print the result.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"ping").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " info":
        embed = discord.Embed(title="Info Command",description="STAAAATTTTTTTSSSS. SSSSSSSSSSTTTTTTTTTTTTTTAAAAAAAAAAAAAAAATTTTTTTTTTTTTSSSSSSSSSSSSSS\n\n... so just display some stats about me",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"info").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " avatar":
        embed = discord.Embed(title="Avatar Command",description="Get someone's avatar!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"avatar [@user]").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " uptime":
        embed = discord.Embed(title="Uptime Command",description="Display the bot's uptime!",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"uptime").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " help":
        embed = discord.Embed(title="Help Command",description="Uhm... Is this what you were looking for?",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"help [command]").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " sleep":
        embed = discord.Embed(title="Sleep Command",description="The literal opposite of wakeup. This is also based off of my best friend, Kitty#4867, who would always tell me to go to bed. Love ya, Kat! ~Desii",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"sleep <@user>").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " kick":
        embed = discord.Embed(title="Kick Command",description="Kick someone from the current server.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"kick <@user> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " ban":
        embed = discord.Embed(title="Ban Command",description="Ban someone from the current server.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"ban <@user> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == " softban":
        embed = discord.Embed(title="Softban Command",description="Effectively kick someone while pruning all previous messages.",color=ctx.message.author.color).add_field(name="Usage",value=bot.command_prefix+"softban <@user> [reason]").set_footer(text="Requested by "+ctx.message.author.display_name)
    elif args == "":
        commands = len(bot.commands)
        embed = discord.Embed(title="The bot prefix is: "+bot.command_prefix,color=ctx.message.author.color).set_author(name="For more help, do "+bot.command_prefix+"help <command>",icon_url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name="Action",value="`cuddle`, `cry`, `hug`, `kiss`, `pat`, `poke`, `slap`, `sleep`, `shrug`, `wakeup`",inline=False).add_field(name="Fun",value="`f`, `flip`, `lewd`, `lood`, `love`, `magicball`, `nonowa`, `say`, `year`",inline=False).add_field(name="Info",value="`about`, `avatar`, `info`, `invite`, `ping`, `request`, `uptime`",inline=False).set_footer(text="Requested by "+ctx.message.author.display_name+" | Total commands: "+str(commands))
        if ctx.message.author.id in ownerids:
            embed.add_field(name="Owner",value="`load`, `owner`, `reload`, `unload`", inline=False) # adds field if you have access to this. prep for mod cmds
        if ctx.message.author.server_permissions.ban_members == True or ctx.message.author.server_permissions.kick_members == True:
            embed.add_field(name="Mod",value="`ban`, `kick`, `softban`",inline=False) #mod cmds
        await bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` issued my `help` command in channel `' + ctx.message.channel.name + '` in  server `' + ctx.message.server.name + '`')
    else:
        await bot.send_message(ctx.message.channel, ":x: That command doesn't exist!")    
    await bot.send_message(ctx.message.channel, content=None, embed=embed)

# The test command is for me to try new features
@bot.command(pass_context = True)
async def test(ctx):
    if ctx.message.author.id != "267207628965281792":
        await bot.say("Uh... no test command here... *runs*")
    else:
        await bot.edit_role(ctx.message.server, discord.utils.get(ctx.message.server.roles, id="328329598322475009"), colour=discord.Color(0x66daff), permissions=discord.Permissions(permissions=1609956470))

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
