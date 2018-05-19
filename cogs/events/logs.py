from ..utils.db import get_log_channel
from ..utils.tools import resolve_emoji, escape_markdown


class Logs:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_delete(self, message):
        channel = get_log_channel(self.bot, message.guild)
        if channel and channel.permissions_for(message.guild.me).send_messages:
            content = '\n-'.join(escape_markdown(message.clean_content, True).split('\n'))
            await channel.send(resolve_emoji('INFO', message)
                               + f' Message by **{message.author}** was deleted in {message.channel}\n'
                               + f'```diff{content}\n```')

def setup(bot):
    bot.add_cog(Logs(bot))