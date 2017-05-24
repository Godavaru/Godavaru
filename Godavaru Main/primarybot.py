# import
import discord
import asyncio
from discord.ext import commands

# client
bot = commands.Bot(command_prefix='--')
bot.remove_command("help")
		
# when bot is ready
@bot.event
async def on_ready():
    print('Starting up bot:')
    print(bot.user.name)
    print(bot.user.id)
    print('=================')
    console = discord.Object('316688736089800715')
    await bot.send_message(console, 'Successfully started up Godavaru.')


@bot.command()
async def help():
    await bot.say("**Commands!**\n\n**Info**\n`--help`, `--about`, `--invite`, `--support`, `--request`\n\n**Fun**\n`--year`, `--lewd`, `--lood`, `--shru`\n\n**Faces**\n`--shrug`, `--lenny`")


@bot.command()
async def invite():
    await bot.say("Invite me at the following link! https://goo.gl/chLxM9")


@bot.command()
async def support():
    await bot.say("**Join the support guild!**\nFor help with the bot, join the support guild at https://discord.gg/ewvvKHM")


@bot.command()
async def year():
    await bot.say ("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send me nudes :3")


@bot.command()
async def lewd():
    await bot.say ("We need to go lewder, man. http://prntscr.com/fa7tiq")


@bot.command()
async def lood():
    await bot.say ("You're very lewd :eyes: http://prntscr.com/fa7ug0")


@bot.command()
async def shrug():
    await bot.say ("¯\_(ツ)_/¯")


@bot.command(pass_context = True)
async def say(ctx):
    await bot.say(ctx.message.content[6:])
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def request(ctx):
    request_channel = discord.Object('316674935898636289')

    if ctx.message.content[13:] != "":
        await bot.send_message(request_channel, '**Request from ' + ctx.message.author.name + '#' + ctx.message.author.discriminator + ':** ' + ctx.message.content[10:])
        await bot.say ("Your request has been sent to the developers! The owner will pm you if your suggestion has been implemented. :slight_smile:")

    else:
        await bot.say ("Please specify something to request or make the request longer!")


@bot.command()
async def lenny():
    await bot.say ("( ͡° ͜ʖ ͡°)")


@bot.command()
async def about():
    server_count = 0
    for server in bot.servers:
        server_count = server_count + 1
    await bot.say("**About Godavaru!**\nHello! My name is Godavaru! I am Desiree#3658's very first bot, very much in production still. I hope you enjoy the bot so far!\n\n**Bot Version**\nv0.1.1\n\n**Servers**\n" + str(server_count))


@bot.command(pass_context = True)
async def shru(ctx):
    member = ctx.message.author
   
    if member.id != "99965250052300800":
        await bot.say ("Who are you, Instance#2513? Messing up the spelling that bad smh >:(")

    else:
        await bot.say("Learn to spell, Paul. For real ;-;")


@bot.command(pass_context = True)
async def game(ctx, *, setGame: str):
    member = ctx.message.author
    
    if member.id != "267207628965281792" and member.id != "99965250052300800":
        await bot.say("No changey my gamey :rage: (access denied)")
        
    else:
        await bot.change_status(discord.Game(name="--help | " + setGame))
        await bot.say("Set my playing status to `" + setGame + "`!");



@bot.command(pass_context = True)
async def shutdown(ctx):
    member = ctx.message.author
        
    if member.id != "267207628965281792" and member.id != "99965250052300800":
        await bot.say("Y-you want me gone? That's just rude! (access denied)")
    else:
        await bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
        raise SystemExit


@bot.command(pass_context = True)
async def owner(ctx):
    member = ctx.message.author

    if member.id != "267207628965281792" and member.id != "99965250052300800":
        await bot.say("No need to be looking at owner commands :eyes: (access denied)")
    else:
        await bot.say("**Owner commands!**\n\n`--shutdown` - Shutdown the bot.\n`--files` - Obtain access to the bot's files.\n`--game` - Set the bot's playing status")

        
# server join
@bot.event
async def on_server_join(server):
    console = discord.Object('316688736089800715')
    await bot.send_message(console, ':tada: I joined the server `' + server.name + '`, owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')


# server leave
@bot.event
async def on_server_remove(server):
    console = discord.Object('316688736089800715')
    await bot.send_message(console, ':frowning: I left the server `' + server.name + '`, owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')


@bot.event
async def on_message(message):
    if message.author.bot == False:
        await bot.process_commands(message)
# login and start bot
bot.run('bot token')


