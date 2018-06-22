import pymysql
import config
from discord import Guild, TextChannel
from discord.ext.commands import Bot
from discord.utils import get


def get_all_prefixes():
    db = pymysql.connect(config.db_ip, config.db_user, config.db_pass, config.db_name)
    cur = db.cursor()
    cur.execute(f'SELECT * FROM settings')
    results = cur.fetchall()
    d = dict()
    for row in results:
        d[str(row[0])] = row[1]
    db.close()
    return d


def get_blacklist(bot):
    results = bot.query_db('SELECT * FROM blacklist')
    d = dict()
    for row in results:
        d[str(row[0])] = row[1]
    return d


def get_log_channel(bot: Bot, guild: Guild) -> TextChannel or None:
    """Get the log channel of the given guild.

    Args:
        bot (Bot): The ``Bot`` or a subclass of ``Bot`` such as ``AutoShardedBot`` or custom made.
        guild (Guild): The ``Guild`` to get the log channel from.

    Returns:
          A ``TextChannel`` or ``NoneType``.
    """
    query = bot.query_db(f'''SELECT log_channel FROM settings WHERE guildid={guild.id};''')
    if query and query[0][0]:
        return get(guild.channels, id=int(query[0][0]))

default_profile_values = [None, None, 0, None, 0, None]