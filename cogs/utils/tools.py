import config


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
    for p in config.prefix:
        prefixes.append(p)
    try:
        pref = bot.prefixes[str(msg.guild.id)]
        if not pref is None and not len(pref) == 0 and not pref == "":
            prefixes.append(pref)
    except KeyError:
        pass
    return prefixes