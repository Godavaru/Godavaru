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
    try:
        pref = bot.prefixes_dict[str(msg.guild.id)]
        if not pref is None and not len(pref) == 0 and not pref == "":
            prefixes.append(pref)
    except KeyError:
        pass
    prefixes.append(config.prefix)
    return prefixes