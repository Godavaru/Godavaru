from discord.ext import commands


class ChannelNotNSFW(Exception):
    pass


def is_nsfw():
    def pred(ctx):
        if ctx.channel.is_nsfw():
            return True
        else:
            raise ChannelNotNSFW("This channel is not marked as NSFW.")
    return commands.check(pred)