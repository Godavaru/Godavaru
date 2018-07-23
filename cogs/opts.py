import discord
import asyncio
import config
import json
from discord.ext import commands
from .utils.db import get_all_prefixes
from .utils.tools import resolve_emoji, resolve_channel, resolve_role


def can_manage(ctx):
    return ctx.author.id in config.owners or ctx.author.guild_permissions.manage_guild


class Settings:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def prefix(self, ctx, prefix: str = None):
        """Change the guild prefix.
        Note: to use this command, you must have the `MANAGE_GUILD` permission. If you wish to have a prefix with spaces, surround it in "quotes" """
        if not prefix:
            try:
                return await ctx.send(
                    f'My prefix here is `{self.bot.prefixes[str(ctx.guild.id)]}`. You can change that with `{ctx.prefix}prefix <prefix>`')
            except KeyError:
                return await ctx.send(
                    f'There is no custom prefix here. You can change that with `{config.prefix[0]}prefix <prefix>`')
        self.bot.query_db(f"""INSERT INTO settings (guildid, prefix) VALUES ({ctx.guild.id}, %s) 
                            ON DUPLICATE KEY UPDATE prefix = %s;""", (prefix, prefix))
        self.bot.prefixes = get_all_prefixes()
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully set my prefix here to `{prefix}`')

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def modlog(self, ctx, channel: str):
        """Change the guild mod log channel.
        Note: to use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            self.bot.query_db(f'''INSERT INTO settings (guildid,mod_channel) VALUES ({ctx.guild.id}, {c.id})
                                ON DUPLICATE KEY UPDATE mod_channel={c.id}''')
            await ctx.send(
                resolve_emoji('SUCCESS', ctx) + f' Successfully changed the modlog channel to **#{c}** (`{c.id}`)')
        elif channel == 'reset':
            self.bot.query_db(f'''UPDATE settings SET mod_channel=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your mod log channel.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Channel "{channel}" not found.')

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def muterole(self, ctx, *, role: str):
        """Change the guild mute role.
        Note: To use this command, you must have the `MANAGE_GUILD` permission.
        Note 2: The muterole does not automatically deny `SEND_MESSAGES`. You must do this yourself."""
        r = resolve_role(role, ctx)
        if r:
            if r.is_default():
                return await ctx.send(
                    resolve_emoji('ERROR', ctx) + ' You cannot set the default everyone role as a muterole.')
            self.bot.query_db(f'''INSERT INTO settings (guildid,muterole) VALUES ({ctx.guild.id},{r.id})
                                ON DUPLICATE KEY UPDATE muterole={r.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully changed the mute role to **{r}** (`{r.id}`)')
        elif role == 'reset':
            self.bot.query_db(f'''UPDATE settings SET muterole=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your mute role.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Role "{role}" not found.')

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def logs(self, ctx, channel: str):
        """Change the guild logging channel.
        Note: To use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            self.bot.query_db(f'''INSERT INTO settings (guildid,log_channel) VALUES ({ctx.guild.id},{c.id})
                                ON DUPLICATE KEY UPDATE log_channel={c.id};''')
            await ctx.send(
                resolve_emoji('SUCCESS', ctx) + f' Successfully changed the logging channel to **#{c}** (`{c.id}`)')
        elif channel == 'reset':
            self.bot.query_db(f'''UPDATE settings SET log_channel=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your log channel.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Channel "{channel}" not found.')

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def welcome(self, ctx, channel: str, *, msg: str = None):
        """Set the welcome message & channel for this server.
        Note: To use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            if msg:
                self.bot.query_db(f'''INSERT INTO settings (guildid,welcome_channel,welcome_message)
                                    VALUES ({ctx.guild.id},{c.id},%s) ON DUPLICATE KEY UPDATE
                                    welcome_channel={c.id},welcome_message=%s;''', (msg, msg))
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
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def leave(self, ctx, channel: str, *, msg: str = None):
        """Set the leave message & channel for this server.
        Note: To use this command, you must have the `MANAGE_GUILD` permission."""
        c = resolve_channel(channel, ctx)
        if c:
            if msg:
                self.bot.query_db(f'''INSERT INTO settings (guildid,leave_channel,leave_message)
                                        VALUES ({ctx.guild.id},{c.id},%s) ON DUPLICATE KEY UPDATE
                                        leave_channel={c.id},leave_message=%s;''', (msg, msg))
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

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def selfroles(self, ctx, func: str, name: str, *, role: discord.Role = None):
        """Manage the guild self roles for the `iam` command.
        Valid functions: `add`, `new`, `remove`, `rm`, `rem`, `delete`, `del`"""
        if func in ['add', 'new']:
            if role:
                if role.is_default():
                    return await ctx.send(resolve_emoji('ERROR', ctx) + ' You cannot set the default everyone role as a self role.')
                if role.position >= ctx.author.top_role.position:
                    return await ctx.send(
                        resolve_emoji('ERROR', ctx) + ' You cannot manage a role higher than your own.')
                results = self.bot.query_db(f'''SELECT self_roles FROM settings WHERE guildid={ctx.guild.id};''')
                selfroles = json.loads(results[0][0].replace("'", '"')) if results and results[0][0] else json.loads('{}')
                selfroles[name] = role.id
                self.bot.query_db(f'''UPDATE settings SET self_roles="{str(selfroles)}" WHERE guildid={ctx.guild.id};''')
                await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully added self role **{name}** which gives role **{role}**. This can be applied with `{ctx.prefix}iam {name}`')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + f' Missing required argument `role`, check `{ctx.prefix}help {ctx.command}`')
        elif func in ['rm', 'rem', 'remove', 'delete', 'del']:
            results = self.bot.query_db(f'''SELECT self_roles FROM settings WHERE guildid={ctx.guild.id};''')
            selfroles = json.loads(results[0][0].replace("'", '"')) if results and results[0][0] else json.loads('{}')
            try:
                del selfroles[name]
            except KeyError:
                return await ctx.send(resolve_emoji('ERROR', ctx) + f' There is no self role with the name `{name}`')
            self.bot.query_db(f'''UPDATE settings SET self_roles="{str(selfroles)}" WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully removed self role **{name}**.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Invalid function, check `{ctx.prefix}help {ctx.command}`')

    @commands.command()
    @commands.cooldown(30, 1, commands.BucketType.guild)
    @commands.check(can_manage)
    async def autorole(self, ctx, *, role: str):
        """Set the guild autorole (the role that will be assigned on member join).
        Use `reset` as an argument to reset the autorole."""
        r = resolve_role(role, ctx)
        if r:
            if r.is_default():
                return await ctx.send(
                    resolve_emoji('ERROR', ctx) + ' You cannot set the default everyone role as an autorole.')
            if r.position >= ctx.author.top_role.position:
                return await ctx.send(
                    resolve_emoji('ERROR', ctx) + ' You cannot manage a role higher than your own.')
            self.bot.query_db(f'''INSERT INTO settings (guildid,autorole) VALUES ({ctx.guild.id},{r.id})
                                ON DUPLICATE KEY UPDATE autorole={r.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Set the guild autorole to **{r.name}**.')
        elif r == 'reset':
            self.bot.query_db(f'''UPDATE settings SET autorole=NULL WHERE guildid={ctx.guild.id};''')
            await ctx.send(resolve_emoji('SUCCESS', ctx) + ' Successfully reset your autorole.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + f' Role "{role}" not found.')


def setup(bot):
    bot.add_cog(Settings(bot))
