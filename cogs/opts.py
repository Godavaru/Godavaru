import discord
import config
from discord.ext import commands
from .utils.db import get_all_prefixes
from .utils.tools import resolve_emoji, resolve_channel, resolve_role


def can_manage(ctx):
    return ctx.author.id in config.owners or ctx.author.guild_permissions.manage_guild


class Settings:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(can_manage)
    async def prefix(self, ctx, prefix: str = None):
        """Change the guild prefix.
        Note: to use this command, you must have the `MANAGE_GUILD` permission. If you wish to have a prefix with spaces, surround it in "quotes" """
        if not prefix:
            try:
                return await ctx.send(f'My prefix here is `{self.bot.prefixes[str(ctx.guild.id)]}`. You can change that with `{ctx.prefix}prefix <prefix>`')
            except KeyError:
                return await ctx.send(f'My prefix here is `{config.prefix[0]}`. You can change that with `{ctx.prefix}prefix <prefix>`')
        self.bot.query_db(f"""INSERT INTO settings (guildid, prefix) VALUES ({ctx.guild.id}, "{prefix}") 
                            ON DUPLICATE KEY UPDATE prefix = "{prefix}";""")
        self.bot.prefixes = get_all_prefixes()
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully set my prefix here to `{prefix}`')

    @commands.command()
    @commands.check(can_manage)
    async def modlog(self, ctx, channel: str):
        """Change the guild mod log channel.
        Note: to use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            self.bot.query_db(f'''INSERT INTO settings (guildid,mod_channel) VALUES ({ctx.guild.id}, {c.id})
                                ON DUPLICATE KEY UPDATE mod_channel={c.id}''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully changed the modlog channel to **#{c}** (`{c.id}`)')
        elif channel == 'reset':
            self.bot.query_db(f'''UPDATE settings SET mod_channel=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your mod log channel.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Channel "{channel}" not found.')

    @commands.command()
    @commands.check(can_manage)
    async def muterole(self, ctx, *, role: str):
        """Change the guild mute role.
        Note: To use this command, you must have the `MANAGE_GUILD` permission.
        Note 2: The muterole does not automatically deny `SEND_MESSAGES`. You must do this yourself."""
        r = resolve_role(role, ctx)
        if r:
            self.bot.query_db(f'''INSERT INTO settings (guildid,muterole) VALUES ({ctx.guild.id},{r.id})
                                ON DUPLICATE KEY UPDATE muterole={r.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully changed the mute role to **{r}** (`{r.id}`)')
        elif role == 'reset':
            self.bot.query_db(f'''UPDATE settings SET muterole=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your mute role.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Role "{role}" not found.')

    @commands.command()
    @commands.check(can_manage)
    async def logs(self, ctx, channel: str):
        """Change the guild logging channel.
        Note: To use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            self.bot.query_db(f'''INSERT INTO settings (guildid,log_channel) VALUES ({ctx.guild.id},{c.id})
                                ON DUPLICATE KEY UPDATE log_channel={c.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully changed the logging channel to **#{c}** (`{c.id}`)')
        elif channel == 'reset':
            self.bot.query_db(f'''UPDATE settings SET log_channel=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your log channel.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Channel "{channel}" not found.')


def setup(bot):
    bot.add_cog(Settings(bot))
