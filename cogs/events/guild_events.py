import datetime


class GuildEvents:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, server):
        self.bot.webhook.send(f':tada: [`{datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")}`] '
                              + f'I joined the server `{server.name}` ({server.id}), owned by `'
                              + f'{server.owner}` ({server.owner.id}).')

    async def on_guild_remove(self, server):
        self.bot.webhook.send(f':frowning: [`{datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")}`] '
                              + f'I left the server `{server.name}` ({server.id}), owned by `'
                              + f'{server.owner}` ({server.owner.id}).')

def setup(bot):
    bot.add_cog(GuildEvents(bot))