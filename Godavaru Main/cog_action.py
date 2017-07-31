import discord
import random
import time
from discord.ext import commands

class Action():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def cuddle(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"cuddle", "")
        random.seed(time.time())
        var = int(random.random() * 10)
        
        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = '<:godavarublobhug:318227863646109696> Aww, are you lonely? I\'ll cuddle with you, **'+ctx.message.author.display_name+'**!'
            else:
                msg = '<:godavarublobhug:318227863646109696> **' + ctx.message.mentions[0].display_name + '** was cuddled by **' + ctx.message.author.display_name +'**!'

            img = ["./images/cuddlea.gif", "./images/cuddleb.gif", "./images/cuddlec.gif", "./images/cuddled.gif", "./images/cuddlee.gif", "./images/cuddlef.gif", "./images/cuddleg.gif", "./images/cuddleh.gif", "./images/cuddlei.gif", "./images/cuddlej.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def hug(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"hug", "")
        random.seed(time.time())
        var = int(random.random() * 10)
        
        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = ':hugging: Are you lonely, **'+ctx.message.mentions[0].display_name+'**? I\'ll hug you!'
            else:
                msg = ':hugging: **' + ctx.message.mentions[0].display_name + '** was hugged by **' + ctx.message.author.display_name +'**!'

            img = ["./images/huga.gif", "./images/hugb.gif", "./images/hugc.gif", "./images/hugd.gif", "./images/huge.gif", "./images/hugf.gif", "./images/hugg.gif", "./images/hugh.gif", "./images/hugi.gif", "./images/hugj.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def slap(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"slap", "")
        random.seed(time.time())
        var = int(random.random() * 9)

        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = ':raised_hand: This makes no sense... Oh well'
            else:
                msg = ':raised_hand: Hyaah! **' + ctx.message.author.display_name + '** has slapped **' + ctx.message.mentions[0].display_name + '**!'

            img = ["./images/slapa.gif", "./images/slapb.gif", "./images/slapc.gif", "./images/slapd.gif", "./images/slape.gif", "./images/slapf.gif", "./images/slapg.gif", "./images/slaph.gif", "./images/slapi.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def kiss(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"kiss", "")
        random.seed(time.time())
        var = int(random.random() * 11)

        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = ":kissing_heart: I don't think you can kiss yourself... I'll kiss you instead!"
            else:
                msg = ':kissing_heart: **' + ctx.message.mentions[0].display_name + '** was kissed by **' + ctx.message.author.display_name +'**!'

            img = ["./images/kissa.gif", "./images/kissb.gif", "./images/kissc.gif", "./images/kissd.gif", "./images/kisse.gif", "./images/kissf.gif", "./images/kissg.gif", "./images/kissh.gif", "./images/kissi.gif", "./images/kissj.gif", "./images/kissk.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug
            
    @commands.command(pass_context = True)
    async def pat(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"pat", "")
        random.seed(time.time())
        var = int(random.random() * 11)
            
        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'
            else:
                msg = '<:patemote:318592885090156544> **' + ctx.message.mentions[0].display_name + '** was pat by **' + ctx.message.author.display_name + '**!'
            
            img = ["./images/pata.gif", "./images/patb.gif", "./images/patc.gif", "./images/patd.gif", "./images/pate.gif", "./images/patf.gif", "./images/patg.gif", "./images/path.gif", "./images/pati.gif", "./images/patj.gif", "./images/patk.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def poke(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"poke", "")
        random.seed(time.time())
        var = int(random.random() * 10)

        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = ":eyes: You can't poke nothing! I'll poke you instead!"
            else:
                msg = ':eyes: **' + ctx.message.mentions[0].display_name + '** was poked by **' + ctx.message.author.display_name +'**!'
        
            img = ["./images/pokea.gif", "./images/pokeb.gif", "./images/pokec.gif", "./images/poked.gif", "./images/pokee.gif", "./images/pokef.gif", "./images/pokeg.gif", "./images/pokeh.gif", "./images/pokei.gif", "./images/pokej.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context = True)
    async def wakeup(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"wakeup", "")
        random.seed(time.time())
        var = int(random.random() * 8)

        if args == "" or len(ctx.message.mentions) == 0:
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = '<:morning:319631823766552597> What are you trying to wake up? Well, you do you I guess.'
            else:
                msg = '<:morning:319631823766552597> **' + ctx.message.mentions[0].display_name + '**, rise and shine honey! **' + ctx.message.author.display_name + '** wants you to wake up!'

            img = ["./images/wakeupa.gif", "./images/wakeupb.gif", "./images/wakeupc.gif", "./images/wakeupd.gif", "./images/wakeupe.gif", "./images/wakeupf.gif", "./images/wakeupg.gif", "./images/wakeuph.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context=True)
    async def sleep(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"sleep", "")
        random.seed(time.time())
        var = int(random.random() * 12)
        if len(ctx.message.mentions) == 0 or args == "":
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = "<:night:319631860512587776> Hmm. Telling yourself to sleep. Self-discipline. I like it. Go slep!1!!"
            else:
                msg = "<:night:319631860512587776> **"+ctx.message.author.display_name+"** is telling **"+ctx.message.mentions[0].display_name+"** to go to sleep!"

            img = ["./images/sleepa.gif", "./images/sleepb.gif", "./images/sleepc.gif", "./images/sleepd.gif", "./images/sleepe.gif", "./images/sleepf.gif", "./images/sleepg.gif", "./images/sleeph.gif", "./images/sleepi.gif", "./images/sleepj.gif", "./images/sleepk.gif", "./images/sleepl.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug
            
    @commands.command(pass_context = True)
    async def cry(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"cry", "")
        random.seed(time.time())
        var = int(random.random() * 11)

        if args == "" or len(ctx.message.mentions) == 0:
            msg = ':cry: **'+ctx.message.author.display_name+'** just started to cry!'
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                msg = ":cry: **" + ctx.message.author.display_name + "** just started to cry!"
            else:
                msg = ':cry: **' + ctx.message.mentions[0].display_name + '** just made **' + ctx.message.author.display_name + '** cry!'
                
            img = ["./images/crya.gif", "./images/cryb.gif", "./images/cryc.gif", "./images/cryd.gif", "./images/crye.gif", "./images/cryf.gif", "./images/cryg.gif", "./images/cryh.gif", "./images/cryi.gif", "./images/cryj.gif", "./images/cryk.gif"]
            await self.bot.send_file(ctx.message.channel, img[var], content=msg)
        else:
            await bot.say("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug

    @commands.command(pass_context=True)
    async def kill(self, ctx):
        args = ctx.message.content
        args = args.replace(self.bot.command_prefix+"kill", "")
        random.seed(time.time())
        var = int(random.random() * 10)
        
        if len(ctx.message.mentions) == 0 or args == "":
            await self.bot.say(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].id == ctx.message.author.id:
                await self.bot.say("Don't kill yourself! I love you!")
            elif ctx.message.mentions[0].id == ctx.message.server.me.id:
                await self.bot.say("You tried to kill me, but you realised I'm a bot. So I killed you instead.")
            else:
                killmsg = [ctx.message.mentions[0].mention+" was stabbed by "+ctx.message.author.mention, "You tried to kill "+ctx.message.mentions[0].mention+", but you got caught by the police :<", ctx.message.mentions[0].mention+" disintegrated.", "While trying to kill "+ctx.message.mentions[0].mention+", "+ctx.message.author.mention+" accidentally killed themselves.", ctx.message.mentions[0].mention+" drowned.", "Hahahaha nice try. You just tried to kill a cop. You're in jail now.", "While trying to kill "+ctx.message.mentions[0].mention+", you accidentally pinged b1nzy. Ouch.", "You pushed "+ctx.message.mentions[0].mention+" into a river with crocodiles.", "You made "+ctx.message.mentions[0].mention+" listen to KidzBop, so they bled out of their ears and died.", "Meh. I don't feel like helping a murder today. Try again."]
                await self.bot.send_message(ctx.message.channel, killmsg[var])

    @commands.command(pass_context = True)
    async def shrug(self, ctx):
        embed = discord.Embed(title='Welp', description='*shrugs*', color=ctx.message.author.color).set_image(url='https://i.imgur.com/TPyz6lH.gif')
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        
def setup(bot):
    bot.add_cog(Action(bot))
