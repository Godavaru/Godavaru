import discord
import config
import pymysql
from discord.ext import commands
from cogs.utils.db import *


def is_owner(ctx):
    return ctx.author.id in config.owners


class Settings:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    @commands.check(is_owner)
    async def prefix(self, ctx, prefix: str = None):
        if not prefix:
            try:
                return await ctx.send(f'My prefix here is `{self.bot.prefixes_dict[str(ctx.guild.id)]}`')
            except KeyError:
                return await ctx.send(f'I have no custom prefix here. Set one with `{ctx.prefix}prefix <prefix>`')
        db = pymysql.connect(config.db_ip, config.db_user, config.db_pass, config.db_name)
        cur = db.cursor()
        cur.execute(
            f"""INSERT INTO settings (guildid, prefix) VALUES ({ctx.guild.id}, "{prefix}") ON DUPLICATE KEY UPDATE prefix = "{prefix}";""")
        db.commit()
        db.close()
        self.bot.prefixes_dict = get_all_prefixes()
        await ctx.send(f':ok_hand: Successfully set my prefix here to `{prefix}`')