import config
import random
from discord.ext import commands
from cogs.utils.tools import *
from cogs.utils import weeb


class Action:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def cuddle(self, ctx, *members: str):
        """For when you just need to cuddle someone uwu"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is cuddling **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'***cuddles with you***'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="cuddle"), name="cuddle.gif")
        await ctx.send(content=msg, file=discord.File("./images/cuddle.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def hug(self, ctx, *members: str):
        """Give a person a big fat hug! Awww!"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is hugging **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'***hugs*** Are you okay now, **{ctx.author.display_name}**?'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="hug"), name="hug.gif")
        await ctx.send(content=msg, file=discord.File("./images/hug.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def slap(self, ctx, *members: str):
        """What the hell did you just say to me? I'm gonna slap you to the moon for that comment!"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is slapping **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**Uh, okay. Sure. _slaps_**'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="slap"), name="slap.gif")
        await ctx.send(content=msg, file=discord.File("./images/slap.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def kiss(self, ctx, *members: str):
        """Give that special someone a kiss! <3"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is kissing **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'I\'ll kiss you! *kisses*'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="kiss"), name="kiss.gif")
        await ctx.send(content=msg, file=discord.File("./images/kiss.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def pat(self, ctx, *members: str):
        """Send a pat over to a person or a few people. Sometimes a pat speaks words that words cannot.
        Or maybe I just really like pats so I endorse them. Whichever one it is."""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is patting **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'***pats you***'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="slap"), name="slap.gif")
        await ctx.send(content=msg, file=discord.File("./images/slap.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def poke(self, ctx):
        """Do you ever have a friend who just wont stop ignoring you? Just poke them. :eyes:

        **Usage:** `g_poke <user(s)>`

        **Permission:** User"""
        apiUrl = self.base_url+"?type=poke&hidden=false&nsfw=false&filetype=gif"
        headers = {"Authorization": "Wolke "+config.weeb_token}
        r = requests.get(apiUrl, headers=headers)
        js = r.json()
        url = js['url']
        
        if len(ctx.message.mentions) == 0:
            await ctx.send(":x: You must mention a user!")
        elif len(ctx.message.mentions) > 0:
            o = AppURLopener()
            d = o.open(url)
            data = d.read()
            with open("./images/poke.gif", "wb") as img:
                img.write(data)
                img.close()
            ments = ""
            for x in range(0, len(ctx.message.mentions)):
                if ctx.message.mentions[x].id == ctx.message.author.id:
                    msg = ":eyes: You can't poke nothing! I'll poke you instead!"
                    await ctx.send(file=discord.File("./images/poke.gif"), content=msg)
                    return
                if x == 0:
                    ments = ctx.message.mentions[x].display_name
                elif x == len(ctx.message.mentions) - 1:
                    if len(ctx.message.mentions) == 2:
                        ments = ments+" and "+ctx.message.mentions[x].display_name
                    else:
                        ments = ments+", and "+ctx.message.mentions[x].display_name
                else:
                    ments = ments+", "+ctx.message.mentions[x].display_name
            if len(ctx.message.mentions) == 1:
                pr = "was"
            else:
                pr = "were"
            msg = ':eyes: **' + ments + '** ' + pr + ' poked by **' + ctx.message.author.display_name +'**!'
            await ctx.send(file=discord.File("./images/poke.gif"), content=msg)

    @commands.command(aliases=["teehee"])
    @commands.bot_has_permissions(attach_files=True)
    async def tease(self, ctx, *members: str):
        """Hehe. The command for when you want to be a little joker and tease someone."""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is teasing **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'*teases you* hehe'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="teehee"), name="tease.gif")
        await ctx.send(content=msg, file=discord.File("./images/tease.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def stare(self, ctx, *members: str):
        """The command for when you have no clue what to say to someone, so you just stare..."""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is staring at **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**..."
        for u in l:
            if u == ctx.author.display_name:
                msg = f'***stares at you***'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="stare"), name="stare.gif")
        await ctx.send(content=msg, file=discord.File("./images/stare.gif"))
            
    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def wakeup(self, ctx, *members: str):
        """A way to get your friends off of their lazy butts and wake up."""
        imgs = ["./images/wakeupa.gif", "./images/wakeupb.gif", "./images/wakeupc.gif", "./images/wakeupd.gif", "./images/wakeupe.gif", "./images/wakeupf.gif", "./images/wakeupg.gif", "./images/wakeuph.gif"]
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is slapping **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**Uh, okay. Sure. _slaps_**'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="slap"), name="slap.gif")
        await ctx.send(content=msg, file=discord.File(f"./images/{random.choice(imgs)}.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def sleep(self, ctx, *members: str):
        """The literal opposite of wakeup. This is also based off of my best friend, Kitty#4867, who would always tell me to go to bed. Love ya, Kat! ~Desii"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            await ctx.send(":x: You must mention at least one user.")
            return
        msg = f"**{ctx.author.display_name}** is telling **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}** to sleep!"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**Self-discipline! I like it! Go sleep!**'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="sleep"), name="sleep.gif")
        await ctx.send(content=msg, file=discord.File("./images/sleep.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def cry(self, ctx, *members: str):
        """When life gets at you and you just wanna let it all out."""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'**{ctx.author.display_name}** is crying!'
        else:
            msg = f"**{ctx.author.display_name}** is crying because of **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is crying!'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="cry"), name="cry.gif")
        await ctx.send(content=msg, file=discord.File("./images/cry.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def triggered(self, ctx, *members: str):
        """**T R I G G E R E D**"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'**{ctx.author.display_name}** is triggered! REEEEEEEEEEEEEE'
        else:
            msg = f"**{ctx.author.display_name}** is triggered because of **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is triggered! REEEEEEEEEEEEEE'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="triggered"), name="triggered.gif")
        await ctx.send(content=msg, file=discord.File("./images/triggered.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def think(self, ctx, *members: str):
        """You ever think about stuff, man?"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'**{ctx.author.display_name}** is thinking...'
        else:
            msg = f"**{ctx.author.display_name}** is thinking about **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**! o.o"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is thinking...'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="thinking"), name="thinking.gif")
        await ctx.send(content=msg, file=discord.File("./images/thinking.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def blush(self, ctx, *members: str):
        """I-it's not like I like you, b-baka!"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'**{ctx.author.display_name}** is blushing... Who made them blush?'
        else:
            msg = f"**{ctx.author.display_name}** is blushing because of **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**! o.o"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is blushing... Who made them blush?'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="blush"), name="blush.gif")
        await ctx.send(content=msg, file=discord.File("./images/blush.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def smile(self, ctx, *members: str):
        """\uD83C\uDFB6 You make me smile like the sun, fall outta bed... \uD83C\uDFB6
        What? I wasn't singing!"""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'**{ctx.author.display_name}** is smiling.'
        else:
            msg = f"**{ctx.author.display_name}** is smiling at**{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**!"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is smiling.'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="smile"), name="smile.gif")
        await ctx.send(content=msg, file=discord.File("./images/smile.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def shrug(self, ctx, *members: str):
        """When you have no idea what is going on."""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'***shrugs***'
        else:
            msg = f"**{ctx.author.display_name}** is shrugging at **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**!"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'***shrugs***'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="shrug"), name="shrug.gif")
        await ctx.send(content=msg, file=discord.File("./images/shrug.gif"))

    @commands.command()
    @commands.bot_has_permissions(attach_files=True)
    async def confused(self, ctx, *members: str):
        """When you still have no idea what is going on."""
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            msg = f'**{ctx.author.display_name}** is confused'
        else:
            msg = f"**{ctx.author.display_name}** is confused with **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}**!"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'**{ctx.author.display_name}** is confused'
        weeb.save_to_image(url=weeb.request_image_as_gif(type="clagwimoth"), name="clagwimoth.gif")
        await ctx.send(content=msg, file=discord.File("./images/clagwimoth.gif"))

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def fuck(self, ctx, *members: str):
        """Feeling lewd? Why don't you go and fuck a person :eyes:
        Note: This command does include NSFW content, meaning it can only be used in NSFW marked channels. For a reference on how to set channels as NSFW, [here is a general idea of where the button usually is.](https://i.imgur.com/ZisyibJ.png)"""
        # IMPORTANT: Hey you! Yes you, scrolling through the source code. Be warned that these links contain NSFW gifs.
        # Visit the sites at your own risk.
        gifs = ["http://x.imagefapusercontent.com/u/TrickyLouse/3985842/42565623/Slow-Fuck-Hentai-GIF-TheHentaiWorld-6.gif",
                "http://www.hentairider.com/media/images/5/hentai-fuck-images/hentai-fuck-images-134125.gif",
                "https://media.tenor.com/images/965a2bf373b32091041e901ef0f247cb/tenor.gif",
                "https://s.smutty.com/media_smutty/e/v/i/l/b/evilbaroness-z9hrj-a6a24c.gif",
                "https://ii.yuki.la/1/10/86f3aec8549511d0ec67dceef1d8c8124e0e7f50bb442d70bed825cf1d1ff101.gif",
                "https://danbooru.donmai.us/data/__kanaya_azami_ukagaka_drawn_by_zee_zee_sub__b9442481a2d7fd6dcf3c74280822237e.gif",
                "https://danbooru.donmai.us/data/__little_boy_admiral_and_ooi_kantai_collection_drawn_by_hangaku__8e81bf57306a4fdf326da4214ef3aa35.gif",
                "https://danbooru.donmai.us/data/__admiral_and_murakumo_kantai_collection_drawn_by_hangaku__7e555705d880142de82bbac193ebc73d.gif",
                "https://danbooru.donmai.us/data/__okumura_haru_persona_and_persona_5_drawn_by_bard_bot__21850b2448462ce7d9a544c02a4ba7f3.gif",
                "https://danbooru.donmai.us/data/__hagikaze_kantai_collection_drawn_by_hangaku__e621e283aab8a39da57b6629779525c4.gif",
                "https://danbooru.donmai.us/data/__stocking_panty_stocking_with_garterbelt_drawn_by_phanpix__b5506ab4ddf63686df9492bd9cf79400.gif",
                "https://simg3.gelbooru.com/images/3a/1e/3a1e7fc0b758814be7363813588cc3aa.gif",
                "https://danbooru.donmai.us/data/__2627973__dae809c5f38fcfe532ef8f798eacae63.gif",
                "https://img.rule34.xxx/images/2393/1cb2ac9e280e2716c250e06c8c16a99e3f1b4b86.gif",
                "https://img.rule34.xxx/images/2393/8839cfc024213be28e2ef7b03e0fbf0a820ed635.gif",
                "https://78.media.tumblr.com/f97beead9fa9f26e8eafe7e47c2ab1c8/tumblr_oq824xOoqL1vpe4noo1_540.gif",
                "https://i.pinimg.com/originals/9f/63/b9/9f63b9fd7352d135d6b8623541117a16.gif",
                "https://i1.woh.to/2017/01/06/22_013e8567.gif",
                "https://i.pinimg.com/originals/a9/56/32/a956328e0f31b85158a5c08cd0aff798.gif",
                "http://www.tagstube.com/wp-content/uploads/cache-e21155888465eabf55d969bc601f08b2/2016/01/Anime-Hentai-Gif-3.gif",
                "http://www.tagstube.com/wp-content/uploads/cache-e21155888465eabf55d969bc601f08b2/2016/01/Anime-Hentai-Gif-4.gif",
                "https://angrygif.com/wp-content/uploads/2017/02/fd5d61e746e1dc4a41b872f4e388753f.gif"]
        l = []
        for m in members:
            if m.startswith('<@') and m.endswith('>'):
                mid = m.replace('<@!', '').replace('<@', '').replace('>', '')
                try:
                    mem = ctx.guild.get_member(int(mid))
                    if mem is None or mem.display_name in l:
                        continue
                    else:
                        l.append(ctx.guild.get_member(int(mid)).display_name)
                except:
                    continue
        if len(l) == 0:
            return await ctx.send(":x: You can't fuck the air... well, you can try.")
        if not ctx.channel.is_nsfw():
            return await ctx.send(":x: Y-you lewdie! Go get a room!")
        msg = f"**{ctx.author.display_name}** is fucking **{(', '.join(l)).replace(', '+l[len(l)-1], ' and '+l[len(l)-1])}** to sleep!"
        for u in l:
            if u == ctx.author.display_name:
                msg = f'Oh, okay. Sure. I\'ll fuck you.'
        em = discord.Embed(
            description=":eggplant: " + msg,
            color=ctx.message.author.color)
        em.set_image(url=random.choice(gifs))
        em.set_footer(text="You lewdie o.o")
        await ctx.send(embed=em)
        
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
