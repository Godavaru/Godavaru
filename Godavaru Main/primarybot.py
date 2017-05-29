# import
import discord
import asyncio
from discord.ext import commands
import random
import time

# client
bot = commands.Bot(command_prefix='--')
bot.remove_command("help")
ownerids = [
	'267207628965281792',
	'99965250052300800',
	'170991374445969408',
	'188663897279037440'
]

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
    elif ctx.message.content[7:] == "hug":
        await bot.say ("To hug a user, do `--hug <@user>`! :hugging:")
    elif ctx.message.content[7:] == "kiss":
        await bot.say ("Kiss me before I lose my mind!! `--kiss <@user>`")
    elif ctx.message.content[7:] =="poke":
        await bot.say ("Don't poke me! Poke someone else with `--poke <@user>`!")
    elif ctx.message.content[7:] =="cuddle":
        await bot.say ("<:godavarublobhug:318227863646109696> Cuddle someone with `--cuddle <@user>`")
    elif ctx.message.content[7:] == "nonowa":
        await bot.say ("Make a nonowa face! `--nonowa`")
    elif ctx.message.content[7:] == "pat":
        await bot.say ("You did good! `--pat <@user>`")
    else:
        embed = discord.Embed(title='Commands!', description='Remember, the prefix is `--`!', color=0x9B59B6).set_author(name="For more detailed help, do --help <command>", icon_url ='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Info', value='`about`, `help`, `request`', inline=False).add_field(name='Fun', value='`echo`, `lewd`, `lood`, `say`, `shru`, `year`', inline=False).add_field(name='Faces', value='`lenny`, `nonowa`, `shrug`', inline=False).add_field(name='Action', value='`cuddle`, `hug`, `kill`, `kiss`, `pat`, `poke`', inline=False).set_footer(text="Enjoy the bot! <3 | Total commands: 18")
        await bot.send_message(ctx.message.channel, content=None, embed=embed)



@bot.command(pass_context = True)
async def about(ctx):
    server_count = 0
    for server in bot.servers:
        server_count = server_count + 1
    if ctx.message.content[8:] == "credits":
        embed = discord.Embed(title='Credits!', description='Here are some very honorable mentions for the creation, support, and overall community of the bot!',color=0x9B59B6).add_field(name='First Donator',value='MrLar#8117').add_field(name='Developers',value='Desiree#3658, Instance#2513, Yuvira#7842, and Jonas B.#9089').set_footer(text='Hope you enjoy the bot!').set_thumbnail(url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    else:
        embed = discord.Embed(title='About Godavaru!', description = "Hello! My name is Godavaru! I am Desiree#3658's very first bot, very much in production still. I hope you enjoy the bot so far!", color=0x9B59B6).add_field(name='Version Number', value='0.3.1', inline=False).add_field(name='Servers', value=str(server_count)+ '\n\n[Invite me](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)\n[Patreon page](https://www.patreon.com/godavaru)', inline=False).set_footer(text="Made with love <3 | Do --about credits for credits!").set_thumbnail(url="https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png")
        await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context = True)
async def request(ctx):
    request_channel = discord.Object('316674935898636289')

    if ctx.message.content[13:] != "":
        await bot.send_message(request_channel, '**Request from ' + ctx.message.author.name + '#' + ctx.message.author.discriminator + ':** ' + ctx.message.content[10:])
        await bot.say ("Your request has been received! :slight_smile:")

    else:
        await bot.say ("Please specify something to request or make the request longer!")
        

@bot.command(pass_context = True)
async def year(ctx):
    await bot.say ("A year has:\n\n12 Months\n52 Weeks\n365 Days\n8760 Hours\n525600 Minutes\n3153600 Seconds\n\nAnd it only takes 1 minute to send " + ctx.message.author.mention + " nudes :3")


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
async def nonowa(ctx):
    await bot.say("のワの")
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

    if member.id not in ownerids:
        await bot.say("No changey my gamey :rage: (access denied)")
    else:
        await bot.change_presence(game=discord.Game(name='--help | ' + setGame))
        await bot.say("Set my playing status to `--help | " + setGame + "`!");


@bot.command(pass_context = True)
async def shutdown(ctx):
    member = ctx.message.author
    console = discord.Object('316688736089800715')
    
    if member.id not in ownerids:
        await bot.say("Y-you want me gone? That's just rude! (access denied)")
        await bot.send_message(console, '`' +  str(ctx.message.author) + '` tried to shut me down! :frowning:')
        
    else:
        await bot.say("I-I'm hurt! Ah well, I never loved you anyway! :broken_heart: :sob:")
        await bot.send_message(console, '`' + str(ctx.message.author) + '` successfully shutdown Godavaru!')
        raise SystemExit


@bot.command(pass_context = True)
async def owner(ctx):
    member = ctx.message.author

    if member.id not in ownerids:
        await bot.say("No need to be looking at owner commands :eyes: (access denied)")
    else:
        await bot.say("**Owner commands!**\n\n`--shutdown` - Shutdown the bot.\n`--game` - Set the bot's playing status\n`--serverlist` - List all servers the bot is in.")

	
@bot.command(pass_context = True)
async def echo(ctx):

    if ctx.message.content[7:] == "":
        await bot.say (":mega: I can't echo something that isn't specified!")

    else:
        await bot.say(':mega:' + ctx.message.content[6:])


@bot.command(pass_context = True)
async def kill(ctx):
    random.seed(time.time())
    var = int(random.random() * 9)
    
    if ctx.message.mentions[0].id == ctx.message.author.id and ctx.message.mentions[0].id == '267207628965281792':
        await bot.say("Are you sure, master..?")
    elif ctx.message.mentions[0].id == '311810096336470017':
        await bot.say("DON'T YOU DARE TRY TO KILL ME! I'LL KILL YOU FIRST! :knife:")
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
    elif (var == 4):
        await bot.say("Whoops, I just killed " + ctx.message.mentions[0].mention + " by taking their own hair and making a rope to tie around their neck... Please don't tell the cops...")
    elif (var == 5):
        await bot.say(":knife: stabby stab to you," + ctx.message.mentions[0].mention + "! :eyes:")
    elif (var == 6):
            await bot.say("I decided to be nice for once, so I ordered " + ctx.message.mentions[0].mention + ' some pizza. Little did I know that I was gonna bump into the pizza guy in town. I was carrying poison and I "accidentally" poisoned and killed ' + ctx.message.mentions[0].mention + "...")
    elif (var == 7):
        await bot.say("RIP to " + ctx.message.mentions[0].mention + ". I took over their account and made them tag b1nzy on Google Emoji >:)")
    elif (var == 8):
        await bot.say("LOL! I just killed " + ctx.message.mentions[0].mention + " by pressing this button! I could try it on you too, " + ctx.message.author.mention + " :eyes:")
    elif (var == 9):
        embed = discord.Embed(description=ctx.message.mentions[0].display_name + ', you deded. <3',color='member').set_image(url='https://cdn.discordapp.com/attachments/312256765104226304/316225947277983746/kms.gif')


@bot.command(pass_context = True)
async def serverlist(ctx):
    msg = '**Godavaru Server List**'
    channel = ctx.message.channel
    member = ctx.message.author
    for server in bot.servers:
        msg = msg + '\n`' + server.name + '` owned by `' + server.owner.name + '#' + server.owner.discriminator + '`'
    
    if member.id not in ownerids:
        await bot.say ("My mommy says giving strangers information is bad! (access denied)")
    else:
        await bot.send_message(channel, msg)


@bot.command(pass_context = True)
async def say(ctx):

    if ctx.message.content[6:] == "":
        await bot.say('Specify something for me to say!')

    else:
        await bot.say(ctx.message.content[6:])
        await bot.delete_message(ctx.message)


@bot.command(pass_context = True)
async def hug(ctx):
    random.seed(time.time())
    var = int(random.random() * 13)
	
    msg = ':hugging: **' + ctx.message.mentions[0].display_name + '** was hugged by **' + ctx.message.author.display_name +'**!'
    if  (ctx.message.mentions[0].id == ctx.message.author.id):
        msg = ':hugging: Aw, are you lonely? Have a hug!'
    
    if  (var == 0):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/64tEiNj.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 1):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/kvTu3tb.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 2):
        embed = discord.Embed(description=msg).set_image(url='https://media3.giphy.com/media/lXiRKBj0SAA0EWvbG/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var ==3):
        embed = discord.Embed(description=msg).set_image(url='http://cdn.smosh.com/sites/default/files/ftpuploads/bloguploads/0413/epic-hugs-monsters-inc.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 4):
        embed = discord.Embed(description=msg).set_image(url='https://media1.giphy.com/media/BXrwTdoho6hkQ/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 5):
        embed = discord.Embed(description=msg).set_image(url='https://media0.giphy.com/media/VGACXbkf0AeGs/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 6):
        embed = discord.Embed(description=msg).set_image(url='https://media1.giphy.com/media/mLYVrZR44EcU0/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 7):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/81kpBJDlwPi2Q/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 8):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/14tdcXZOONVCXm/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 9):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/jmwFZljh2QnkI/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 10):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/Bg3PXi0Ka1ZWE/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 11):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/21f89b12419bda49ce8ee33d50f01f85/tumblr_o5u9l1rBqg1ttmhcxo1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 12):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/uVVAPGE.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context = True)
async def kiss(ctx):
    random.seed(time.time())
    var = int(random.random() * 11)
	
    msg = ':kissing_heart: **' + ctx.message.mentions[0].display_name + '** was kissed by **' + ctx.message.author.display_name +'**!'
    if  (ctx.message.mentions[0].id == ctx.message.author.id):
        msg = ':kissing_heart: Are you that desperate for affection? Guess I have no choice then.'

    if  (var == 0):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/nxhdQuJ.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 1):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/2mFkqXh.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 2):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/71lpaeH.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 3):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/ZUc3T7U.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 4):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/Lce2Zw2.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 5):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/dpHduEL.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 6):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/YfqU78J.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 7):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/uKxYHBx.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 8):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/gvn3TYx.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 9):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/w58KuGF.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 10):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/6F1blBK.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context=True)
async def poke(ctx):
    random.seed(time.time())
    var = int(random.random() * 11)
	
    msg = ':eyes: **' + ctx.message.mentions[0].display_name + '** was poked by **' + ctx.message.author.display_name +'**!'
    if  (ctx.message.mentions[0].id == ctx.message.author.id):
        msg = ':eyes: I mean alright, if you really need someone to poke you.'

    if  (var == 0):
        embed = discord.Embed(description=msg).set_image(url='http://fc06.deviantart.net/fs71/f/2012/007/3/e/minako_poke_by_endless_summer181-d4llj28.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 1):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/ovbDDmY4Kphtu/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 2):
        embed = discord.Embed(description=msg).set_image(url='https://31.media.tumblr.com/7c8457fd628f55b768ac2c6232a893cf/tumblr_mnycv2sm2f1r43mgoo1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 3):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/oyIXHxY.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 4):
        embed = discord.Embed(description=msg).set_image(url='http://fanaru.com/sword-art-online/image/244663-sword-art-online-poke-poke.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 5):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/WvVzZ9mCyMjsc/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 6):
        embed = discord.Embed(description=msg).set_image(url='https://media.tenor.co/images/6882df36a5ee12e9464549eb62730655/tenor.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 7):
        embed = discord.Embed(description=msg).set_image(url='http://orig12.deviantart.net/d4e5/f/2016/342/7/a/tickle_poke_by_otakuangelx-d9vflfu.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 8):
        embed = discord.Embed(description=msg).set_image(url='https://s-media-cache-ak0.pinimg.com/originals/ec/d5/db/ecd5db48f5bdfb9b67f86f2094554839.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 9):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/omTtzUFX8mf4s/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 10):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/VTIF0AivyNoL6/source.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context = True)
async def cuddle(ctx):
    random.seed(time.time())
    var = int(random.random() * 11)
	
    msg = '<:godavarublobhug:318227863646109696> **' + ctx.message.mentions[0].display_name + '** was cuddled by **' + ctx.message.author.display_name +'**!'
    if  (ctx.message.mentions[0].id == ctx.message.author.id):
        msg = '<:godavarublobhug:318227863646109696> Aw, you want to cuddle with me?'

    if  (var == 0):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/87ml5C6JwBhBe/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 1):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/PqUvkkVr4Osgw/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 2):
        embed = discord.Embed(description=msg).set_image(url='http://gifrific.com/wp-content/uploads/2012/08/cat-cuddle-stuffed-animal.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 3):
        embed = discord.Embed(description=msg).set_image(url='http://i1207.photobucket.com/albums/bb480/Yumekichi11/Picture%2033/ht34t34t34_zpse40ba541.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 4):
        embed = discord.Embed(description=msg).set_image(url='http://38.media.tumblr.com/9e3f2c64ae935f4043a32d9e82187291/tumblr_mwd81e5V4W1socks4o1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 5):
        embed = discord.Embed(description=msg).set_image(url='http://pa1.narvii.com/5781/0fe4236473bcce8194b5aed3cf4c824f91da58bb_hq.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 6):
        embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/51Q4oAg.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 7):
        embed = discord.Embed(description=msg).set_image(url='http://data.whicdn.com/images/244674930/large.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 8):
        embed = discord.Embed(description=msg).set_image(url='http://data.whicdn.com/images/45672340/large.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 9):
        embed = discord.Embed(description=msg).set_image(url='http://img4.wikia.nocookie.net/__cb20130302231719/adventuretimewithfinnandjake/images/1/15/Tumblr_m066xoISk41r6owqs.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif  (var == 10):
        embed = discord.Embed(description=msg).set_image(url='http://pa1.narvii.com/5824/92a2818ade550f45782d302b8707a6046bfdf652_hq.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)


@bot.command(pass_context = True)
async def pat(ctx):
    random.seed(time.time())
    var = int(random.random() * 11)
	
    msg = '<:patemote:318592885090156544> **' + ctx.message.mentions[0].display_name + '** was pat by **' + ctx.message.author.display_name + '**!'
    if  (ctx.message.mentions[0].id == ctx.message.author.id):
        msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'

    if (var == 0):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/50ae3b3525c02603b15e5c4b51d7490b/tumblr_ngihi38QXY1qks4szo1_r3_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 1):
        embed = discord.Embed(description=msg).set_image(url='https://gimmebar-assets.s3.amazonaws.com/508a17c6e1e33.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 2):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/cc0451847fa08b202f4bd7a1cb9bd327/tumblr_o2js2xhINq1tydz8to1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 3):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/f95f14437809dfec8057b2bd525e6b4a/tumblr_omvkl2SzeK1ql0375o1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 4):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/X9MUeQelKifU4/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 5):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/18e1fdcde34edf0cf03c588162fbd0ea/tumblr_npeccq4y3H1rzk6edo1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 6):
        embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/iGZJRDVEM6iOc/giphy.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 7):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/2d61aa2fd9286f5670fbb17b6e56475f/tumblr_o4ufimpBNt1tydz8to1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 8):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/5f971a365d815655803dcaea590df074/tumblr_od76a3qX4i1s9gdrpo1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 9):
        embed = discord.Embed(description=msg).set_image(url='https://s-media-cache-ak0.pinimg.com/originals/33/19/75/3319753afeb1eab2e4d2dbe0ac496167.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
    elif (var == 10):
        embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/472da02d9544dd3d26fdf6afb9995ee3/tumblr_ogj6hz2XhG1ukty6zo1_500.gif')
        await bot.send_message(ctx.message.channel, content=None, embed=embed)
	

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


@bot.event
async def on_error(e):
    print("There was an error, see below")
    console = discord.Object('316688736089800715')
    await bot.send_message(console, "```\n" + e + "```")
# login and start bot
bot.run('bot token')


