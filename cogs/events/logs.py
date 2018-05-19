from ..utils.db import get_log_channel
from ..utils.tools import resolve_emoji, escape_markdown


class Logs:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self, message):
        channel = get_log_channel(self.bot, message.guild)
        if channel and channel.permissions_for(message.guild.me).send_messages and channel.id != message.channel.id:
            content = '\n-'.join(escape_markdown(message.clean_content, True).split('\n'))
            await channel.send(resolve_emoji('ERROR', message)
                               + f' Message by **{message.author}** was deleted in **{message.channel.mention}**\n'
                               + f'```diff\n-{content}\n```')

    async def on_message_edit(self, before, after):
        channel = get_log_channel(self.bot, after.guild)
        if channel and channel.permissions_for(after.guild.me).send_messages and channel.id != after.channel.id:
            before_content = '\n-'.join(escape_markdown(before.clean_content, True).split('\n'))
            after_content = '\n+'.join(escape_markdown(after.clean_content, True).split('\n'))
            await channel.send(resolve_emoji('WARNING', after)
                               + f' Message by **{after.author}** was edited in **{after.channel.mention}**\n'
                               + f'```diff\n-{before_content}\n+{after_content}\n```')


def setup(bot):
    bot.add_cog(Logs(bot))