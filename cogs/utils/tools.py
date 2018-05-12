import config
import aiohttp
from discord import Message
from discord.ext.commands import Context


def remove_html(string):
    return string.replace('&amp;', '&').replace("&lt;", '<').replace("&gt;", '>').replace('&quot;', '"').replace(
        '&#039;', "'")


def get_status_emoji(status, number):
    status_dict = {
        "online": [
            "💚",
            "<:online:398856032392183819>"
        ],
        "idle": [
            "💛",
            "<:idle:398856031360253962>"
        ],
        "dnd": [
            "❤",
            "<:dnd:398856030068670477>"
        ]
    }
    return status_dict[status][number]


def get_prefix(bot, msg):
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

def resolve_emoji(emoji, msg) -> str:
    """Resolve an emoji that will be sent based on the permissions of the SelfUser.

    Args:
        emoji (str): The emoji type to get.
        msg (discord.Message or discord.ext.commands.Context): The message or context to get the user/channel from.

    Returns:
        The string of the emoji, an empty string if not found or ``msg`` is not a Message or Context.
    """
    channel = msg.channel
    if isinstance(msg, Message):
        me = msg.guild.me
    elif isinstance(msg, Context):
        me = msg.me
    else:
        return ''
    emojis = {
        'ERROR': [
            '❌',
            '<:cross:402968721515347968>'
        ],
        'SUCCESS': [
            '✅',
            '<:check:394001925860884480>'
        ],
        'WARN': [
            '⚠',
            '<:warning:394314103604117504>'
        ],
        'TSUNDERE': [
            '😳',
            '<:catBaka:389802304808943641>'
        ]
    }
    num = ~~channel.permissions_for(me).external_emojis
    try:
        return emojis[emoji][num]
    except KeyError:
        return ''
