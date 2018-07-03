import discord
import random
import json
from discord.ext import commands
from .utils import checks
from .utils.tools import resolve_emoji
from .assets import gifs


class NSFW:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="<members>")
    @checks.is_nsfw()
    @commands.bot_has_permissions(embed_links=True)
    async def fuck(self, ctx):
        """Feeling lewd? Why don't you go and fuck a person :eyes:
        Note: This command does include NSFW content, meaning it can only be used in NSFW marked channels. For a reference on how to set channels as NSFW, [here is a general idea of where the button usually is.](https://i.imgur.com/ZisyibJ.png)"""
        if len(ctx.message.mentions) == 0:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You can't fuck the air... well, you can try.")
        msg = f"**{ctx.author.display_name}** is fucking **{(', '.join([m.display_name for m in ctx.message.mentions])).replace(', '+ctx.message.mentions[len(ctx.message.mentions)-1].display_name, ' and '+ctx.message.mentions[len(ctx.message.mentions)-1].display_name)}**!"
        if ctx.author in ctx.message.mentions:
            msg = 'Oh, okay. Sure. I\'ll fuck you.'
        em = discord.Embed(
            description=":eggplant: " + msg,
            color=ctx.message.author.color)
        em.set_image(url=random.choice(gifs.fuck))
        em.set_footer(text="You lewdie o.o")
        await ctx.send(embed=em)

    @commands.command(aliases=["r34"])
    @checks.is_nsfw()
    async def rule34(self, ctx, tag: str):
        """Search for an image on rule34!
        Note: To use this command, the channel must be NSFW."""
        try:
            url = 'https://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=' + tag
            async with self.bot.session.get(url) as resp:
                js = json.loads(await resp.text())
            non_loli = list(filter(lambda x: 'loli' not in x['tags'] and 'shota' not in x['tags'], js))
            if len(non_loli) == 0:
                return await ctx.send(resolve_emoji('WARN', ctx) + " All results included loli/shota content; this search is invalid.")
            response = non_loli[random.randint(0, len(non_loli) - 1)]
            img = f"https://img.rule34.xxx/images/{response['directory']}/{response['image']}"
            tags = ', '.join(response['tags'].split(' '))
            safe = "`" + tags + "`" if len(tags) < 5000 else ("[Click me for the tags](" + await self.bot.post_to_haste(tags) + ')')
            em = discord.Embed(
                description=f'{safe}',
                colour=0xff0000)
            em.set_image(url=img)
            em.set_author(name='Found Image! Click me if it doesn\'t load!', url=img)
            await ctx.send(embed=em)
        except json.JSONDecodeError:
            await ctx.send(resolve_emoji('ERROR', ctx) + " No image found. Sorry :/")

    @commands.command()
    async def yandere(self, ctx, tag: str, rating: str = None):
        """Search for an image on yande.re!
        Note: To use this command, the channel must be NSFW."""
        rating = rating.lower() if rating else None
        if ctx.channel.is_nsfw():
            url = 'https://yande.re/post.json?tags=rating:' + (
                rating if rating in ['safe', 'questionable', 'explicit'] else 'safe') + '%20' + tag
            async with self.bot.session.get(url) as resp:
                js = await resp.json()
            if len(js) > 0:
                non_loli = list(filter(
                    lambda x: 'loli' not in x['tags'] and 'shota' not in x['tags'] and 'deletethistag' not in x['tags'],
                    js))
                if len(non_loli) == 0:
                    return await ctx.send(resolve_emoji('WARN', ctx) + " All results included loli/shota content; this search is invalid.")
                response = non_loli[random.randint(0, len(non_loli) - 1)]
                img = response['file_url']
                tags = ', '.join(response['tags'].split(' '))
                safe = "`" + tags + "`" if len(tags) < 5000 else ("[Click me for the tags](" + await self.bot.post_to_haste(tags) + ')')
                em = discord.Embed(
                    description=f'**Rating:** {(rating if rating in ["safe", "questionable", "explicit"] else "safe")}'
                                + f'\n{safe}',
                    colour=0xff0000)
                em.set_image(url=img)
                em.set_author(name='Found Image! Click me if it doesn\'t load!', url=img)
                await ctx.send(embed=em)
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + " No image found. Sorry :/")
        elif rating == "safe" and not ctx.channel.is_nsfw():
            await ctx.send(
                resolve_emoji('WARN', ctx) + " Sorry! I know that this image is marked as `safe`, but yande.re sometimes returns lewd images in the safe rating. Please use an NSFW channel.")
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + " This is not an NSFW channel.")


def setup(bot):
    bot.add_cog(NSFW(bot))
