import random
import discord
import asyncio
import json
from .assets import items
from discord.ext import commands


class Currency:
    def __init__(self, bot):
        self.bot = bot

    def is_premium(self, member):
        support = self.bot.get_guild(315251940999299072)
        role = discord.utils.get(support.roles, name="Patron")
        return role in support.get_member(member.id).roles

    @commands.command()
    @commands.cooldown(rate=300, per=1, type=commands.BucketType.user)
    async def loot(self, ctx):
        """Loot the current channel for goodies!"""
        max_num = 100 if not self.is_premium(ctx.author) else 500
        amnt = random.randint(0, max_num)
        if amnt > 50:
            self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps, items) 
                                VALUES ({ctx.author.id}, DEFAULT, {amnt}, DEFAULT, DEFAULT, DEFAULT) 
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
            name = ("💰 | " if self.is_premium(member) else "") + member.display_name
            em = discord.Embed(description=profile[1] if profile[1] else 'No description set.', color=ctx.author.color)
            em.set_author(
                name=name + ("'s" if not name.endswith('s') else "'") + " Profile")
            em.add_field(name='Balance', value=f'${profile[2]}')
            em.add_field(name='Reputation', value=profile[4])
            em.add_field(name='Married with', value=await self.bot.get_user_info(int(profile[3])), inline=False)
            em.set_thumbnail(url=member.avatar_url.replace('?size=1024', ''))
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
        await ctx.send(
            f'{member.display_name}, say `yes` or `no` to the marriage proposal from {ctx.author.display_name}')

        def check(m):
            return m.content.lower() in ["yes", "no"] and m.channel == ctx.channel and m.author == member

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=120.0)
        except asyncio.TimeoutError:
            return await ctx.send("The proposal timed out :<")
        if msg.content.lower() == 'yes':
            await ctx.send(":tada: Congratulations! The two of you are now married.")
            self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps, items) 
                                VALUES ({ctx.author.id}, DEFAULT, DEFAULT, {member.id}, DEFAULT, DEFAULT) 
                                ON DUPLICATE KEY UPDATE marriage={member.id}''')
        elif msg.content.lower() == 'no':
            await ctx.send(f":sob: {ctx.author.display_name} just got denied :broken_heart:")

    @commands.command()
    async def divorce(self, ctx):
        """Divorce the person you are married to :sob:"""
        if not self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={ctx.author.id}'''):
            return await ctx.send(":x: You are not married.")
        await ctx.send(":ok_hand: You're single now. Cool.")
        self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps, items)
                            VALUES ({ctx.author.id}, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT) 
                            ON DUPLICATE KEY UPDATE marriage=DEFAULT''')

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, *, member: discord.Member = None):
        """Check the balance of yourself or another user."""
        if member is None:
            member = ctx.author
        results = self.bot.query_db(f'''SELECT balance FROM users WHERE userid={member.id}''')
        balance = 0
        if results:
            balance = list(results)[0][0]
        await ctx.send(f":gem: {member.display_name} has a balance of ${balance}")

    @commands.command()
    async def daily(self, ctx, *, member: discord.Member = None):
        """Collect your daily reward.
        Alternatively, you may give your daily to someone else and they get more credits."""
        user_id = member.id if member else ctx.author.id
        max_value = 200 if not self.is_premium(ctx.author) else 600
        daily_coins = random.randint(200, max_value) + (0 if not member else random.randint(1, 20))
        self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps, items)
                            VALUES ({user_id}, DEFAULT, {daily_coins}, DEFAULT, DEFAULT, DEFAULT)
                            ON DUPLICATE KEY UPDATE balance = balance + {daily_coins}''')
        await ctx.send(f':white_check_mark: You {"gave your daily credits of $" + str(daily_coins) + " to " + member.display_name if member else "collected your daily credits of $" + str(daily_coins)}')

    @commands.command()
    async def buy(self, ctx, item: str, amount: int = 1):
        """Buy an item.
        Use `list` as the param for a list of all items that can be bought."""
        if item.lower() == 'list':
            msg = ""
            for it in items.all_items:
                if items.all_items[it]['buy']:
                    msg += f"{items.all_items[it]['emoji']} - ${items.all_items[it]['buy']} - {it.capitalize()}\n"
            return await ctx.send(msg)
        if item.upper() not in items.all_items:
            return await ctx.send(":x: That is not an item.")
        if items.all_items[item]['buy']:
            results = self.bot.query_db(f'''SELECT balance,items FROM users WHERE userid={ctx.author.id}''')
            if results:
                if results[0][0] > (items.all_items[item]["buy"] * amount):
                    itms = json.loads(results[0][1] if results[0][1] else '{}')
                    try:
                        amnt = itms[item]
                        itms[item] = amnt + amount
                        self.bot.query_db(f'''UPDATE users SET items='{str(itms)}' WHERE userid={ctx.author.id}''')
                    except:
                        itms[item] = amount
                        self.bot.query_db(f'''UPDATE users SET items='{str(itms)}' WHERE userid={ctx.author.id}''')
                    self.bot.query_db(
                        f'''UPDATE users SET balance=balance-{items.all_items[item]["buy"] * amount} WHERE userid={ctx.author.id}''')
                    await ctx.send(f':white_check_mark: You purchased {amount}x{items.all_items[item]["emoji"]} for ${items.all_items[item]["buy"] * amount}')
                else:
                    await ctx.send(":x: You do not have the money for that.")
            else:
                await ctx.send(":x: You do not have the money for that.")
        else:
            await ctx.send(":x: That item can not be bought.")


def setup(bot):
    bot.add_cog(Currency(bot))
