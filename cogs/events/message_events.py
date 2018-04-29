import config
import random
import datetime


class MessageEvents:
    def __init__(self, bot):
        self.bot = bot

    async def on_message_edit(self, before, after):
        if after.guild.name is not None and str(after.content) != str(
                before.content) and before.author.bot is False:
            await self.bot.process_commands(after)

def setup(bot):
    @bot.listen("on_message")
    async def message_event(message):
        bot.seen_messages += 1
        channel = message.channel
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
                await channel.send(random.choice(prefix_messages))
            if message.author.id not in config.blacklist:
                await bot.process_commands(message)
        if not message.author.bot:
            if message.guild is None:
                await message.channel.send(
                    "Hey! Weirdo! Stop sending me dms. If you're trying to use commands, use it in a server.")
                bot.webhook.send(content="[`" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "`][`Godavaru`]\n"
                                          + "[`CommandHandler`][`InterceptDirectMessage`]\n"
                                          + "[`AuthorInformation`]: {} ({})\n".format(str(message.author),
                                                                                      str(message.author.id))
                                          + "[`MessageInformation`]: {} ({})\n".format(message.clean_content,
                                                                                       str(message.id))
                                          + "Intercepted direct message and sent alternate message.")
                print("[" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "][Godavaru]\n"
                      + "[CommandHandler][InterceptDirectMessage]\n"
                      + "[AuthorInformation]: {} ({})\n".format(str(message.author), str(message.author.id))
                      + "[MessageInformation]: {} ({})\n".format(message.clean_content, str(message.id))
                      + "Intercepted direct message and sent alternate message.\n")
                return
    bot.add_cog(MessageEvents(bot))