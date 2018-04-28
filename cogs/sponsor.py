import discord
from discord.ext import commands


class Sponsor:
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def template(self, ctx):
        """Generate a template for the Sponsor commands."""
        if ctx.invoked_subcommand is None:
            return await ctx.send('The valid tiers are `1`, `2`, or `3`')

    @template.command(name="1")
    async def _1(self, ctx):
        """The template for the first tier of Sponsor commands, achieved at $15"""
        return await ctx.send('__**Up here is where your title will be!**__\n'
                              + 'In this next line, you say who it\'s by and what it is (a guild by Desii, a bot by Lars, etc)\n'
                              + '\nNow, you can start your description. You have only a few requirements:\n'
                              + 'No `@everyone`s\n'
                              + 'No image links\n'
                              + 'You cannot surpass 1000 characters\n'
                              + 'There will be a "watermark" at the bottom (removed in $20 tier)\n\n'
                              + 'To get your own sponsor command, please check out <https://patreon.com/desii>')

    @template.command(name="2")
    async def _2(self, ctx):
        """The template for the second tier of Sponsor commands, achieved at $20"""
        em = discord.Embed(description='Tell us who this is by and what it is (a guild by Desii, etc)\n'
                                       + 'Now, you are allowed a full description, with [masked links](https://godavaru.site/) '
                                       + 'and anything you can have in a normal embed description.')
        em.set_author(name='Up here is where your title will be!', icon_url=ctx.author.avatar_url)
        em.set_footer(text='You can also customise the footer (no watermarks either :) )')
        return await ctx.send(embed=em)

    @template.command(name="3")
    async def _3(self, ctx):
        """The "template" for the third tier of Sponsor commands, achieved at $50"""
        return await ctx.send('There is no template. You have full control, so long as you follow the following rules:\n'
                              + '**1:** The name of your item & the creator(s) must be shown somewhere in a visible place, '
                              + 'preferably at the top\n'
                              + '**2:** You must not place anything harmful, aka IP loggers, `@everyone` pings in simple '
                              + 'text messages, or anything of the like. Your sponsor command goes through a quick '
                              + 'verification process, and if you break these rules, it will never be verified.\n'
                              + '**3:** You must fit in with the limitations of Discord and have common sense. (message no '
                              + 'longer than 2000 chars (ofc) and dont have a wall of emojis)\n\n'
                              + 'Aside from that, thanks for your pledge if you have already or if you are considering it, '
                              + 'thanks as well :)')

def setup(bot):
    bot.add_cog(Sponsor(bot))