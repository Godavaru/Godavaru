import config
import random
from discord.ext import commands
from cogs.utils.tools import *
from cogs.utils import weeb


class Action:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def cuddle(self, ctx):
        """For when you just need to cuddle someone uwu"""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is cuddling **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'***cuddles with you***'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="cuddle"), name="cuddle.gif")
        await ctx.send(content=msg, file=discord.File("./images/cuddle.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def hug(self, ctx):
        """Give a person a big fat hug! Awww!"""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is hugging **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'***hugs*** Are you okay now, **{ctx.author.display_name}**?'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="hug"), name="hug.gif")
        await ctx.send(content=msg, file=discord.File("./images/hug.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def slap(self, ctx):
        """What the hell did you just say to me? I'm gonna slap you to the moon for that comment!"""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is slapping **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**Uh, okay. Sure. _slaps_**'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="slap"), name="slap.gif")
        await ctx.send(content=msg, file=discord.File("./images/slap.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def kiss(self, ctx):
        """Give that special someone a kiss! <3"""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is kissing **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'I\'ll kiss you! *kisses*'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="kiss"), name="kiss.gif")
        await ctx.send(content=msg, file=discord.File("./images/kiss.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def pat(self, ctx):
        """Send a pat over to a person or a few people. Sometimes a pat speaks words that words cannot.
        Or maybe I just really like pats so I endorse them. Whichever one it is."""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is patting **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'***pats you***'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="slap"), name="slap.gif")
        await ctx.send(content=msg, file=discord.File("./images/slap.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def poke(self, ctx):
        """Do you ever have a friend who just wont stop ignoring you? Just poke them. :eyes:"""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is poking **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'*pokes you* hi. *pokes more*'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="teehee"), name="tease.gif")
        await ctx.send(content=msg, file=discord.File("./images/tease.gif"))

    @commands.command(aliases=["teehee"], usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def tease(self, ctx):
        """Hehe. The command for when you want to be a little joker and tease someone."""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is teasing **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'*teases you* hehe'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="teehee"), name="tease.gif")
        await ctx.send(content=msg, file=discord.File("./images/tease.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def stare(self, ctx):
        """The command for when you have no clue what to say to someone, so you just stare..."""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is staring at **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**..."
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'***stares at you***'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="stare"), name="stare.gif")
        await ctx.send(content=msg, file=discord.File("./images/stare.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def wakeup(self, ctx):
        """A way to get your friends off of their lazy butts and wake up."""
        imgs = ["./images/wakeupa.gif", "./images/wakeupb.gif", "./images/wakeupc.gif", "./images/wakeupd.gif", "./images/wakeupe.gif", "./images/wakeupf.gif", "./images/wakeupg.gif", "./images/wakeuph.gif"]
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is slapping **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**Uh, okay. Sure. _slaps_**'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="slap"), name="slap.gif")
        await ctx.send(content=msg, file=discord.File(f"./images/{random.choice(imgs)}.gif"))

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(attach_files=True)
    async def sleep(self, ctx):
        """The literal opposite of wakeup. This is also based off of my best friend, Kitty#4867, who would always tell me to go to bed. Love ya, Kat! ~Desii"""
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is telling **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}** to sleep!"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**Self-discipline! I like it! Go sleep!**'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="sleep"), name="sleep.gif")
        await ctx.send(content=msg, file=discord.File("./images/sleep.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def cry(self, ctx):
        """When life gets at you and you just wanna let it all out."""
        if len(ctx.message.mentions) == 0:
            msg = f'**{ctx.author.display_name}** is crying!'
        else:
            msg = f"**{ctx.author.display_name}** is crying because of **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is crying!'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="cry"), name="cry.gif")
        await ctx.send(content=msg, file=discord.File("./images/cry.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def triggered(self, ctx):
        """**T R I G G E R E D**"""
        if len(ctx.message.mentions) == 0:
            msg = f'**{ctx.author.display_name}** is triggered! REEEEEEEEEEEEEE'
        else:
            msg = f"**{ctx.author.display_name}** is triggered because of **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is triggered! REEEEEEEEEEEEEE'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="triggered"), name="triggered.gif")
        await ctx.send(content=msg, file=discord.File("./images/triggered.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def think(self, ctx):
        """You ever think about stuff, man?"""
        if len(ctx.message.mentions) == 0:
            msg = f'**{ctx.author.display_name}** is thinking...'
        else:
            msg = f"**{ctx.author.display_name}** is thinking about **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**! o.o"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is thinking...'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="thinking"), name="thinking.gif")
        await ctx.send(content=msg, file=discord.File("./images/thinking.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def blush(self, ctx):
        """I-it's not like I like you, b-baka!"""
        if len(ctx.message.mentions) == 0:
            msg = f'**{ctx.author.display_name}** is blushing... Who made them blush?'
        else:
            msg = f"**{ctx.author.display_name}** is blushing because of **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**! o.o"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is blushing... Who made them blush?'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="blush"), name="blush.gif")
        await ctx.send(content=msg, file=discord.File("./images/blush.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def smile(self, ctx):
        """\uD83C\uDFB6 You make me smile like the sun, fall outta bed... \uD83C\uDFB6
        What? I wasn't singing!"""
        if len(ctx.message.mentions) == 0:
            msg = f'**{ctx.author.display_name}** is smiling.'
        else:
            msg = f"**{ctx.author.display_name}** is smiling at**{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**!"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is smiling.'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="smile"), name="smile.gif")
        await ctx.send(content=msg, file=discord.File("./images/smile.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def shrug(self, ctx):
        """When you have no idea what is going on."""
        if len(ctx.message.mentions) == 0:
            msg = f'***shrugs***'
        else:
            msg = f"**{ctx.author.display_name}** is shrugging at **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**!"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'***shrugs***'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="shrug"), name="shrug.gif")
        await ctx.send(content=msg, file=discord.File("./images/shrug.gif"))

    @commands.command(usage="[members]")
    @commands.bot_has_permissions(attach_files=True)
    async def confused(self, ctx):
        """When you still have no idea what is going on."""
        if len(ctx.message.mentions) == 0:
            msg = f'**{ctx.author.display_name}** is confused'
        else:
            msg = f"**{ctx.author.display_name}** is confused with **{(', '.join(ctx.message.mentions)).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1], ' and '+ctx.message.mentions[len(ctx.message.mentions)-1])}**!"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is confused'
        weeb.save_to_image(url=await weeb.request_image_as_gif(type="clagwimoth"), name="clagwimoth.gif")
        await ctx.send(content=msg, file=discord.File("./images/clagwimoth.gif"))

    @commands.command()
    async def kill(self, ctx, *, member: discord.Member):
        """Kill a user!
        Note this command is just for fun. Nobody died in the making of this command... well maybe. *runs*"""
        with open('killquotes.txt') as f:
            quotes = f.readlines()
        if ctx.author.id == member.id:
            return await ctx.send(":x: Don't kill yourself! You're loved!")
        if member.id == ctx.me.id:
            return await ctx.send(":x: Nice try. <3")
        await ctx.send(":knife: " + random.choice(quotes).format(member.display_name, ctx.author.display_name))
        
def setup(bot):
    bot.add_cog(Action(bot))

"""
                                    =================================
                                    VERSION 1.0 LEFTOVERS STARTS HERE
                                    =================================
                                    
    @commands.command()
    async def kill(self, ctx):
        ""\"Attempt to kill people. Has a chance of failing. Also, you may only kill one user at a time, so this command does not (and will never) have multi mention support.

        **Usage:** `g_kill <user>`

        **Permission:** User""\"

        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            killmsg = ["**"+ctx.message.mentions[0].display_name+"** was stabbed by **"+ctx.message.author.display_name+"**", "You tried to kill **"+ctx.message.mentions[0].display_name+"**, but you got caught by the police :<", "**"+ctx.message.mentions[0].display_name+"** disintegrated.", "While trying to kill **"+ctx.message.mentions[0].display_name+"**, **"+ctx.message.author.display_name+"** accidentally killed themselves.", "**"+ctx.message.mentions[0].display_name+"** drowned.", "Hahahaha nice try. You just tried to kill a cop. You're in jail now.", "While trying to kill **"+ctx.message.mentions[0].display_name+"**, you accidentally pinged b1nzy. Ouch.", "You pushed **"+ctx.message.mentions[0].display_name+"** into a river with crocodiles.", "You made **"+ctx.message.mentions[0].display_name+"** listen to KidzBop, so they bled out of their ears and died.", "Meh. I don't feel like helping a murder today. Try again.", "**"+ctx.message.mentions[0].display_name+"** was thrown into a pit of snakes.", "**"+ctx.message.author.display_name+"** threw **"+ctx.message.mentions[0].display_name+"** into a pit of snakes, but fell in as well.", "**"+ctx.message.mentions[0].display_name+"** was given the death sentence after **"+ctx.message.author.display_name+"** framed them for murder.", "**"+ctx.message.mentions[0].display_name+"** was forced to use Kotlin by **"+ctx.message.author.display_name+"**, so they died.", "**"+ctx.message.author.display_name+"** tried to kill someone, but found their way into Mantaro Hub and gave into the memes.", "**"+ctx.message.mentions[0].display_name+"** was killed by a sentient robot... Why are you looking at me? I didn't do it...", "**"+ctx.message.author.display_name+"** tried to kill someone and got away from the police. However, the FBI jailed them.", "You don't have a weapon. Oops. Was I supposed to bring it? I think I was...", "When **"+ctx.message.author.display_name+"** tried to kill **"+ctx.message.mentions[0].display_name+"**, they were disappointed to find they were already dead.", "**"+ctx.message.mentions[0].display_name+"** took an arrow to the knee! Well, actually it was a gunshot. And it was actually to the heart."]
            var = int(random.random() * len(killmsg))
            if ctx.message.mentions[0].id == ctx.message.author.id:
                await ctx.send("Don't kill yourself! I love you!")
            elif ctx.message.mentions[0].id == ctx.message.guild.me.id:
                await ctx.send("You tried to kill me, but you realised I'm a bot. So I killed you instead.")
            else:
                await ctx.send(killmsg[var])
        else:
            await ctx.send("An unexpected error occurred. Please report this to Desiree#3658 on the support guild, link found in g!about.") # just in case. You never know shrug
            
    
    @commands.command()
    async def dab(self, ctx):
        ""\"Dab on the haterz

        **Usage: `g_dab`

        **Permission:** User""\"
        apiUrl = self.base_url+"?type=dab&hidden=false&nsfw=false&filetype=gif"
        headers = {"Authorization": "Wolke "+config.weeb_token}
        r = requests.get(apiUrl, headers=headers)
        js = r.json()
        url = js['url']
        o = AppURLopener()
        d = o.open(url)
        data = d.read()
        with open("./images/dab.gif", "wb") as img:
            img.write(data)
            img.close()
        await ctx.send(file=discord.File("./images/dab.gif"), content=f"<:blobdab:353520064017858560> **{ctx.author.display_name}** is dabbing... I am disappointed.")

"""
