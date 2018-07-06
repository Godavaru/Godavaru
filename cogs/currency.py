import random
import discord
import asyncio
import json
from .assets import items
from .utils import db
from .utils.tools import resolve_emoji
from discord.ext import commands
import config


class Currency:
    def __init__(self, bot):
        self.bot = bot
        self.crime_quotes = {
            'win': [
                'You robbed a bank, scoring ${0} without even digging into your money for funding.',
                'You stole candy from a baby and sold it for ${0}!',
                'After a long and unsuccessful day, you finally managed to mug a dog. It had ${0} in its fur.',
                'You stole a car! There was ${0} in the back seat, so double score!'
            ],
            'lose': [
                'You were going to steal candy from a baby, but then you accidentally mistook the baby for the mom. You lost $500.',
                'You stole a car, but crashed it. You paid $500 for repairs, but atleast you got a car.',
                'When trying to hack into the Pentagon, your laptop exploded, revealing your location. You paid $500 for bail.',
                'Your mom called you and scolded you for trying to commit a crime. She took your money and your phone for a week :<',
                'Your selfbot usage was discovered by b1nzy. You got banned instantly, losing all $500 you spent on Discord.',
                'You stepped on an ant. You paid for its life support, costing you $500.'
            ]
        }

    def is_premium(self, member):
        support = self.bot.get_guild(315251940999299072)
        role = discord.utils.get(support.roles, name="Patron")
        return role in support.get_member(member.id).roles if support.get_member(member.id) else False

    @commands.command()
    @commands.cooldown(rate=1, per=300, type=commands.BucketType.user)
    async def loot(self, ctx):
        """Loot the current channel for goodies!"""
        max_num = 100 if not self.is_premium(ctx.author) else 500
        amnt = random.randint(0, max_num)
        gets_item = random.randint(0, 10) >= 7
        if amnt > 50:
            self.bot.query_db(f'''INSERT INTO users (userid, balance) VALUES ({ctx.author.id}, {amnt}) 
                                ON DUPLICATE KEY UPDATE balance = balance + {amnt}''')
            msg = f":tada: You looted **{amnt}** from this channel!" + (' Also, ' if gets_item else '')
        else:
            msg = ":slight_frown: You didn't loot anything" + (', but ' if gets_item else '.')
        if gets_item:
            amount = random.randint(1, 5)
            item = random.choice([['LEAF', 'leaves'], ['BLOSSOM', 'blossoms']])
            msg += f'you found {amount} {item[1]}! ' + items.all_items[item[0]]['emoji']
            results = self.bot.query_db(f'''SELECT items FROM users WHERE userid={ctx.author.id}''')
            itms = json.loads(results[0][0].replace("'", '"')) if results and results[0][0] else json.dumps({})
            try:
                blossoms = itms[item[0]]
                itms[item[0]] = blossoms + amount
            except KeyError:
                itms[item[0]] = amount
            self.bot.query_db(f'''INSERT INTO users (userid, items) VALUES ({ctx.author.id}, "{str(itms)}") 
                                        ON DUPLICATE KEY UPDATE items="{str(itms)}";''')
        await ctx.send(msg)

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def transfer(self, ctx, user: discord.Member, amount: str):
        """Transfer money to another user."""
        try:
            amount = float(amount)
        except ValueError:
            return await ctx.send(resolve_emoji('ERROR', ctx) + ' That is not a number.')
        amount = round(amount)
        if user.id == ctx.author.id:
            return await ctx.send(resolve_emoji('ERROR', ctx) + ' You cannot transfer to yourself, silly.')
        if user.bot:
            return await ctx.send(resolve_emoji('ERROR', ctx) + ' You cannot transfer to a bot, silly.')
        if amount <= 0:
            return await ctx.send(
                resolve_emoji('ERROR', ctx) + ' Nice try. You cannot transfer negative or zero money.')
        bal = self.bot.query_db(f'''SELECT balance FROM users WHERE userid={ctx.author.id};''')
        if not bal or not bal[0][0] >= amount:
            return await ctx.send(resolve_emoji('ERROR', ctx) + ' You cannot transfer more than what you have.')
        self.bot.query_db(f'''INSERT INTO users (userid, balance) VALUES ({user.id}, {amount})
                            ON DUPLICATE KEY UPDATE balance = balance + {amount};''')
        self.bot.query_db(f'''UPDATE users SET balance = balance - {amount} WHERE userid={ctx.author.id};''')
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successully transfered **{amount}** credits to **{user}**')

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def profile(self, ctx, *, member: discord.Member = None):
        """Show yours or someone else's profile."""
        if member is None:
            member = ctx.author
        if member.bot:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " Bots don't have profiles.")
        if str(member.id) in self.bot.blacklist.keys():
            return await ctx.send(resolve_emoji('ERROR', ctx) + " That user is blacklisted.")
        results = self.bot.query_db(f'''SELECT * FROM users WHERE userid={member.id}''')
        if results:
            profile = list(results)[0]
        else:
            profile = db.default_profile_values
        emote = ('⚙ ' if member.id in config.owners else '') + ('💰 ' if self.is_premium(member) else '')
        name = (emote + '| ' if emote != '' else '') + member.display_name
        itms = json.loads(profile[5].replace("'", '"')) if profile[5] else json.loads('{}')
        msg = []
        for i in itms:
            if itms[i] != 0:
                msg.append(f"{items.all_items[i]['emoji']} x{itms[i]}")
        em = discord.Embed(
            description=profile[1] if profile[1] else ('No description set.'
                                                       + (
                                                           f' Set one with `{ctx.prefix}description <description>`!' if member is ctx.author else "")),
            color=ctx.author.color)
        em.set_author(
            name=name + ("'s" if not name.endswith('s') else "'") + " Profile")
        em.add_field(name='Balance', value=f'${profile[2]}')
        em.add_field(name='Reputation', value=profile[4])
        em.add_field(name='Married with',
                     value=await self.bot.get_user_info(int(profile[3])) if profile[3] else "Nobody.", inline=False)
        em.add_field(name="Items", value=", ".join(msg) if len(msg) > 0 else "None (yet!)")
        em.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    async def description(self, ctx, *, description: str):
        """Set your profile description.
        Max of 300 for non-donors and 500 for donors."""
        max_value = 300 if not self.is_premium(ctx.author) else 500
        if len(description) > max_value:
            return await ctx.send(
                resolve_emoji('ERROR',
                              ctx) + f" The maximum the description can be is `{max_value}` characters for you! "
                + (
                    f"Get the max raised to 500 by donating! Find the link in `{ctx.prefix}links`!" if not self.is_premium(
                        ctx.author) else ""))
        self.bot.query_db(f'''INSERT INTO users (userid, description) VALUES ({ctx.author.id}, %s) 
                            ON DUPLICATE KEY UPDATE description=%s''', (description, description))
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f" Set your description! Check it out on `{ctx.prefix}profile`!")

    @commands.command()
    @commands.cooldown(rate=1, per=43200, type=commands.BucketType.user)
    async def rep(self, ctx, *, member: discord.Member):
        """Give reputation to a user."""
        if member == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You can not rep yourself.")
        if member.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(resolve_emoji('ERROR', ctx) + " Yes, bots are cool, but you can not rep them.")
        if str(member.id) in self.bot.blacklist.keys():
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(resolve_emoji('ERROR', ctx) + " That user is blacklisted.")
        self.bot.query_db(f'''INSERT INTO users (userid, reps) VALUES ({member.id}, 1) 
                            ON DUPLICATE KEY UPDATE reps=reps+1''')
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f" Added reputation point to **{member}**")

    @commands.group(aliases=["richest", "top", "lb"])
    async def leaderboard(self, ctx):
        """Check the leaderboard of money."""
        if ctx.invoked_subcommand is None:
            results = self.bot.query_db(f'SELECT userid,balance FROM users ORDER BY balance DESC LIMIT 15')
            msg = ""
            for i in range(len(results)):
                row = results[i]
                user = self.bot.get_user(int(row[0]))
                if not user:
                    user = row[0]
                n = i + 1
                if n < 10:
                    n = f'0{i+1}'
                msg += f'{n}.- {user}: ${row[1]}\n'
            em = discord.Embed(
                title="Richest Users",
                description=msg,
                color=ctx.author.color
            )
            await ctx.send(embed=em)

    @leaderboard.command(name="rep")
    async def leaderboard_rep(self, ctx):
        """Check the leaderboard of reputation."""
        results = self.bot.query_db(f'SELECT userid,reps FROM users ORDER BY reps DESC LIMIT 15')
        msg = ""
        for i in range(len(results)):
            row = results[i]
            user = self.bot.get_user(int(row[0]))
            if not user:
                user = row[0]
            n = i + 1
            if n < 10:
                n = f'0{i+1}'
            msg += f'{n}.- {user}: {row[1]} points\n'
        em = discord.Embed(
            title="Richest Users in Reputation",
            description=msg,
            color=ctx.author.color
        )
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def crime(self, ctx):
        """Commit a crime and get up to $1000, but risk $500."""
        profile = self.bot.query_db(f'''SELECT balance FROM users WHERE userid={ctx.author.id}''')
        if profile and profile[0][0] >= 500:
            win = random.randint(1, 10) > 8
            if win:
                amount = random.randint(500, 1000)
                self.bot.query_db(f'''UPDATE users SET balance=balance+{amount} WHERE userid={ctx.author.id}''')
                await ctx.send(resolve_emoji('SUCCESS', ctx) + random.choice(self.crime_quotes['win']).format(amount))
            else:
                self.bot.query_db(f'''UPDATE users SET balance=balance-500 WHERE userid={ctx.author.id}''')
                await ctx.send(resolve_emoji('ERROR', ctx) + random.choice(self.crime_quotes['lose']))
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + 'You need at least $500 to fund the crime!')
            ctx.command.reset_cooldown(ctx)

    @commands.command()
    @commands.cooldown(rate=1, per=8, type=commands.BucketType.user)
    async def gamble(self, ctx, amount: str):
        """Gamble your life away!"""
        profile = self.bot.query_db(f'''SELECT balance FROM users WHERE userid={ctx.author.id}''')
        if profile:
            if amount == 'all':
                amount = profile[0][0]
            elif amount.endswith('%'):
                try:
                    amount = round((int(amount[:-1]) * 0.01) * profile[0][0])
                except ValueError:
                    return await ctx.send(resolve_emoji('ERROR', ctx) + ' That is not a valid percentage.')
            try:
                amount = int(amount)
            except ValueError:
                return await ctx.send(resolve_emoji('ERROR', ctx) + ' That is not a valid number.')
            if amount <= 0:
                return await ctx.send(resolve_emoji('ERROR', ctx) + ' Don\'t even try it...')
            if profile[0][0] >= amount:
                win = random.randint(1, 10) >= 7
                if win:
                    bal = f'balance+{round(amount * 0.7)}'
                    await ctx.send(f':tada: You won {round(amount * 0.7)} credits!')
                else:
                    bal = f'balance-{amount}'
                    await ctx.send(f':sob: Sadly, you lost {amount} credits.')
                self.bot.query_db(f'''UPDATE users SET balance={bal} WHERE userid={ctx.author.id}''')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + ' You don\'t have the money to do that.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + ' You don\'t have the money to do that.')

    @commands.command()
    async def marry(self, ctx, *, member: discord.Member):
        """Marry a user!"""
        if member == ctx.author:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You can't marry yourself.")
        if member.bot:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You can't marry a bot.")
        if self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={member.id}''') and \
                self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={member.id}''')[0][0]:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " That person is already married!")
        if self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={ctx.author.id}''') and \
                self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={ctx.author.id}''')[0][0]:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You are already married!")
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
            self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps, items) 
                                VALUES ({member.id}, DEFAULT, DEFAULT, {ctx.author.id}, DEFAULT, DEFAULT) 
                                ON DUPLICATE KEY UPDATE marriage={ctx.author.id}''')
        elif msg.content.lower() == 'no':
            await ctx.send(f":sob: {ctx.author.display_name} just got denied :broken_heart:")

    @commands.command()
    async def divorce(self, ctx):
        """Divorce the person you are married to :sob:"""
        married = self.bot.query_db(f'''SELECT marriage FROM users WHERE userid={ctx.author.id}''')
        if not married or not married[0][0]:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You are not married.")
        await ctx.send(resolve_emoji('SUCCESS', ctx) + " You're single now. Cool.")
        self.bot.query_db(f'''UPDATE users SET marriage=DEFAULT WHERE userid={ctx.author.id}''')
        self.bot.query_db(f'''UPDATE users SET marriage=DEFAULT WHERE userid={married[0][0]}''')

    @commands.command(aliases=["bal", "credits"])
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
    @commands.cooldown(rate=1, per=86400, type=commands.BucketType.user)
    async def daily(self, ctx, *, member: discord.Member = None):
        """Collect your daily reward.
        Alternatively, you may give your daily to someone else and they get more credits."""
        user_id = member.id if member else ctx.author.id
        max_value = 200 if not self.is_premium(ctx.author) else 600
        daily_coins = random.randint(200, max_value) + (0 if not member else random.randint(1, 20))
        self.bot.query_db(f'''INSERT INTO users (userid, description, balance, marriage, reps, items)
                            VALUES ({user_id}, DEFAULT, {daily_coins}, DEFAULT, DEFAULT, DEFAULT)
                            ON DUPLICATE KEY UPDATE balance = balance + {daily_coins}''')
        await ctx.send(resolve_emoji('SUCCESS',
                                     ctx) + f' You {"gave your daily credits of $" + str(daily_coins) + " to " + member.display_name if member else "collected your daily credits of $" + str(daily_coins)}')

    @commands.command()
    async def buy(self, ctx, item: str, amount: int = 1):
        """Buy an item.
        Use `list` as the param for a list of all items that can be bought."""
        if amount <= 0:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You can not buy less than one of an item.")
        item = item.upper()
        if item == 'LIST':
            msg = ""
            for it in items.all_items:
                if items.all_items[it]['buy']:
                    msg += f"{items.all_items[it]['emoji']} - ${items.all_items[it]['buy']} - {it.capitalize()}\n"
            return await ctx.send(msg)
        if item not in items.all_items:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " That is not an item.")
        if items.all_items[item]['buy']:
            results = self.bot.query_db(f'''SELECT balance,items FROM users WHERE userid={ctx.author.id}''')
            if results:
                if results[0][0] > (items.all_items[item]["buy"] * amount):
                    itms = json.loads(results[0][1].replace("'", '"')) if results[0][1] else json.loads('{}')
                    try:
                        amnt = itms[item]
                        itms[item] = amnt + amount
                        self.bot.query_db(f'''UPDATE users SET items="{str(itms)}" WHERE userid={ctx.author.id}''')
                    except KeyError:
                        itms[item] = amount
                        self.bot.query_db(f'''UPDATE users SET items="{str(itms)}" WHERE userid={ctx.author.id}''')
                    self.bot.query_db(
                        f'''UPDATE users SET balance=balance-{items.all_items[item]["buy"] * amount} WHERE userid={ctx.author.id}''')
                    await ctx.send(
                        resolve_emoji('SUCCESS',
                                      ctx) + f' You purchased {amount}x {items.all_items[item]["emoji"]} for ${items.all_items[item]["buy"] * amount}')
                else:
                    await ctx.send(resolve_emoji('ERROR', ctx) + " You do not have the money for that.")
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + " You do not have the money for that.")
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + " That item can not be bought.")

    @commands.command()
    async def sell(self, ctx, item: str, amount: int = 1):
        """Sell an item.
        Use `list` as the param for a list of all items that can be sold."""
        if amount <= 0:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You can not sell less than one of an item.")
        item = item.upper()
        if item == 'LIST':
            msg = ""
            for it in items.all_items:
                if items.all_items[it]['sell']:
                    msg += f"{items.all_items[it]['emoji']} - ${items.all_items[it]['sell']} - {it.capitalize()}\n"
            return await ctx.send(msg)
        if item not in items.all_items:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " That is not an item.")
        if items.all_items[item]['sell']:
            results = self.bot.query_db(f'''SELECT items FROM users WHERE userid={ctx.author.id}''')
            if results:
                itms = json.loads(results[0][0].replace("'", '"')) if results[0][0] else json.loads('{}')
                try:
                    amnt = itms[item]
                    if amount > amnt:
                        return await ctx.send(resolve_emoji('ERROR', ctx) + " You do not have enough of that item.")
                    itms[item] = amnt - amount
                    self.bot.query_db(
                        f'''UPDATE users SET items="{str(itms)}",balance=balance+{items.all_items[item]["sell"] * amount} WHERE userid={ctx.author.id}''')
                    await ctx.send(
                        resolve_emoji('SUCCESS',
                                      ctx) + f' You successfully sold {amount}x {items.all_items[item]["emoji"]} for ${items.all_items[item]["sell"] * amount}')
                except KeyError:
                    return await ctx.send(resolve_emoji('ERROR', ctx) + " You do not have enough of that item.")
            else:
                return await ctx.send(resolve_emoji('ERROR', ctx) + " You do not have enough of that item.")
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + " That item can not be sold.")

    @commands.command()
    @commands.cooldown(rate=1, per=300, type=commands.BucketType.user)
    async def mine(self, ctx):
        """Go mining for those diamonds!
        Requires a pickaxe. Has a chance of breaking the pickaxe."""
        results = self.bot.query_db(f'''SELECT items FROM users WHERE userid={ctx.author.id}''')
        itms = json.loads(results[0][0].replace("'", '"')) if results and results[0][0] else json.dumps({})
        if 'PICKAXE' not in itms or itms['PICKAXE'] == 0:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(resolve_emoji('ERROR', ctx) + " You don't seem to have a pickaxe.")
        gets_jewel = random.randint(1, 10) >= 7
        jewel = random.choice(['DIAMOND', 'RUBY', 'SAPPHIRE'])
        pick_breaks = random.randint(1, 10) >= 8
        max_value = 150 if not self.is_premium(ctx.author) else 300
        num = random.randint(0, max_value)
        if num > 50:
            msg = f":pick: You mined {num} credits" + (" and you found a " + jewel.lower() + '!' if gets_jewel else "") + (
                " but your pickaxe broke :<" if pick_breaks else "") + '.'
            await ctx.send(msg)
            if gets_jewel:
                try:
                    amnt = itms[jewel]
                    itms[jewel] = amnt + 1
                except KeyError:
                    itms[jewel] = 1
            if pick_breaks:
                pick_amnt = itms['PICKAXE']
                itms['PICKAXE'] = pick_amnt - 1
            sets = f'balance=balance+{num},items="{str(itms)}"'
            self.bot.query_db(f'''UPDATE users SET {sets} WHERE userid={ctx.author.id}''')
        else:
            msg = f':sob: You didn\'t find anything' + (' and your pick broke :<' if pick_breaks else '') + '.'
            await ctx.send(msg)
            if pick_breaks:
                pick_amnt = itms['PICKAXE']
                itms['PICKAXE'] = pick_amnt - 1
                self.bot.query_db(f'''UPDATE users SET items="{str(itms)}" WHERE userid={ctx.author.id}''')


def setup(bot):
    bot.add_cog(Currency(bot))
