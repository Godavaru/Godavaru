import aiohttp
import datetime
import config

class GuildEvents:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, server):
        self.bot.webhook.send(':tada: [`' + str(
            datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")) + '`] I joined the server `' + server.name + '` (' + str(
            server.id) + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + str(
            server.owner.id) + ').')

    async def on_guild_remove(self, server):
        self.bot.webhook.send(f':frowning: [`{datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")}`] I left the server `' + server.name + '` (' + str(
            server.id) + '), owned by `' + str(server.owner) + '` (' + str(
            server.owner.id) + ').')

def setup(bot):
    bot.add_cog(GuildEvents(bot))