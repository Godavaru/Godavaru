import discord
import asyncio
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

    @commands.command()
    @commands.check(can_manage)
    async def welcome(self, ctx, channel: str, *, msg: str = None):
        """Set the welcome message & channel for this server.
        Note: To use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            if msg:
                msg = msg.replace('"', '\\"')
                self.bot.query_db(f'''INSERT INTO settings (guildid,welcome_channel,welcome_message)
                                    VALUES ({ctx.guild.id},{c.id},"{msg}") ON DUPLICATE KEY UPDATE
                                    welcome_channel={c.id},welcome_message="{msg}";''')
                await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully set your welcome channel and message.')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + ' You must supply the message you want after the channel.')
        elif channel == 'reset':
            self.bot.query_db(f'''UPDATE settings SET welcome_channel=NULL,welcome_message=NULL WHERE
                                guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your welcome channel & message.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Channel "{channel}" not found.')

    @commands.command()
    @commands.check(can_manage)
    async def leave(self, ctx, channel: str, *, msg: str = None):
        """Set the leave message & channel for this server.
        Note: To use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            if msg:
                msg = msg.replace('"', '\\"')
                self.bot.query_db(f'''INSERT INTO settings (guildid,leave_channel,leave_message)
                                        VALUES ({ctx.guild.id},{c.id},"{msg}") ON DUPLICATE KEY UPDATE
                                        leave_channel={c.id},leave_message="{msg}";''')
                await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully set your leave channel and message.')
            else:
                await ctx.send(
                    resolve_emoji('ERROR', ctx) + ' You must supply the message you want after the channel.')
        elif channel == 'reset':
            self.bot.query_db(f'''UPDATE settings SET leave_channel=NULL,leave_message=NULL WHERE
                                    guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your leave channel & message.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Channel "{channel}" not found.')

    @commands.command(name='import')
    @commands.check(can_manage)
    @commands.cooldown(rate=1, per=3600, type=commands.BucketType.guild)
    async def _import(self, ctx):
        """Import settings from Kumiko.
        WARNING: THIS CAN NOT BE UNDONE."""
        kum_query = self.bot.query_db(f'''SELECT logchannel,modlogchannel,muterole,
                                        joinmessage,leavemessage,welcomechannel FROM desii.opts 
                                        WHERE guildid={ctx.guild.id};''')
        if kum_query:
            await ctx.send('Found data! Are you ***sure*** that you want to do this? This can **NOT** be undone.'
                           + ' This will replace all of your current settings in Godavaru. Are you ***bolded sure*** '
                           + 'that you wish to go through with this? Please say `yes` if you wish to continue.')

            def check(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content == 'yes'

            try:
                await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                return await ctx.send(resolve_emoji('ERROR', ctx) + f' The time ran out, cancelling import.')
            data = kum_query[0]
            logs = str(data[0]).replace('None', 'NULL')
            mod = str(data[1]).replace('None', 'NULL')
            mute = str(data[2]).replace('None', 'NULL')
            join = '"' + data[3].replace('"', '\\"') + '"' if data[3] else 'NULL'
            leave = '"' + data[4].replace('"', '\\"') + '"' if data[4] else 'NULL'
            channel = str(data[5]).replace('None', 'NULL')
            self.bot.query_db(f'''INSERT INTO settings (guildid,log_channel,mod_channel,muterole,
                                welcome_message,leave_message,welcome_channel,leave_channel) VALUES
                                ({ctx.guild.id}, {logs}, {mod}, {mute}, "{join}", "{leave}", 
                                {channel}, {channel}) ON DUPLICATE KEY UPDATE log_channel={logs},
                                mod_channel={mod},muterole={mute},welcome_message="{join}",
                                leave_message="{leave}",welcome_channel={channel},leave_channel={channel};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully imported all data from Kumiko into Godavaru.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' I couldn\'t find any data from Kumiko to import.')


def setup(bot):
    bot.add_cog(Settings(bot))
