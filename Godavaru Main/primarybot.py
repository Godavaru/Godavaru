# import
import discord
import asyncio
from discord.ext import commands
import random
import time

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
    await bot.send_message(console, 'Successfully started up!')


@bot.command(pass_context = True)
async def help(ctx):

    if ctx.message.content[7:] == "echo":
        await bot.say ("Use `--echo <text>` to make me echo something!")
    elif ctx.message.content[7:] == "about":
        await bot.say ("Display the facts about me by doing `--about`!")
    elif ctx.message.content[7:] == "help":
        await bot.say ("Uh... really? just do `--help`...")
    elif ctx.message.content[7:] == "request":
        await bot.say ("Request something to add by doing `--request <suggestion>`! Make sure it's longer than three characters!")
    elif ctx.message.content[7:] == "kill":
        await bot.say ("Kill your worst enemies! ~~Or friends, whatever you wish.~~ Do `--kill <@user>`")
    elif ctx.message.content[7:] == "lewd":
        await bot.say ("What should we do? `--lewd`")
    elif ctx.message.content[7:] == "lood":
        await bot.say ("S-senpai! `--lood`")
    elif ctx.message.content[7:] == "say":
        await bot.say ("Make me say something by doing `--say <text>`")
    elif ctx.message.content[7:] == "shru":
        await bot.say ("I hope that was a spelling error... `--shru`")
    elif ctx.message.content[7:] == "year":
        await bot.say ("See my very first fun command! It's good I promise ( ͡° ͜ʖ ͡°) `--year`")
    elif ctx.message.content[7:] == "lenny":
        await bot.say ("Make a lenny face by doing `--lenny`!")
    elif ctx.message.content[7:] == "shrug":
        await bot.say ("Uhh... idk *shrugs* `--shrug`")
    else:
        embed = discord.Embed(title='Commands!', description='Remember, the prefix is `--`!', color=0x9B59B6).set_author(name="For more detailed help, do --help <command>", icon_url ='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Info', value='`about`, `help`, `request`', inline=False).add_field(name='Fun', value='`echo`, `kill`, `lewd`, `lood`, `say`, `shru`, `year`', inline=False).add_field(name='Faces', value='`lenny`, `shrug`', inline=False).set_footer(text="Enjoy the bot! <3")
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    

@bot.command(pass_context = True)
async def about(ctx):
    server_count = 0
    for server in bot.servers:
        server_count = server_count + 1
    embed = discord.Embed(title='About Godavaru!', description = "Hello! My name is Godavaru! I am Desiree#3658's very first bot, very much in production still. I hope you enjoy the bot so far!", color=0x9B59B6).add_field(name='Version Number', value='0.2.1', inline=False).add_field(name='Servers', value=str(server_count)+ '\n\n[Invite me](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)', inline=False).set_footer(text="Made with love <3").set_thumbnail(url="https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png")
    await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context = True)
async def request(ctx):
    request_channel = discord.Object('316674935898636289')

    if ctx.message.content[13:] != "":
        await bot.send_message(request_channel, '**Request from ' + ctx.message.author.name + '#' + ctx.message.author.discriminator + ':** ' + ctx.message.content[10:])
        await bot.say ("Your request has been recieved! :slight_smile:")

    else:
        await bot.say ("Please specify something to request or make the request longer!")
        

@bot.command()
async def year():
    await bot.say ("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send me nudes :3")


@bot.command(pass_context = True)
async def lewd(ctx):
    embed = discord.Embed(title='We must go lewder!', description=":eyes:").set_image(url="https://image.prntscr.com/image/4beb7e203f394913abfccc19154d994a.png")
    await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context = True)
async def lood(ctx):
    embed = discord.Embed(title='P-put it in me senpai...', description=':blush:').set_image(url="https://image.prntscr.com/image/8e9cad7c75d84e419a2c551c18c36427.png")
    await bot.send_message(ctx.message.channel, content=None, embed=embed)

   
@bot.command(pass_context = True)
async def shrug(ctx):
    await bot.say ("¯\_(ツ)_/¯")
    await bot.delete_message(ctx.message)


@bot.command(pass_context = True)
async def lenny(ctx):
    await bot.say ("( ͡° ͜ʖ ͡°)")
    await bot.delete_message(ctx.message)


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
        await bot.change_status(discord.Game(name='--help | ' + setGame))
        await bot.say("Set my playing status to `--help | " + setGame + "`!");


@bot.command(pass_context = True)
async def shutdown(ctx):
    member = ctx.message.author
    console = discord.Object('316688736089800715')
    
    if member.id != "267207628965281792" and member.id != "99965250052300800":
        await bot.say("Y-you want me gone? That's just rude! (access denied)")
        await bot.send_message(console, '`' +  str(ctx.message.author) + '` tried to shut me down! :frowning:')
        
    else:
        await bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
        await bot.send_message(console, '`' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
        raise SystemExit


@bot.command(pass_context = True)
async def owner(ctx):
    member = ctx.message.author

    if member.id != "267207628965281792" or member.id != "99965250052300800":
        await bot.say("**Owner commands!**\n\n`--shutdown` - Shutdown the bot.\n`--game` - Set the bot's playing status")
        
    else:
        await bot.say("No need to be looking at owner commands :eyes: (access denied)")


@bot.command(pass_context = True)
async def echo(ctx):

    if ctx.message.content[7:] == "":
        await bot.say (":mega: I can't echo something that isn't specified!")

    else:
        await bot.say(':mega:' + ctx.message.content[6:])



@bot.command(pass_context = True)
async def kill(ctx):
    random.seed(time.time())
    var = int(random.random() * 4)
    
    if ctx.message.mentions[0].id == ctx.message.author.id and ctx.message.mentions[0].id == '267207628965281792':
        await bot.say("Are you sure, master..?")
    elif ctx.message.mentions[0].id == ctx.message.author.id:
        await bot.say("Why would you want me to kill you?")
    elif (var == 0):
        await bot.say(ctx.message.mentions[0].mention + ' "accidentally" fell in a ditch. RIP >:)')
    elif (var == 1):
        await bot.say("I just tackled " + ctx.message.mentions[0].mention + " and killed them accidentally... oops")
    elif (var == 2):
        await bot.say(ctx.message.mentions[0].mention + " died. Why are you looking at me? I don't know how... :fingers_crossed:")
    elif (var == 3):
        await bot.say("I poisoned the food of " + ctx.message.mentions[0].mention + ". This should be fun to watch!")
    else:
        await bot.say("Whoops, I just killed " + ctx.message.mentions[0].mention + " by taking their own hair and making a rope to tie around their neck... Please don't tell the cops...")


@bot.command(pass_context = True)
async def say(ctx):

    if ctx.message.content[6:] == "":
        await bot.say('Specify something for me to say!')

    else:
        await bot.say(ctx.message.content[6:])
        await bot.delete_message(ctx.message)


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


