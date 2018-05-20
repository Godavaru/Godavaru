from ..utils.db import get_log_channel
from ..utils.tools import resolve_emoji, escape_markdown
from discord import TextChannel, VoiceChannel


class Logs:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self, message):
        channel = get_log_channel(self.bot, message.guild)
        if channel and \
                channel.permissions_for(message.guild.me).send_messages and \
                channel.id != message.channel.id and message.content != '':
            content = '\n-'.join(escape_markdown(message.clean_content, True).split('\n'))
            await channel.send(resolve_emoji('ERROR', channel)
                               + f' Message by **{message.author}** was deleted in **{message.channel.mention}**\n'
                               + f'```diff\n-{content}\n```')

    async def on_message_edit(self, before, after):
        channel = get_log_channel(self.bot, after.guild)
        if channel and \
                channel.permissions_for(after.guild.me).send_messages and \
                channel.id != after.channel.id and before.content != after.content:
            before_content = '\n-'.join(escape_markdown(before.clean_content, True).split('\n'))
            after_content = '\n+'.join(escape_markdown(after.clean_content, True).split('\n'))
            await channel.send(resolve_emoji('WARN', channel)
                               + f' Message by **{after.author}** was edited in **{after.channel.mention}**\n'
                               + f'```diff\n-{before_content}\n+{after_content}\n```')

    async def on_member_join(self, member):
        channel = get_log_channel(self.bot, member.guild)
        if channel and channel.permissions_for(member.guild.me).send_messages:
            await channel.send(resolve_emoji('INFO', channel)
                               + f' `{member}` (`{member.id}`) has joined `{member.guild}` (`Member #{len(member.guild.members)}`)')

    async def on_member_remove(self, member):
        channel = get_log_channel(self.bot, member.guild)
        if channel and channel.permissions_for(member.guild.me).send_messages:
            await channel.send(resolve_emoji('INFO', channel)
                               + f' `{member}` (`{member.id}`) has left `{member.guild}` (`Was member #{len(member.guild.members) + 1}`)')

    async def on_member_update(self, before, after):
        channel = get_log_channel(self.bot, after.guild)
        if channel and channel.permissions_for(after.guild.me).send_messages:
            if before.nick != after.nick:
                await channel.send(resolve_emoji('WARN', channel)
                                   + f' Nickname of member **{after}** updated.\n'
                                   + f'```diff\n-{before.nick}\n+{after.nick}\n```')
            r_roles = list(filter(lambda r: r not in after.roles, before.roles))
            a_roles = list(filter(lambda r: r not in before.roles, after.roles))
            msg = ''
            if len(r_roles) > 0:
                msg += '\n-' + '\n-'.join([r.name for r in r_roles])
            if len(a_roles) > 0:
                msg += '\n+' + '\n+'.join([r.name for r in a_roles])
            if msg != '':
                await channel.send(resolve_emoji('WARN', channel)
                                   + f' Roles for **{after}** updated.\n'
                                   + f'```diff{escape_markdown(msg, True)}\n```')

    async def on_guild_role_create(self, role):
        channel = get_log_channel(self.bot, role.guild)
        if channel and channel.permissions_for(role.guild.me).send_messages:
            await channel.send(resolve_emoji('SUCCESS', channel)
                               + f'Role **{role}** was created.\n'
                               + f'```diff\n+ID: {role.id}\n+Name: {role}\nMentionanle: {role.mentionable}\n'
                               + f'+Colour: {role.colour}\n+Permissions: {role.permissions}\n```')

    async def on_guild_role_delete(self, role):
        channel = get_log_channel(self.bot, role.guild)
        if channel and channel.permissions_for(role.guild.me).send_messages:
            await channel.send(resolve_emoji('ERROR', channel)
                               + f'Role **{role}** was deleted.\n'
                               + f'```diff\n-ID: {role.id}\n-Name: {role}\nMentionable: {role.mentionable}\n'
                               + f'-Colour: {role.colour}\n-Permissions: {role.permissions}\n```')

    async def on_guild_role_update(self, before, after):
        channel = get_log_channel(self.bot, after.guild)
        if channel and channel.permissions_for(after.guild.me).send_messages:
            msg = ''
            if before.name != after.name:
                msg += f'\n-Name: {before.name}\n+Name: {after.name}'
            if before.colour != after.colour:
                msg += f'\n-Colour: {before.colour}\n+Colour: {after.colour}'
            if before.permissions != after.permissions:
                msg += f'\n-Permissions: {before.permissions}\n+Permissions: {after.permissions}'
            if before.mentionable is not after.mentionable:
                msg += f'\n-Mentionable: {before.mentionable}\n+Mentionable: {after.mentionable}'
            if msg != '':
                await channel.send(resolve_emoji('WARN', channel)
                                   + f' Role **{after}** was updated.\n'
                                   + f'```diff{msg}\n```')

    async def on_guild_emojis_update(self, guild, before, after):
        channel = get_log_channel(self.bot, guild)
        if channel and channel.permissions_for(guild.me).send_messages:
            after = sorted(after, key=lambda e: e.id)
            before = sorted(before, key=lambda e: e.id)
            added = list(filter(lambda e: e not in before, after))
            removed = list(filter(lambda e: e not in after, before))
            if len(before) != len(after):
                await channel.send(resolve_emoji('ERROR' if len(removed) == 1 else 'SUCCESS', channel)
                                   + f'Emoji `{removed[0].name if len(removed) == 1 else added[0].name}` '
                                   + 'removed' if len(removed) == 1 else 'added: '
                                   + str(removed[0] if len(removed) == 1 else added[0]))
            for i in range(len(after)):
                if after[i].name != before[i].name:
                    await channel.send(resolve_emoji('WARN', channel)
                                       + f'Name of emoji `{before[i].name}` updated to `{after[i].name}`'
                                       + f': {after[i]}')

    async def on_member_ban(self, guild, user):
        channel = get_log_channel(self.bot, guild)
        if channel and channel.permissions_for(guild.me).send_messages:
            await channel.send(resolve_emoji('INFO', channel)
                               + f' ***{user} ({user.id}) just got banned from {guild}.*** '
                               + resolve_emoji('INFO', channel))

    async def on_member_unban(self, guild, user):
        channel = get_log_channel(self.bot, guild)
        if channel and channel.permissions_for(guild.me).send_messages:
            await channel.send(resolve_emoji('SUCCESS', channel)
                               + f' ***{user} ({user.id}) just got unbanned from {guild}.*** '
                               + resolve_emoji('SUCCESS', channel))

    async def on_guild_channel_create(self, channel):
        c = get_log_channel(self.bot, channel.guild)
        if c and c.permissions_for(channel.guild.me).send_messages:
            chan_type = 'text' if isinstance(channel, TextChannel) else ('voice' if isinstance(channel, VoiceChannel) else 'category')
            await c.send(resolve_emoji('SUCCESS', c)
                         + f' Channel **{channel}** was created.\n'
                         + f'```diff\n+Name: {channel}\n+ID: {channel.id}\n+Topic: {channel.topic}\n'
                         + f'+Category: {channel.category}\n+Type: {chan_type}\n```')

    async def on_guild_channel_delete(self, channel):
        c = get_log_channel(self.bot, channel.guild)
        if c and c.permissions_for(channel.guild.me).send_messages:
            chan_type = 'text' if isinstance(channel, TextChannel) else ('voice' if isinstance(channel, VoiceChannel) else 'category')
            await c.send(resolve_emoji('ERROR', c)
                         + f' Channel **{channel}** was deleted.\n'
                         + f'```diff\n-Name: {channel}\n-ID: {channel.id}\n-Topic: {channel.topic}\n'
                         + f'-Category: {channel.category}\n-Type: {chan_type}\n```')

    async def on_guild_channel_update(self, before, after):
        channel = get_log_channel(self.bot, after.guild)
        if channel and channel.permissions_for(after.guild.me).send_messages:
            msg = ''
            if before.name != after.name:
                msg += f'\n-Name: {before.name}\n+Name: {after.name}'
            if before.category != after.category:
                msg += f'\n-Category: {before.category}\n+Category: {after.category}'
            if before.topic != after.topic:
                msg += f'\n-Topic: {before.topic}\n+Topic: {after.topic}'
            if msg != '':
                await channel.send(resolve_emoji('WARN', channel)
                                   + f' Channel **{after}** was updated.\n'
                                   + f'```diff{msg}\n```')


def setup(bot):
    bot.add_cog(Logs(bot))
