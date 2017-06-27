import discord
import asyncio
from discord.ext import commands
import random
import time
import datetime, re

bot = commands.Bot(command_prefix="g!")
bot.remove_command("help")
startup_extensions = ["cog_info", "cog_fun", "cog_faces", "cog_action", "cog_owner", "cog_mod"]
console = discord.Object('316688736089800715')

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
    await bot.send_message(console, 'Godavaru now ready! Preparing for use in `' + str(server_count) + '` servers for `' + str(member_count) + '` members!')
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
    if ctx.message.content[7:] == "echo":
        await bot.say ("Use `" + bot.command_prefix + "echo <text>` to make me echo something!")
    elif ctx.message.content[7:] == "about":
        await bot.say ("Display the facts about me by doing `" + bot.command_prefix + "about`!")
    elif ctx.message.content[7:] == "help":
        await bot.say ("Uh... really? just do `" + bot.command_prefix + "help`...")
    elif ctx.message.content[7:] == "request":
        await bot.say ("Request something to add by doing `" + bot.command_prefix + "request <suggestion>`! Make sure it's longer than three characters!")
    elif ctx.message.content[7:] == "kill":
        await bot.say ("Kill your worst enemies! ~~Or friends, whatever you wish.~~ Do `" + bot.command_prefix + "kill <@user>`")
    elif ctx.message.content[7:] == "lewd":
        await bot.say ("What should we do? `" + bot.command_prefix + "lewd`")
    elif ctx.message.content[7:] == "lood":
        await bot.say ("S-senpai! `" + bot.command_prefix + "lood`")
    elif ctx.message.content[7:] == "say":
        await bot.say ("Make me say something by doing `" + bot.command_prefix + "say <text>`")
    elif ctx.message.content[7:] == "shru":
        await bot.say ("I hope that was a spelling error... `" + bot.command_prefi + "shru`")
    elif ctx.message.content[7:] == "year":
        await bot.say ("See my very first fun command! It's good I promise ( ͡° ͜ʖ ͡°) `" + bot.command_prefix + "year`")
    elif ctx.message.content[7:] == "lenny":
        await bot.say ("Make a lenny face by doing `" + bot.command_prefix + "lenny`!")
    elif ctx.message.content[7:] == "shrug":
        await bot.say ("Uhh... idk *shrugs* `" + bot.command_prefix + "shrug`")
    elif ctx.message.content[7:] == "hug":
        await bot.say ("To hug a user, do `" + bot.command_prefix + "hug <@user>`! :hugging:")
    elif ctx.message.content[7:] == "kiss":
        await bot.say ("Kiss me before I lose my mind!! `" + bot.command_prefix + "kiss <@user>`")
    elif ctx.message.content[7:] =="poke":
        await bot.say ("Don't poke me! Poke someone else with `" + bot.command_prefix + "poke <@user>`!")
    elif ctx.message.content[7:] =="cuddle":
        await bot.say ("<:godavarublobhug:318227863646109696> Cuddle someone with `" + bot.command_prefix + "cuddle <@user>`")
    elif ctx.message.content[7:] == "nonowa":
        await bot.say ("Make a nonowa face! `" + bot.command_prefix + "nonowa`")
    elif ctx.message.content[7:] == "pat":
        await bot.say ("You did good! `" + bot.command_prefix + "pat <@user>`")
    elif ctx.message.content[7:] == "ping":
        await bot.say ("Play ping pong with me! `" + bot.command_prefix + "ping`")
    elif ctx.message.content[7:] == "wakeup":
        await bot.say ("WAKE ME UP INSIDE! Or wake up a friend with `" + bot.command_prefix + "wakeup <@user>`")
    elif ctx.message.content[7:] == "magicball" or ctx.message.content[7:] == "mb":
        await bot.say ("Ask the magician a question! :thinking: `" + bot.command_prefix + "magicball` or `" + bot.command_prefix + "mb`")
    elif ctx.message.content[7:] == "flip":
        await bot.say("Hyahh! Flip someone! `" + bot.command_prefix + "flip <@user>`")
    else:
        embed = discord.Embed(title='Commands!', description='Remember, the prefix is `' + bot.command_prefix + '`!', color=0x9B59B6).set_author(name="For more detailed help, do " + bot.command_prefix + "help <command>", icon_url ='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Info', value='`about`, `avatar`, `help`, `info`, `ping`, `request`', inline=False).add_field(name='Fun', value='`echo`, `flip`, `lewd`, `lood`, `magicball`, `say`, `shru`, `year`', inline=False).add_field(name='Faces', value='`lenny`, `nonowa`, `shrug`', inline=False).add_field(name='Action', value='`cuddle`, `hug`, `kill`, `kiss`, `pat`, `poke`, `wakeup`', inline=False).add_field(name='Mod', value='soon:tm:', inline=False).set_footer(text="Enjoy the bot! <3 | Total commands: 22")
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
        await bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` issued my `help` command in channel `' + ctx.message.channel.name + '` in  server `' + ctx.message.server.name + '`')

# The test command is for me to try new features
@bot.command(pass_context = True)
async def test(ctx):
    await bot.say("Uh... no test command here... *runs*")

# cog commands    
@bot.command()
async def load(extension_name : str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def reload(extension_name : str):
    try:
        bot.unload_extension(extension_name)
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} reloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))
    bot.run('token')
