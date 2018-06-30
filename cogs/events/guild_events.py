import datetime


class GuildEvents:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, server):
        if str(server.id) in self.bot.blacklist.keys():
            self.bot.webhook.send(f':warning: Tried to join server `{server}` (`{server.id}`) owned by `{server.owner}` '
                                  + f'(`{server.owner.id}`) but it was blacklisted for: `{self.bot.blacklist[str(server.id)]}`')
            return await server.leave()
        self.bot.webhook.send(f':tada: [`{datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")}`] '
                              + f'I joined the server `{server.name}` ({server.id}), owned by `'
                              + f'{server.owner}` ({server.owner.id}) with `{len(server.members)}` members.')

    async def on_guild_remove(self, server):
        if str(server.id) in self.bot.blacklist.keys():
            return
        self.bot.webhook.send(f':frowning: [`{datetime.datetime.now().strftime("%H:%M:%S")}`] '
                              + f'I left the server `{server.name}` ({server.id}), owned by `'
                              + f'{server.owner}` ({server.owner.id})with `{len(server.members)}` members.')


def setup(bot):
    bot.add_cog(GuildEvents(bot))
