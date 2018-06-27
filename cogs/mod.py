import datetime

import discord
from discord.ext import commands
from .utils.bases import ModLog
from .utils.tools import resolve_emoji, process_modlog, parse_flags


class Mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """Ban a member from the guild.
        You can also supply an optional reason.
        Add `--delete-days <day>` to the end to add an amount of days to delete."""
        if ctx.author.top_role.position > member.top_role.position:
            days = 7
            flags = parse_flags(reason)
            if flags.get('delete-days'):
                try:
                    days = int(flags.get('delete-days'))
                except ValueError:
                    days = 7
            if days > 7:
                days = 7
            if days < 0:
                days = 0
            reason = reason.split('--delete-days')[0] if reason else None
            try:
                await ctx.guild.ban(member, reason=reason, delete_message_days=days)
            except discord.Forbidden:
                await ctx.send(
                    f"{resolve_emoji('ERROR', ctx)} I-I'm sorry, I couldn't ban `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I banned **{member}** successfully.")
            await process_modlog(ctx, self.bot, 'ban', member, reason)
        else:
            await ctx.send(
                resolve_emoji('ERROR', ctx) + " I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason: str = None):
        """Kick a member from the guild and clean messages from the last 7 days.
        You can also supply an optional reason.
        Add `--delete-days <day>` to the end to add an amount of days to delete."""
        if ctx.author.top_role.position > member.top_role.position:
            days = 7
            flags = parse_flags(reason)
            if flags.get('delete-days'):
                try:
                    days = int(flags.get('delete-days'))
                except ValueError:
                    days = 7
            if days > 7:
                days = 7
            if days < 0:
                days = 0
            reason = reason.split('--delete-days')[0] if reason else None
            try:
                await ctx.guild.ban(member, reason=f'Responsible Moderator: {ctx.author} | Reason: ' + (
                    reason if reason else 'No reason specified.'), delete_message_days=days)
                await ctx.guild.unban(member)
            except discord.Forbidden:
                await ctx.send(
                    resolve_emoji('ERROR',
                                  ctx) + f" I-I'm sorry, I couldn't ban `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I soft-banned **{member}** successfully.")
            await process_modlog(ctx, self.bot, 'softban', member, reason)
        else:
            await ctx.send(
                resolve_emoji('ERROR', ctx) + " I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        """Kick a member from the guild.
        You can also supply an optional reason."""
        if ctx.author.top_role.position > member.top_role.position:
            try:
                await ctx.guild.kick(member, reason=f'Responsible Moderator: {ctx.author} | Reason: ' + (
                    reason if reason else 'No reason specified.'))
            except discord.Forbidden:
                await ctx.send(
                    resolve_emoji('ERROR',
                                  ctx) + f" I-I'm sorry, I couldn't kick `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I kicked **{member}** successfully.")
            await process_modlog(ctx, self.bot, 'kick', member, reason)
        else:
            await ctx.send(
                resolve_emoji('ERROR', ctx) + " I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def hackban(self, ctx, user_id: int, *, reason: str = None):
        """Ban a member by their user ID.
        You can also supply an optional reason."""
        member = await self.bot.get_user_info(user_id)
        if member.id in [m.id for m in ctx.guild.members] and ctx.author.top_role.position > discord.utils.get(
                ctx.guild.members, id=member.id).top_role.position or member not in ctx.guild.members:
            try:
                await ctx.guild.ban(member, reason=f'Responsible Moderator: {ctx.author} | Reason: ' + (
                    reason if reason else 'No reason specified.'))
            except discord.Forbidden:
                await ctx.send(
                    resolve_emoji('ERROR',
                                  ctx) + f" I-I'm sorry, I couldn't ban `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I banned **{member}** successfully.")
            await process_modlog(ctx, self.bot, 'hackban', member, reason)
        else:
            await ctx.send(
                resolve_emoji('ERROR', ctx) + " I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int, *, reason: str = None):
        """This command allows you to unban a user by their ID."""
        if user_id not in [u.user.id for u in await ctx.guild.bans()]:
            await ctx.send(resolve_emoji('ERROR', ctx) + " U-uh, excuse me! That user doesn't seem to be banned!")
            return
        user = await self.bot.get_user_info(user_id)
        await ctx.guild.unban(user, reason=f'Responsible Moderator: {ctx.author} | Reason: ' + (
            reason if reason else 'No reason specified.'))
        await ctx.send(f":ok_hand: I unbanned **{user}** successfully.")
        await process_modlog(ctx, self.bot, 'unban', user, reason)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def prune(self, ctx, *, number_of_messages: int):
        """Prune a number of messages from a channel.
        Minimum is 3, maximum is 100. If the number is > 100, it will shrink down to 100 for you"""
        if number_of_messages > 100:
            number_of_messages = 100
        if number_of_messages < 3:
            await ctx.send(resolve_emoji('ERROR', ctx) + " B-baka! That's too few messages!")
            return
        mgs = []
        async for m in ctx.channel.history(limit=number_of_messages).filter(
                lambda x: (datetime.datetime.now() - x.created_at).days < 14):
            mgs.append(m)
        try:
            await ctx.channel.delete_messages(mgs)
        except discord.HTTPException:
            await ctx.send(resolve_emoji('ERROR',
                                         ctx) + " I can't delete messages older than 14 days.\nNote: If you see this message, it is a bug. Please report this.")
            return
        await ctx.send(resolve_emoji('SUCCESS', ctx) + f" Deleted `{len(mgs)}` messages!", delete_after=5)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def role(self, ctx, user: discord.Member, *, role: discord.Role):
        """Apply or remove a role from a user.
        If you are searching with username/nickname, you must surround the user in quotations ("). The role field should not have this unless the role name has it."""
        if role.position >= ctx.author.top_role.position:
            await ctx.send(resolve_emoji('ERROR', ctx) + " You can't manage roles higher than your highest role.")
        elif role.position >= ctx.me.top_role.position:
            await ctx.send(resolve_emoji('ERROR', ctx) + " I can't manage that role.")
        else:
            if role not in user.roles:
                await user.add_roles(role)
                await ctx.send(f":ok_hand: Added the {role.name} role to {user.display_name}")
            else:
                await user.remove_roles(role)
                await ctx.send(f":ok_hand: Removed the {role.name} role from {user.display_name}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        """Mute a user.
        The muterole must be set in this server to use this."""
        if ctx.author.top_role.position > member.top_role.position:
            query = self.bot.query_db(f'''SELECT muterole FROM settings WHERE guildid={ctx.guild.id};''')
            if query and query[0][0]:
                role = discord.utils.get(ctx.guild.roles, id=int(query[0][0]))
                if role:
                    try:
                        await member.add_roles(role, reason=f'Responsible Moderator: {ctx.author} | Reason: ' + (
                            reason if reason else 'No reason specified.'))
                        await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully muted **{member}**.')
                        await process_modlog(ctx, self.bot, 'mute', member, reason)
                    except discord.Forbidden:
                        await ctx.send(resolve_emoji('ERROR',
                                                     ctx) + ' I don\'t seem to be able to manage the mute role. Make sure my highest role is above the set muterole.')
                else:
                    await ctx.send(
                        resolve_emoji('ERROR', ctx) + ' I can\' seem to find the mute role set. Maybe it was deleted.')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + ' The muterole is not set in this server.')
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + ' You cannot punish members with a higher role than your own.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):
        """Unmute a user.
        The muterole must be set in this server to use this."""
        if ctx.author.top_role.position > member.top_role.position:
            query = self.bot.query_db(f'''SELECT muterole FROM settings WHERE guildid={ctx.guild.id};''')
            if query and query[0][0]:
                role = discord.utils.get(ctx.guild.roles, id=int(query[0][0]))
                if role:
                    try:
                        await member.remove_roles(role, reason=f'Responsible Moderator: {ctx.author} | Reason: ' + (
                            reason if reason else 'No reason specified.'))
                        await ctx.send(resolve_emoji('SUCCESS', ctx) + f' Successfully unmuted **{member}**.')
                        await process_modlog(ctx, self.bot, 'unmute', member, reason)
                    except discord.Forbidden:
                        await ctx.send(resolve_emoji('ERROR',
                                                     ctx) + ' I don\'t seem to be able to manage the mute role. Make sure my highest role is above the set muterole.')
                else:
                    await ctx.send(
                        resolve_emoji('ERROR', ctx) + ' I can\' seem to find the mute role set. Maybe it was deleted.')
            else:
                await ctx.send(resolve_emoji('ERROR', ctx) + ' The muterole is not set in this server.')
        else:
            await ctx.send(
                resolve_emoji('ERROR', ctx) + ' You cannot unpunish members with a higher role than your own.')

    @commands.command()
    async def reason(self, ctx, case: int, *, reason: str):
        """Change the modlog reason for a specific case.
        You must be the responsible moderator or the server owner to do this."""
        try:
            modlog = self.bot.modlogs[str(ctx.guild.id)][str(case)]
        except KeyError:
            return await ctx.send(resolve_emoji('ERROR',
                                                ctx) + ' I couldn\'t find that modlog message, Either it doesn\'t exist or it was so long ago I forgot.')
        if ctx.author.id == modlog['mod'].id or ctx.author.id == ctx.guild.owner.id:
            query = self.bot.query_db(f'''SELECT mod_channel FROM settings WHERE guildid={ctx.guild.id};''')
            if query and query[0][0] and discord.utils.get(ctx.guild.channels, id=int(query[0][0])):
                try:
                    msg = await discord.utils.get(ctx.guild.channels, id=int(query[0][0])).get_message(
                        modlog['message'])
                except discord.NotFound:
                    return await ctx.send(resolve_emoji('ERROR',
                                                        ctx) + ' The message linked to this modlog reason seems to have been deleted.')
                await msg.edit(embed=ModLog(modlog['action'], modlog['mod'], modlog['user'], case, reason))
                await ctx.send(resolve_emoji('SUCCESS', ctx))
            else:
                return await ctx.send(
                    resolve_emoji('ERROR', ctx) + ' There doesn\'t seem to be a mod log channel here.')
        else:
            return await ctx.send(resolve_emoji('ERROR',
                                                ctx) + ' Only the responsible moderator or the server owner can alter modlog reasons.')


def setup(bot):
    bot.add_cog(Mod(bot))
