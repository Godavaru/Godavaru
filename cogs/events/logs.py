from ..utils.db import get_log_channel
from ..utils.tools import resolve_emoji, escape_markdown


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
                msg += '\n-' + '\n-'.join(r_roles)
            if len(a_roles) > 0:
                msg += '\n+' + '\n+'.join(a_roles)
            if msg != '':
                await channel.send(resolve_emoji('WARN', channel)
                                   + f' Roles for **{after}** updated.\n'
                                   + f'```diff{escape_markdown(msg, True)}\n```')


def setup(bot):
    bot.add_cog(Logs(bot))
