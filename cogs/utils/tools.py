# This tools.py file is directly taken from the RubyRoseBot.
# It is simply for being able to do things unable to do normally
# All credit goes to ZeroEpoch1969.
# Github link: https://github.com/ZeroEpoch1969/RubyRoseBot
# The file has been edited as I may have needed, but I do not claim ownership
# of this file.

import io
import re

import discord
import requests

_USER_ID_MATCH = re.compile(r"<@(\d+)>")

_EMOTE_MATCH = re.compile(r"<:(.+?):(\d+)>")

py = "```py\n{}```"

xl = "```xl\n{}```"

diff = "```diff\n{}```"


def write_file(filename, contents):
    with open(filename, "w", encoding="utf8") as file:
        for item in contents:
            file.write(str(item))
            file.write("\n")


def download_file(url, destination):
    req = requests.get(url)
    file = open(destination, "wb")
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()


def extract_emote_id(arg):
    match = _EMOTE_MATCH.match(arg)
    if match:
        return str(match.group(2))


def extract_emote_name(arg):
    match = _EMOTE_MATCH.match(arg)
    if match:
        return str(match.group(1))


def get_avatar(user, animate=True):
    if user.avatar_url:
        avatar = user.avatar_url
    else:
        avatar = user.default_avatar_url
    if not animate:
        avatar = avatar.replace(".gif", ".png")
    return avatar


def make_message_embed(author, color, message, *, formatUser=False, useNick=False):
    if formatUser:
        name = str(author)
    elif useNick:
        name = author.display_name
    else:
        name = author.name
    embed = discord.Embed(color=color, description=message)
    embed.set_author(name=name, icon_url=get_avatar(author))
    return embed


def remove_html(string):
    return string.replace('&amp;', '&').replace("&lt;", '<').replace("&gt;", '>').replace('&quot;', '"').replace(
        '&#039;', "'")


def make_list_embed(fields):
    embed = discord.Embed(description="\u200b")
    for key, value in fields.items():
        embed.add_field(name=key, value=value, inline=True)
    return embed


def format_time(time):
    return time.strftime("%B %d, %Y at %I:%M:%S %p")


def convert_to_bool(arg):
    arg = str(arg).lower()
    if arg in ["yes", "y", "true", "t", "1", "enable", "on"]:
        return True
    elif arg in ["no", "n", "false", "f", "0", "disable", "off"]:
        return False
    else:
        raise ValueError


def strip_global_mentions(message, ctx=None):
    if ctx:
        perms = ctx.message.channel.permissions_for(ctx.message.author)
        if perms.mention_everyone:
            return message
    remove_everyone = re.compile(re.escape("@everyone"), re.IGNORECASE)
    remove_here = re.compile(re.escape("@here"), re.IGNORECASE)
    message = remove_everyone.sub("everyone", message)
    message = remove_here.sub("here", message)
    return message


def format_number(number):
    return "{:,d}".format(number)


def url_to_bytes(url):
    data = requests.get(url)
    content = io.BytesIO(data.content)
    filename = url.rsplit("/", 1)[-1]
    return {"content": content, "filename": filename}


def get_json_from_url(url, headers=None):
    r = requests.get(url, headers=headers)
    return r.json()


def get_status_emoji(status, number):
    global array
    if status == "online":
        array = [
            "💚",
            "<:online:398856032392183819>"
        ]
    elif status == "idle":
        array = [
            "💛",
            "<:idle:398856031360253962>"
        ]
    elif status == 'dnd':
        array = [
            "❤",
            "<:dnd:398856030068670477>"
        ]
    return str(array[number])
