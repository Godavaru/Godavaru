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
        var = int(random.random() * 12)
        
        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = '<:godavarublobhug:318227863646109696> Aww, are you lonely? I\'ll cuddle with you, '+ctx.message.author.display_name+'!'
        elif ctx.message.mentions[0] is not None:
            msg = '<:godavarublobhug:318227863646109696> **' + ctx.message.mentions[0].display_name + '** was cuddled by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[9:] == ""):
            msg = '<:godavarublobhug:318227863646109696> Aww, are you lonely? I\'ll cuddle with you, '+ctx.message.author.display_name+'!'

        if  (var == 0):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/87ml5C6JwBhBe/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 1):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/PqUvkkVr4Osgw/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 2):
            embed = discord.Embed(description=msg).set_image(url='http://gifrific.com/wp-content/uploads/2012/08/cat-cuddle-stuffed-animal.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 3):
            embed = discord.Embed(description=msg).set_image(url='http://i1207.photobucket.com/albums/bb480/Yumekichi11/Picture%2033/ht34t34t34_zpse40ba541.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 4):
            embed = discord.Embed(description=msg).set_image(url='http://38.media.tumblr.com/9e3f2c64ae935f4043a32d9e82187291/tumblr_mwd81e5V4W1socks4o1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 5):
            embed = discord.Embed(description=msg).set_image(url='http://pa1.narvii.com/5781/0fe4236473bcce8194b5aed3cf4c824f91da58bb_hq.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 6):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/51Q4oAg.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 7):
            embed = discord.Embed(description=msg).set_image(url='http://data.whicdn.com/images/244674930/large.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 8):
            embed = discord.Embed(description=msg).set_image(url='http://data.whicdn.com/images/45672340/large.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 9):
            embed = discord.Embed(description=msg).set_image(url='http://img4.wikia.nocookie.net/__cb20130302231719/adventuretimewithfinnandjake/images/1/15/Tumblr_m066xoISk41r6owqs.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 10):
            embed = discord.Embed(description=msg).set_image(url='http://pa1.narvii.com/5824/92a2818ade550f45782d302b8707a6046bfdf652_hq.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 11):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/b601854c659e4327f103e157306c6237/tumblr_opn01yPHjK1wpo4m9o1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def hug(self, ctx, member : discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 13)
        
        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ':hugging: Aww, are you lonely? Have a hug, '+ctx.message.author.display_name+'!'
        elif ctx.message.mentions[0] is not None:
            msg = ':hugging: **' + ctx.message.mentions[0].display_name + '** was hugged by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[5:] == ""):
            msg = ':hugging: Aww, are you lonely? Have a hug, '+ctx.message.author.display_name+'!'
            
        if  (var == 0):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/64tEiNj.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 1):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/kvTu3tb.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 2):
            embed = discord.Embed(description=msg).set_image(url='https://media3.giphy.com/media/lXiRKBj0SAA0EWvbG/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var ==3):
            embed = discord.Embed(description=msg).set_image(url='http://cdn.smosh.com/sites/default/files/ftpuploads/bloguploads/0413/epic-hugs-monsters-inc.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 4):
            embed = discord.Embed(description=msg).set_image(url='https://media1.giphy.com/media/BXrwTdoho6hkQ/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 5):
            embed = discord.Embed(description=msg).set_image(url='https://media0.giphy.com/media/VGACXbkf0AeGs/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 6):
            embed = discord.Embed(description=msg).set_image(url='https://media1.giphy.com/media/mLYVrZR44EcU0/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 7):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/81kpBJDlwPi2Q/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 8):
            embed = discord.Embed(description=msg).set_image(url='http://pa1.narvii.com/5940/c29578ee808fc55992dedae89ac46d75d9e9f84d_hq.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 9):
            embed = discord.Embed(description=msg).set_image(url='http://i1004.photobucket.com/albums/af169/mutopis/SodokoMakoyurihug_zpsd86d47a5.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 10):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/Bg3PXi0Ka1ZWE/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 11):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/21f89b12419bda49ce8ee33d50f01f85/tumblr_o5u9l1rBqg1ttmhcxo1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 12):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/uVVAPGE.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def kiss(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 14)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ":kissing_heart: I don't think you can kiss yourself... I'll kiss you instead!"
        elif ctx.message.mentions[0] is not None:
            msg = ':kissing_heart: **' + ctx.message.mentions[0].display_name + '** was kissed by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[5:] == ""):
            msg = ":kissing_heart: I don't think you can kiss yourself... I'll kiss you instead!"
        
        if  (var == 0):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/nxhdQuJ.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 1):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/2mFkqXh.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 2):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/71lpaeH.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 3):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/ZUc3T7U.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 4):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/Lce2Zw2.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 5):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/dpHduEL.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 6):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/YfqU78J.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 7):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/uKxYHBx.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 8):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/gvn3TYx.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 9):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/w58KuGF.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 10):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/6F1blBK.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 11):
            embed = discord.Embed(description=msg).set_image(url='https://cdn.discordapp.com/attachments/291978890237313024/310061819836235779/Kiss3.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 12):
            embed = discord.Embed(description=msg).set_image(url='https://cdn.discordapp.com/attachments/291978890237313024/310061848349114369/Kiss2.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 13):
            embed = discord.Embed(description=msg).set_image(url='https://cdn.discordapp.com/attachments/291978890237313024/310061884399157259/Kiss1.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
            
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

    @commands.command(pass_context = True)
    async def pat(self, ctx, member : discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 12)
        
        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'
        elif ctx.message.mentions[0] is not None:
            msg = '<:patemote:318592885090156544> **' + ctx.message.mentions[0].display_name + '** was pat by **' + ctx.message.author.display_name + '**!'
        if(ctx.message.content[9:] == ""):
            msg = '<:patemote:318592885090156544> I guess I can pat you if nobody else will.'
            
        if (var == 0):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/50ae3b3525c02603b15e5c4b51d7490b/tumblr_ngihi38QXY1qks4szo1_r3_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 1):
            embed = discord.Embed(description=msg).set_image(url='https://gimmebar-assets.s3.amazonaws.com/508a17c6e1e33.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 2):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/cc0451847fa08b202f4bd7a1cb9bd327/tumblr_o2js2xhINq1tydz8to1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 3):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/f95f14437809dfec8057b2bd525e6b4a/tumblr_omvkl2SzeK1ql0375o1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 4):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/X9MUeQelKifU4/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 5):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/18e1fdcde34edf0cf03c588162fbd0ea/tumblr_npeccq4y3H1rzk6edo1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 6):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/iGZJRDVEM6iOc/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 7):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/2d61aa2fd9286f5670fbb17b6e56475f/tumblr_o4ufimpBNt1tydz8to1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 8):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/5f971a365d815655803dcaea590df074/tumblr_od76a3qX4i1s9gdrpo1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 9):
            embed = discord.Embed(description=msg).set_image(url='https://s-media-cache-ak0.pinimg.com/originals/33/19/75/3319753afeb1eab2e4d2dbe0ac496167.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 10):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/472da02d9544dd3d26fdf6afb9995ee3/tumblr_ogj6hz2XhG1ukty6zo1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 11):
            embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/c92bd1a98d593c1b7d98493f96e1d09d/tumblr_nj4r4iKOa91tuglmxo4_400.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def poke(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 11)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = ":eyes: Poking yourself is no fun! I'll poke you myself :3"
        elif ctx.message.mentions[0] is not None:
            msg = ':eyes: **' + ctx.message.mentions[0].display_name + '** was poked by **' + ctx.message.author.display_name +'**!'
        if(ctx.message.content[9:] == ""):
            msg = ":eyes: You can't poke nothing! I'll poke you instead!"
        
        if  (var == 0):
            embed = discord.Embed(description=msg).set_image(url='http://fc06.deviantart.net/fs71/f/2012/007/3/e/minako_poke_by_endless_summer181-d4llj28.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 1):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/ovbDDmY4Kphtu/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 2):
            embed = discord.Embed(description=msg).set_image(url='https://31.media.tumblr.com/7c8457fd628f55b768ac2c6232a893cf/tumblr_mnycv2sm2f1r43mgoo1_500.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 3):
            embed = discord.Embed(description=msg).set_image(url='http://i.imgur.com/oyIXHxY.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 4):
            embed = discord.Embed(description=msg).set_image(url='http://fanaru.com/sword-art-online/image/244663-sword-art-online-poke-poke.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 5):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/WvVzZ9mCyMjsc/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 6):
            embed = discord.Embed(description=msg).set_image(url='https://media.tenor.co/images/6882df36a5ee12e9464549eb62730655/tenor.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 7):
            embed = discord.Embed(description=msg).set_image(url='http://orig12.deviantart.net/d4e5/f/2016/342/7/a/tickle_poke_by_otakuangelx-d9vflfu.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 8):
            embed = discord.Embed(description=msg).set_image(url='https://s-media-cache-ak0.pinimg.com/originals/ec/d5/db/ecd5db48f5bdfb9b67f86f2094554839.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 9):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/omTtzUFX8mf4s/giphy.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif  (var == 10):
            embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/VTIF0AivyNoL6/source.gif')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def wakeup(self, ctx, member: discord.Member = None):
        random.seed(time.time())
        var = int(random.random() * 11)

        if (member is None or ctx.message.mentions[0].id == ctx.message.author.id):
            msg = "<:GoodMorning:270672240973053962> You can't wake yourself up... aren't you already awake? Ah well <3"
        elif ctx.message.mentions[0] is not None:
            msg = '<:GoodMorning:270672240973053962> **' + ctx.message.mentions[0].display_name + '**, rise and shine honey! **' + ctx.message.author.display_name + '** wants you to wake up!'
        if ctx.message.content[11:] == "":
            msg = '<:GoodMorning:270672240973053962> What are you trying to wake up? Well, you do you I guess.'

        if (var == 0):
           embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/JGrhaJzR1eMoM/giphy.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 1):
           embed = discord.Embed(description=msg).set_image(url='http://data.whicdn.com/images/16713172/original.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 2):
           embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/oav6WEAGsFIFG/giphy.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 3):
           embed = discord.Embed(description=msg).set_image(url='http://orig12.deviantart.net/2db7/f/2012/287/4/a/wake_up__sugu__by_diemdenis-d5hs3gu.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 4):
           embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/f58ad175ae8b1cf095f712b70cbb7eb5/tumblr_oegjq4J3761tydz8to1_500.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 5):
           embed = discord.Embed(description=msg).set_image(url='https://s-media-cache-ak0.pinimg.com/originals/97/bd/f2/97bdf2fc6e043b602153bc282e237ded.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 6):
           embed = discord.Embed(description=msg).set_image(url='http://31.media.tumblr.com/86cc50bc61f7f49a228525af3985897a/tumblr_nh04bnIe0c1r37arko1_500.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 7):
           embed = discord.Embed(description=msg).set_image(url='http://pa1.narvii.com/5659/2b2d65dcbf9cf3ba16eb7037f64f7a82bdbb2f6f_hq.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 8):
           embed = discord.Embed(description=msg).set_image(url='https://68.media.tumblr.com/cd7c02510749b14581a47296f9019222/tumblr_nk2qpsplXb1uo1owvo1_500.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 9):
           embed = discord.Embed(description=msg).set_image(url='http://data.whicdn.com/images/20582147/large.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif (var == 10):
           embed = discord.Embed(description=msg).set_image(url='https://media.giphy.com/media/yxFTNmdbcLmes/giphy.gif')
           await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
           
def setup(bot):
    bot.add_cog(Action(bot))
