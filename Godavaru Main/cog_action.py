import discord
import random
import time
from discord.ext import commands

class Action():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def cuddle(self, ctx, member : discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 10)
        
        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = '<:godavarublobhug:318227863646109696> Aww, are you lonely? I\'ll cuddle with you, **'+ctx.message.author.display_name+'**!'
        elif ctx.message.mentions[0] is not None:
            msg = '<:godavarublobhug:318227863646109696> **' + ctx.message.mentions[0].display_name + '** was cuddled by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[9:] == ""):
            msg = '<:godavarublobhug:318227863646109696> Aww, are you lonely? I\'ll cuddle with you, **'+ctx.message.author.display_name+'**!'

        if  (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/cuddlea.gif', content=msg)
        elif  (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/cuddleb.gif', content=msg)
        elif  (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/cuddlec.gif', content=msg)
        elif  (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/cuddled.gif', content=msg)
        elif  (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/cuddlee.gif', content=msg)
        elif  (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/cuddlef.gif', content=msg)
        elif  (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/cuddleg.gif', content=msg)
        elif  (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/cuddleh.gif', content=msg)
        elif  (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/cuddlei.gif', content=msg)
        elif  (var == 9):
            await self.bot.send_file(ctx.message.channel, './images/cuddlej.gif', content=msg)
        

    @commands.command(pass_context = True)
    async def hug(self, ctx, member : discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 10)
        
        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ':hugging: Aww, are you lonely? Have a hug, **'+ctx.message.author.display_name+'**!'
        elif ctx.message.mentions[0] is not None:
            msg = ':hugging: **' + ctx.message.mentions[0].display_name + '** was hugged by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[6:] == ""):
            msg = ':hugging: Aww, are you lonely? Have a hug, **'+ctx.message.author.display_name+'**!'
            
        if  (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/huga.gif', content=msg)
        elif  (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/hugb.gif', content=msg)
        elif  (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/hugc.gif', content=msg)
        elif  (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/hugd.gif', content=msg)
        elif  (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/huge.gif', content=msg)
        elif  (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/hugf.gif', content=msg)
        elif  (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/hugg.gif', content=msg)
        elif  (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/hugh.gif', content=msg)
        elif  (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/hugi.gif', content=msg)
        elif  (var == 9):
            await self.bot.send_file(ctx.message.channel, './images/hugj.gif', content=msg)

    @commands.command(pass_context = True)
    async def slap(self, ctx, member : discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 9)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = '*slaps you* :eyes:'
        elif ctx.message.mentions[0] is not None:
            msg = ':raised_hand: Hyaah! **' + ctx.message.author.display_name + '** has slapped **' + ctx.message.mentions[0].display_name + '**!'
        if(ctx.message.content[6:] == ""):
            msg = '*slaps you* :eyes:'

        if (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/slapa.gif', content=msg)
        elif (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/slapb.gif', content=msg)
        elif (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/slapc.gif', content=msg)
        elif (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/slapd.gif', content=msg)
        elif (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/slape.gif', content=msg)
        elif (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/slapf.gif', content=msg)
        elif (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/slapg.gif', content=msg)
        elif (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/slaph.gif', content=msg)
        elif (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/slapi.gif', content=msg)

    @commands.command(pass_context = True)
    async def kiss(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 11)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ":kissing_heart: I don't think you can kiss yourself... I'll kiss you instead!"
        elif ctx.message.mentions[0] is not None:
            msg = ':kissing_heart: **' + ctx.message.mentions[0].display_name + '** was kissed by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[5:] == ""):
            msg = ":kissing_heart: I don't think you can kiss yourself... I'll kiss you instead!"
        
        if (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/kissa.gif', content=msg)
        elif (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/kissb.gif', content=msg)
        elif (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/kissc.gif', content=msg)
        elif (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/kissd.gif', content=msg)
        elif (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/kisse.gif', content=msg)
        elif (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/kissf.gif', content=msg)
        elif (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/kissg.gif', content=msg)
        elif (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/kissh.gif', content=msg)
        elif (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/kissi.gif', content=msg)
        elif (var == 9):
            await self.bot.send_file(ctx.message.channel, './images/kissj.gif', content=msg)
        elif (var == 10):
            await self.bot.send_file(ctx.message.channel, './images/kissk.gif', content=msg)
            
    @commands.command(pass_context = True)
    async def pat(self, ctx, member : discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 11)
        
        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'
        elif ctx.message.mentions[0] is not None:
            msg = '<:patemote:318592885090156544> **' + ctx.message.mentions[0].display_name + '** was pat by **' + ctx.message.author.display_name + '**!'
        if(ctx.message.content[9:] == ""):
            msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'

        if (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/pata.gif', content=msg)
        elif (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/patb.gif', content=msg)
        elif (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/patc.gif', content=msg)
        elif (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/patd.gif', content=msg)
        elif (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/pate.gif', content=msg)
        elif (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/patf.gif', content=msg)
        elif (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/patg.gif', content=msg)
        elif (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/path.gif', content=msg)
        elif (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/pati.gif', content=msg)
        elif (var == 9):
            await self.bot.send_file(ctx.message.channel, './images/patj.gif', content=msg)
        elif (var == 10):
            await self.bot.send_file(ctx.message.channel, './images/patk.gif', content=msg)

    @commands.command(pass_context = True)
    async def poke(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 10)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ":eyes: Poking yourself is no fun! I'll poke you myself :3"
        elif ctx.message.mentions[0] is not None:
            msg = ':eyes: **' + ctx.message.mentions[0].display_name + '** was poked by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[9:] == ""):
            msg = ":eyes: You can't poke nothing! I'll poke you instead!"
        
        if (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/pokea.gif', content=msg)
        elif (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/pokeb.gif', content=msg)
        elif (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/pokec.gif', content=msg)
        elif (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/poked.gif', content=msg)
        elif (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/pokee.gif', content=msg)
        elif (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/pokef.gif', content=msg)
        elif (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/pokeg.gif', content=msg)
        elif (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/pokeh.gif', content=msg)
        elif (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/pokei.gif', content=msg)
        elif (var == 9):
            await self.bot.send_file(ctx.message.channel, './images/pokej.gif', content=msg)
        

    @commands.command(pass_context = True)
    async def wakeup(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 8)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = "<:morning:319631823766552597> You can't wake yourself up... aren't you already awake? Ah well <3"
        elif ctx.message.mentions[0] is not None:
            msg = '<:morning:319631823766552597> **' + ctx.message.mentions[0].display_name + '**, rise and shine honey! **' + ctx.message.author.display_name + '** wants you to wake up!'
        if ctx.message.content[11:] == "":
            msg = '<:morning:319631823766552597> What are you trying to wake up? Well, you do you I guess.'

        if (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/wakeupa.gif', content=msg)
        elif (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/wakeupb.gif', content=msg)
        elif (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/wakeupc.gif', content=msg)
        elif (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/wakeupd.gif', content=msg)
        elif (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/wakeupe.gif', content=msg)
        elif (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/wakeupf.gif', content=msg)
        elif (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/wakeupg.gif', content=msg)
        elif (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/wakeuph.gif', content=msg)

    @commands.command(pass_context = True)
    async def cry(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 11)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ":cry: **" + ctx.message.author.display_name + "** just started to cry!"
        elif ctx.message.mentions[0] is not None:
            msg = ':cry: **' + ctx.message.mentions[0].display_name + '** just made **' + ctx.message.author.display_name + '** cry!'
        if ctx.message.content[6:] == "":
            msg = ":cry: **" + ctx.message.author.display_name + "** just started to cry!"

        if (var == 0):
            await self.bot.send_file(ctx.message.channel, './images/crya.gif', content=msg)
        elif (var == 1):
            await self.bot.send_file(ctx.message.channel, './images/cryb.gif', content=msg)
        elif (var == 2):
            await self.bot.send_file(ctx.message.channel, './images/cryc.gif', content=msg)
        elif (var == 3):
            await self.bot.send_file(ctx.message.channel, './images/cryd.gif', content=msg)
        elif (var == 4):
            await self.bot.send_file(ctx.message.channel, './images/crye.gif', content=msg)
        elif (var == 5):
            await self.bot.send_file(ctx.message.channel, './images/cryf.gif', content=msg)
        elif (var == 6):
            await self.bot.send_file(ctx.message.channel, './images/cryg.gif', content=msg)
        elif (var == 7):
            await self.bot.send_file(ctx.message.channel, './images/cryh.gif', content=msg)
        elif (var == 8):
            await self.bot.send_file(ctx.message.channel, './images/cryi.gif', content=msg)
        elif (var == 9):
            await self.bot.send_file(ctx.message.channel, './images/cryj.gif', content=msg)
        elif (var == 10):
            await self.bot.send_file(ctx.message.channel, './images/cryk.gif', content=msg)

    @commands.command(pass_context = True)
    async def kill(self, ctx):
        random.seed(time.time())
        var = int(random.random() * 9)

        if len(ctx.message.mentions) == 0:
            await self.bot.say("I don't know who I'm going to kill!")
        elif ctx.message.mentions[0].id == ctx.message.author.id and ctx.message.mentions[0].id == '267207628965281792':
            await self.bot.say("Are you sure, master..?")
        elif ctx.message.mentions[0].id == '311810096336470017':
            await self.bot.say("DON'T YOU DARE TRY TO KILL ME! I'LL KILL YOU FIRST! :knife:")
        elif ctx.message.mentions[0].id == ctx.message.author.id:
            await self.bot.say("Why would you want me to kill you?")
        elif (var == 0):
            await self.bot.say(ctx.message.mentions[0].mention + ' "accidentally" fell in a ditch. RIP >:)')
        elif (var == 1):
            await self.bot.say("I just tackled " + ctx.message.mentions[0].mention + " and killed them accidentally... oops")
        elif (var == 2):
            await self.bot.say(ctx.message.mentions[0].mention + " died. Why are you looking at me? I don't know how... :fingers_crossed:")
        elif (var == 3):
            await self.bot.say("I poisoned the food of " + ctx.message.mentions[0].mention + ". This should be fun to watch!")
        elif (var == 4):
            await self.bot.say("Whoops, I just killed " + ctx.message.mentions[0].mention + " by taking their own hair and making a rope to tie around their neck... Please don't tell the cops...")
        elif (var == 5):
            await self.bot.say(":knife: stabby stab to you," + ctx.message.mentions[0].mention + "! :eyes:")
        elif (var == 6):
            await self.bot.say("I decided to be nice for once, so I ordered " + ctx.message.mentions[0].mention + ' some pizza. Little did I know that I was gonna bump into the pizza guy in town. I was carrying poison and I "accidentally" poisoned and killed ' + ctx.message.mentions[0].mention + "...")
        elif (var == 7):
            await self.bot.say("RIP to " + ctx.message.mentions[0].mention + ". I took over their account and made them tag b1nzy on Google Emoji >:)")
        elif (var == 8):
            await self.bot.say("LOL! I just killed " + ctx.message.mentions[0].mention + " by pressing this button! I could try it on you too, " + ctx.message.author.mention + " :eyes:")
        elif (var == 9):
            embed = discord.Embed(description=ctx.message.mentions[0].display_name + ', you deded. <3',color='member').set_image(url='https://cdn.discordapp.com/attachments/312256765104226304/316225947277983746/kms.gif')
            await bot.send_message(ctx.message.channel, conten=None, embed=embed)

    @commands.command(pass_context = True)
    async def shrug(self, ctx):
        embed = discord.Embed(title='Welp', description='*shrugs*', color=ctx.message.author.color).set_image(url='https://i.imgur.com/TPyz6lH.gif')
        await self.bot.send_message(ctx.message.channel, content = None, embed=embed)
        
def setup(bot):
    bot.add_cog(Action(bot))
