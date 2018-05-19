import config
import aiohttp
from discord import Message, Forbidden, Member, User
from discord.ext.commands import Context, Bot
from .bases import ModLog
import string
import random


def remove_html(string):
    return string.replace('&amp;', '&').replace("&lt;", '<').replace("&gt;", '>').replace('&quot;', '"').replace(
        '&#039;', "'")


def get_prefix(bot: Bot, msg: Message) -> list:
    """Get the prefix(es) that the bot will listen to.

    Args:
        bot (Bot): A ``Bot`` object.
        msg (Message): The message to get the guild prefixes for.

    Returns:
        A ``list`` of prefixes that will be used in this server.
    """
    prefixes = []
    prefixes.append(msg.guild.me.mention)
    prefixes.append(msg.guild.me.mention + ' ')
    for p in config.prefix:
        prefixes.append(p)
        prefixes.append(p + ' ')
    try:
        pref = bot.prefixes[str(msg.guild.id)]
        if not pref is None and not len(pref) == 0 and not pref == "":
            prefixes.append(pref)
            prefixes.append(pref + ' ')
    except KeyError:
        pass
    return prefixes


async def get(url, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            return await resp.read()


async def post(url, headers=None, data=None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, data=data) as resp:
            return await resp.read()


def generate_id(size: int = 6, chars: str = string.ascii_uppercase + string.digits) -> str:
    """Generate an ID with the given length and possible characters.
    Mostly used for an error ID.

    Args:
        size (int): The length of the generated ID. (Default: 6)
        chars (str): A ``str`` with all possible characters that the random generator can choose from. (Default: string.ascii_uppercase + string.digits)

    Returns:
        The ``str`` of the generated ID.
    """
    return ''.join(random.choice(chars) for _ in range(size))


def resolve_emoji(emoji: str, msg: Message or Context) -> str:
    """Resolve an emoji that will be sent based on the permissions of the SelfUser.

    Args:
        emoji (str): The emoji type to get.
        msg (Message or Context): The message or context to get the user/channel from.

    Returns:
        The ``str`` of the emoji, an empty string if not found or ``msg`` is not a Message or Context.
    """
    channel = msg.channel
    if isinstance(msg, Message):
        me = msg.guild.me
    elif isinstance(msg, Context):
        me = msg.me
    else:
        return ''
    emojis = {
        'ERROR': ['❌', '<:crossed:402968721515347968>'],
        'SUCCESS': ['✅', '<:check:394001925860884480>'],
        'WARN': ['⚠', '<:warning:394314103604117504>'],
        'TSUNDERE': ['😳', '<:catBaka:389802304808943641>'],
        'ONLINE': ['💚', '<:online:398856032392183819>'],
        'IDLE': ['💛', '<:idle:398856031360253962>'],
        'DND': ['❤', '<:dnd:398856030068670477>']
    }
    num = ~~channel.permissions_for(me).external_emojis
    try:
        return emojis[emoji][num]
    except KeyError:
        return ''


async def process_modlog(ctx: Context, bot: Bot, action: str, member: Member or User, reason: str):
    """Process a modlog for the given context, bot, member, and reason.

    Args:
        ctx (Context): The context object to get the moderator and channel from.
        bot (Bot): A ``Bot`` object.
        action (str): The action that was taken against the user.
        member (Member or User): The member or user that is punished.
        reason (str): The reason for this punishment.
    """
    query = bot.query_db(f'''SELECT mod_channel,last_mod_entry FROM settings 
                                    WHERE guildid={ctx.guild.id};''')
    if query and query[0][0]:
        chan = ctx.guild.get_channel(int(query[0][0]))
        if chan:
            try:
                case = int(query[0][1]) + 1 if query[0][1] else 1
                if not reason:
                    reason = f"No reason specified, responsible moderator, please do `{ctx.prefix}reason {case} <reason>`."
                await chan.send(embed=ModLog(action, ctx.author, member, case, reason))
            except Forbidden:
                await ctx.send(resolve_emoji('ERROR',
                                             ctx) + ' I seem to be unable to send a message in the modlog channel set. Please check my permissions there or ask an Admin to do so.')
