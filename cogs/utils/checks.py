from discord.ext.commands import CommandError, check


class ChannelNotNSFW(CommandError):
    pass


def is_nsfw():
    def pred(ctx):
        if ctx.channel.is_nsfw():
            return True
        else:
            raise ChannelNotNSFW("This channel is not marked as NSFW.")
    return check(pred)