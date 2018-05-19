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


def setup(bot):
    bot.add_cog(Logs(bot))
