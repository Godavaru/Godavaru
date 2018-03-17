import datetime

import discord
from discord.ext import commands


class Mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """Ban a member from the guild.
        You can also supply an optional reason."""
        if not reason:
            reason = "No reason given."
        if ctx.author.top_role.position > member.top_role.position:
            try:
                await ctx.guild.ban(member, reason=reason)
            except discord.Forbidden:
                await ctx.send(
                    f":x: I-I'm sorry, I couldn't ban `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I banned **{member}** successfully.")
        else:
            await ctx.send(":x: I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason: str = None):
        """Ban a member from the guild.
        You can also supply an optional reason."""
        r = reason
        if not reason:
            r = "No reason given."
        if ctx.author.top_role.position > member.top_role.position:
            try:
                await ctx.guild.ban(member, reason=r)
                await ctx.guild.unban(member)
            except discord.Forbidden:
                await ctx.send(
                    f":x: I-I'm sorry, I couldn't ban `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I soft-banned **{member}** successfully.")
        else:
            await ctx.send(":x: I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        """Kick a member from the guild.
        You can also supply an optional reason."""
        r = reason
        if not reason:
            r = "No reason given."
        if ctx.author.top_role.position > member.top_role.position:
            try:
                await ctx.guild.kick(member, reason=r)
            except discord.Forbidden:
                await ctx.send(
                    f":x: I-I'm sorry, I couldn't kick `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I kicked **{member}** successfully.")
        else:
            await ctx.send(":x: I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def hackban(self, ctx, user_id: int, *, reason: str = None):
        """Ban a member by their user ID.
        You can also supply an optional reason."""
        member = await self.bot.get_user_info(user_id)
        r = reason
        if not reason:
            r = "No reason given."
        if member.id in [m.id for m in ctx.guild.members] and ctx.author.top_role.position > discord.utils.get(
                ctx.guild.members, id=member.id).top_role.position or member not in ctx.guild.members:
            try:
                await ctx.guild.ban(member, reason=r)
            except discord.Forbidden:
                await ctx.send(
                    f":x: I-I'm sorry, I couldn't ban `{member}` because my role seems to be lower than theirs.")
                return
            await ctx.send(f":ok_hand: I banned **{member}** successfully.")
        else:
            await ctx.send(":x: I-I'm sorry, but you can't ban someone with a higher role than you!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int, *, reason: str = None):
        """This command allows you to unban a user by their ID."""
        if not reason:
            reason = "No reason given."
        if user_id not in [u.user.id for u in await ctx.guild.bans()]:
            await ctx.send(":x: U-uh, excuse me! That user doesn't seem to be banned!")
            return
        user = await self.bot.get_user_info(user_id)
        await ctx.guild.unban(user, reason=reason)
        await ctx.send(f":ok_hand: I unbanned **{user}** successfully.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def prune(self, ctx, *, number_of_messages: int):
        """Prune a number of messages from a channel.
        Minimum is 3, maximum is 100. If the number is > 100, it will shrink down to 100 for you"""
        if number_of_messages > 100:
            number_of_messages = 100
        if number_of_messages < 3:
            await ctx.send(":x: B-baka! That's too few messages!")
            return
        mgs = []
        async for m in ctx.channel.history(limit=number_of_messages).filter(lambda x: (datetime.datetime.now() - x.created_at).days < 14):
            mgs.append(m)
        try:
            await ctx.channel.delete_messages(mgs)
        except discord.HTTPException:
            await ctx.send(":x: I can't delete messages older than 14 days.\nNote: If you see this message, it is a bug. Please report this.")
            return
        await ctx.send(f":white_check_mark: Deleted `{len(mgs)}` messages!", delete_after=5)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def role(self, ctx, user: discord.Member, *, role: discord.Role):
        """Apply or remove a role from a user.
        If you are searching with username/nickname, you must surround the user in quotations ("). The role field should not have this unless the role name has it."""
        if role.position >= ctx.author.top_role.position:
            await ctx.send(":x: You can't manage roles higher than your highest role.")
        elif role.position >= ctx.me.top_role.position:
            await ctx.send(":x: I can't manage that role.")
        else:
            if role not in user.roles:
                await user.add_roles(role)
                await ctx.send(f":ok_hand: Added the {role.name} role to {user.display_name}")
            else:
                await user.remove_roles(role)
                await ctx.send(f":ok_hand: Removed the {role.name} role from {user.display_name}")


def setup(bot):
    bot.add_cog(Mod(bot))