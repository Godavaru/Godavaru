import asyncio
import datetime
import json
import random
import signal
import string
import sys
import traceback
import urllib
import config

import aiohttp
import discord
import pymysql
import weeb
from discord.ext import commands
from threading import Thread
from flask import Flask, Response, request

from cogs.utils.db import *
from cogs.utils.tools import *

initial_extensions = (
    "cogs.info",
    "cogs.fun",
    "cogs.action",
    "cogs.owner",
    "cogs.mod",
    "cogs.utility",
    "cogs.nsfw",
    "cogs.opts",
    "cogs.currency",
)


class Godavaru(commands.Bot):
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.prefixes = get_all_prefixes()
        super().__init__(command_prefix=get_prefix, case_insensitive=True)
        self.token = 'no u'  # yes this is a necessary change
        self.version = config.version
        self.version_info = config.version_description
        self.remove_command('help')
        self.weeb = weeb.Client(token=config.weeb_token, user_agent='Godavaru/'+self.version+'/'+config.environment)
        self.seen_messages = 0
        self.webhook = discord.Webhook.partial(int(config.webhook_id), config.webhook_token,
                                               adapter=discord.RequestsWebhookAdapter())
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception:
                print(f'Failed to load extension {extension}.')
                print(traceback.format_exc())

    async def post_to_haste(self, content):
        async with aiohttp.ClientSession() as session:
            async with session.post("https://hastepaste.com/api/create", data=f'text={content}&raw=false',
                                    headers={'Content-Type': 'application/x-www-form-urlencoded'}) as resp:
                if resp.status == 200:
                    return await resp.text()
                else:
                    return "Error uploading to hastepaste :("

    # noinspection PyAttributeOutsideInit
    async def on_ready(self):
        startup_message = f"[`{datetime.datetime.now().strftime('%H:%M:%S')}`][`Godavaru`]\n" \
                          + "===============\n" \
                          + 'Logged in as:\n' \
                          + str(self.user) + '\n' \
                          + '===============\n' \
                          + 'Ready for use.\n' \
                          + f'Servers: `{len(self.guilds)}`\n' \
                          + f'Users: `{len(self.users)}`\n' \
                          + '===============\n' \
                          + f'Loaded up `{len(self.commands)}` commands in `{len(self.cogs)}` cogs in `{(datetime.datetime.now() - self.start_time).total_seconds()}` seconds.\n' \
                          + '==============='
        print(startup_message.replace('`', ''))
        self.webhook.send(startup_message)
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()
        is_prod = config.environment == "Production"
        if is_prod:
            self.weeb_types = await self.weeb.get_types()
            while True:
                with open('splashes.txt') as f:
                    splashes = f.readlines()
                await self.change_presence(
                    activity=discord.Game(name=config.prefix[0] + "help | " + random.choice(splashes).format(self.version, len(self.guilds))))
                data = {'server_count': len(self.guilds)}
                dbl_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
                terminal_url = "https://ls.terminal.ink/api/v1/bots/311810096336470017"
                async with aiohttp.ClientSession() as session:
                    await session.post(dbl_url, data=data, headers={'Authorization': config.dbotstoken})
                    await session.post(terminal_url, data=data, headers={'Authorization': config.terminal_token})
                await asyncio.sleep(900)

    async def on_guild_join(self, server):
        self.webhook.send(':tada: [`' + str(
            datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")) + '`] I joined the server `' + server.name + '` (' + str(
            server.id) + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + str(
            server.owner.id) + ').')

    async def on_guild_remove(self, server):
        self.webhook.send(':frowning: [`' + str(
            datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")) + '`] I left the server `' + server.name + '` (' + str(
            server.id) + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + str(
            server.owner.id) + ').')
        guild_count = len(self.guilds)
        headers = {'Authorization': config.dbotstoken}
        data = {'server_count': guild_count}
        api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)

    async def on_message_edit(self, before, after):
        if after.guild.name is not None and str(after.content) != str(
                before.content) and before.author.bot is False:
            await self.process_commands(after)

    async def on_message(self, message):
        self.seen_messages += 1
        channel = message.channel
        if not message.author.bot and message.guild is not None:
            if message.content.lower() == "f":
                if message.author.id == 267207628965281792:
                    await channel.send("You have paid your respects. :eggplant:")
            elif message.content.lower().startswith('aaa'):
                if message.author.id == 132584525296435200:
                    await channel.send("Hey Lars, did you know that you are super cute?")
                elif message.author.id == 267207628965281792:
                    await channel.send("You're cute, Desii.")
            elif message.content == message.guild.me.mention:
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
                await self.process_commands(message)
        if not message.author.bot:
            if message.guild is None:
                await message.channel.send(
                    "Hey! Weirdo! Stop sending me dms. If you're trying to use commands, use it in a server.")
                self.webhook.send(content="[`" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "`][`Godavaru`]\n"
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

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f':x: You seem to be missing the `{", ".join(error.missing_perms)}` permission(s).')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f":x: I need the permission(s) `{', '.join(error.missing_perms)}` to run this command.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(":x: " + str(error))
        elif isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            await ctx.send(
                f':x: You can use this command again in {"%d hours, %02d minutes and %02d seconds" % (h, m, s)}'
                + (" (about now)." if error.retry_after == 0 else "."))
        elif isinstance(error, commands.MissingRequiredArgument) or isinstance(error,
                                                                               commands.BadArgument) or isinstance(
                error, commands.UserInputError):
            await ctx.send(f":x: Improper arguments, check `{ctx.prefix}help {ctx.command}`")
            ctx.command.reset_cooldown(ctx)
        else:
            def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))

            errid = id_generator()
            await ctx.send(
                f":x: Unhandled exception. Report this on my support guild (https://discord.gg/ewvvKHM) with the ID **{errid}**")
            err_msg = f"Unhandled exception on command `{ctx.command}`\n**Content:** {ctx.message.clean_content}\n**Author:** {ctx.author} ({ctx.author.id})\n**Guild:** {ctx.guild} ({ctx.guild.id})\n"
            trace = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
            print(err_msg + f"**Traceback:** ```py\n{trace}\n```")
            try:
                self.webhook.send(err_msg + f"**Traceback:** ```py\n{trace}\n```")
            except discord.HTTPException:
                self.webhook.send(err_msg + '**Traceback:** ' + await self.post_to_haste(trace))


    def gracefully_disconnect(self, signal, frame):
        print("Gracefully disconnecting...")
        self.logout()
        sys.exit(0)

    def query_db(self, query):
        db = pymysql.connect(config.db_ip, config.db_user, config.db_pass, config.db_name, charset='utf8mb4')
        cur = db.cursor()
        cur.execute(query)
        res = cur.fetchall()
        db.commit()
        cur.close()
        db.close()
        return res


bot = Godavaru()
signal.signal(signal.SIGINT, bot.gracefully_disconnect)
signal.signal(signal.SIGTERM, bot.gracefully_disconnect)
"""app = Flask(__name__)

web_resources = {
    "statuses": {
        "OK": 200,
        "UN_AUTH": 401,
        "NO_AUTH": 403
    },
    "content_type": "application/json"
}


@app.route("/dbl", methods=["POST"])
def get_webhook():
    if request.method == 'POST':
        auth = request.headers.get("authorization")
        if not auth:
            return Response(json.dumps({"msg": "Authorization required"}), status=web_resources["statuses"]["NO_AUTH"],
                            mimetype=web_resources["content_type"])
        if auth != config.dbl_auth:
            return Response(json.dumps({"msg": "Unauthorized"}), status=web_resources["statuses"]["UN_AUTH"],
                            mimetype=web_resources["content_type"])

def start_app():
    app.run(port=1034, host="localhost")

Thread(target=start_app).start()"""
bot.run(config.token)