import random
import discord
import asyncio
from discord.ext import commands


class Currency:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=300, per=1, type=commands.BucketType.user)
    async def loot(self, ctx):
        """Loot the current channel for goodies!"""
        max_num = 100  # will be affected by prem/vote status, cba to add that for now.
        amnt = random.randint(0, max_num)
        if amnt > 50:
            self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps) 
                                VALUES ({ctx.author.id}, DEFAULT, {amnt}, DEFAULT, DEFAULT) 
                                ON DUPLICATE KEY UPDATE balance = balance + {amnt}''')
            await ctx.send(f":tada: You looted **{amnt}** from this channel!")
        else:
            await ctx.send(":slight_frown: You didn't loot anything")

    @commands.command()
    async def profile(self, ctx, *, member: discord.Member = None):
        """Show yours or someone else's profile."""
        if member is None:
            member = ctx.author
        results = self.bot.query_db(f'''SELECT * FROM users WHERE userid={member.id}''')
        if results:
            profile = list(results)[0]
            em = discord.Embed(description=profile[1] if profile[1] else 'No description set.', color=ctx.author.color)
            em.set_author(
                name=member.display_name + ("'s" if not member.display_name.endswith('s') else "'") + " Profile")
            em.add_field(name='Balance', value=f'${profile[2]}')
            em.add_field(name='Married with', value=self.bot.get_user_info(int(profile[3])))
            em.add_field(name='Reputation', value=profile[4])
            await ctx.send(embed=em)
        else:
            await ctx.send(":x: That user has no profile in my database.")

    @commands.command()
    async def marry(self, ctx, *, member: discord.Member):
        """Marry a user!"""
        if member == ctx.author:
            return await ctx.send(":x: You can't marry yourself.")
        if member.bot:
            return await ctx.send(":x: You can't marry a bot.")
        if self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={member.id}'''):
            return await ctx.send(":x: That person is already married!")
        if self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={ctx.author.id}'''):
            return await ctx.send(":x: You are already married!")
        await ctx.send(f'{member.display_name}, say `yes` or `no` to the marriage proposal from {ctx.author.display_name}')
        def check(m):
            return m.content.lower() in ["yes", "no"] and m.channel == ctx.channel and m.author == member
        try:
            msg = await self.bot.wait_for('message', check=check, timeout=120.0)
        except asyncio.TimeoutError:
            return await ctx.send("The proposal timed out :<")
        if msg.content.lower() == 'yes':
            await ctx.send(":tada: Congratulations! The two of you are now married.")
            self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps) 
                                VALUES ({ctx.author.id}, DEFAULT, DEFAULT, {member.id}, DEFAULT) 
                                ON DUPLICATE KEY UPDATE marriage={member.id}''')
        elif msg.content.lower() == 'no':
            await ctx.send(f":sob: {ctx.author.display_name} just got denied :broken_heart:")

def setup(bot):
    bot.add_cog(Currency(bot))