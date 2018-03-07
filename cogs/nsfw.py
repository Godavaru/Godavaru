import discord
import aiohttp
import random
import json
from discord.ext import commands


class NSFW:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="<members>")
    @commands.bot_has_permissions(embed_links=True)
    async def fuck(self, ctx):
        """Feeling lewd? Why don't you go and fuck a person :eyes:
        Note: This command does include NSFW content, meaning it can only be used in NSFW marked channels. For a reference on how to set channels as NSFW, [here is a general idea of where the button usually is.](https://i.imgur.com/ZisyibJ.png)"""
        # IMPORTANT: Hey you! Yes you, scrolling through the source code. Be warned that these links contain NSFW gifs.
        # Visit the sites at your own risk.
        gifs = [
            "http://x.imagefapusercontent.com/u/TrickyLouse/3985842/42565623/Slow-Fuck-Hentai-GIF-TheHentaiWorld-6.gif",
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
        if len(ctx.message.mentions) == 0:
            return await ctx.send(":x: You can't fuck the air... well, you can try.")
        if not ctx.channel.is_nsfw():
            return await ctx.send(":x: Y-you lewdie! Go get a room!")
        msg = f"**{ctx.author.display_name}** is fucking **{(', '.join([m.display_name for m in ctx.message.mentions])).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1].display_name, ' and '+ctx.message.mentions[len(ctx.message.mentions)-1].display_name)}**!"
        for u in ctx.message.mentions:
            if u == ctx.author.display_name:
                msg = f'Oh, okay. Sure. I\'ll fuck you.'
        em = discord.Embed(
            description=":eggplant: " + msg,
            color=ctx.message.author.color)
        em.set_image(url=random.choice(gifs))
        em.set_footer(text="You lewdie o.o")
        await ctx.send(embed=em)

    @commands.command(aliases=["r34"])
    async def rule34(self, ctx, tag: str):
        """Search for an image on rule34!
        Note: To use this command, the channel must be NSFW."""
        if ctx.channel.is_nsfw():
            try:
                url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=' + tag
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        js = json.loads(await resp.text())
                non_loli = list(filter(lambda x: 'loli' not in x['tags'] and 'shota' not in x['tags'], js))
                if len(non_loli) == 0:
                    return await ctx.send(":warning: All results included loli/shota content; this search is invalid.")
                response = non_loli[random.randint(0, len(non_loli))]
                img = f"https://img.rule34.xxx/images/{response['directory']}/{response['image']}"
                tags = response['tags'].split(' ')
                em = discord.Embed(description=f'`{", ".join(tags)}`', colour=0xff0000)
                em.set_image(url=img)
                em.set_author(name='Found Image! Click me if it doesn\'t load!', url=img)
                await ctx.send(embed=em)
            except json.JSONDecodeError:
                await ctx.send(":x: No image found. Sorry :/")
        else:
            await ctx.send(":x: This is not an NSFW channel.")

    @commands.command()
    async def yandere(self, ctx, tag: str, rating: str = None):
        """Search for an image on yande.re!
        Note: To use this command, the channel must be NSFW."""
        rating = rating.lower() if rating else None
        if ctx.channel.is_nsfw():
            url = 'https://yande.re/post.json?tags=rating:' + (rating if rating in ['safe', 'questionable', 'explicit'] else 'safe') + '%20' + tag
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    js = await resp.json()
            if len(js) > 0:
                non_loli = list(filter(lambda x: 'loli' not in x['tags'] and 'shota' not in x['tags'] and 'deletethistag' not in x['tags'], js))
                if len(non_loli) == 0:
                    return await ctx.send(":warning: All results included loli/shota content; this search is invalid.")
                response = non_loli[random.randint(0, len(non_loli))]
                img = response['file_url']
                tags = response['tags'].split(' ')
                em = discord.Embed(description=f'**Rating:** {(rating if rating in ["safe", "questionable", "explicit"] else "safe")}\n`{", ".join(tags)}`', colour=0xff0000)
                em.set_image(url=img)
                em.set_author(name='Found Image! Click me if it doesn\'t load!', url=img)
                await ctx.send(embed=em)
            else:
                await ctx.send(":x: No image found. Sorry :/")
        elif rating == "safe" and not ctx.channel.is_nsfw():
            await ctx.send(":warning: Sorry! I know that this image is marked as `safe`, but yande.re sometimes returns lewd images in the safe rating. Please use an NSFW channel.")
        else:
            await ctx.send(":x: This is not an NSFW channel.")

def setup(bot):
    bot.add_cog(NSFW(bot))