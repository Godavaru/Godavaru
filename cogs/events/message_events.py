import config
import random
import json
import asyncio
from cogs.utils.tools import resolve_emoji, generate_id


class MessageEvents:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_edit(self, before, after):
        if after.guild.name is not None and after.content != before.content \
                and before.author.bot is False and str(after.author.id) not in self.bot.blacklist.keys():
            await self.bot.process_commands(after)

    async def on_message(self, message):
        self.bot.seen_messages += 1
        if not message.author.bot and message.guild is not None:
            if message.content == message.guild.me.mention:
                prefix = config.prefix[0]
                prefix_messages = [
                    f"H-hi there! If you're trying to use one of my commands, my prefix is `{prefix}`! Use it like: `{prefix}help`",
                    f"Greetings! Attempting to use a command? My prefix is `{prefix}`! For example: `{prefix}help`",
                    f"Hello! Trying to use a command? The prefix I'm using is `{prefix}`! Use it like so: `{prefix}help`",
                    f"I-it's not like I want you to use my commands or anything! B-but if you want, my prefix is `{prefix}`, used like: `{prefix}help`",
                    f"Y-yes? Looks like you were trying to use a command, my prefix is `{prefix}`! Use it like: `{prefix}help`",
                    f"Baka! Don't you know pinging is rude! O-oh, you want to use my commands? Well, the prefix is `{prefix}`. Try it like this: `{prefix}help`"
                ]
                await message.channel.send(random.choice(prefix_messages))
            if str(message.author.id) not in self.bot.blacklist.keys():
                await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(MessageEvents(bot))
