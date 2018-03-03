import datetime
import random
import string
import traceback
import asyncio

import aiohttp
from discord.ext import commands

import config
from cogs.utils.tools import *

initial_extensions = (
    "cogs.info",
    "cogs.fun",
    "cogs.action",
    "cogs.owner",
    "cogs.mod",
    "cogs.utility",
)

class Godavaru(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config.prefix)
        self.start_time = datetime.now()
        self.version = config.version
        self.version_info = config.version_description
        self.remove_command('help')
        self.webhook = discord.Webhook.partial(int(config.webhook_id), config.webhook_token, adapter=discord.RequestsWebhookAdapter())
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception:
                print(f'Failed to load extension {extension}.')
                print(traceback.format_exc())

    async def on_ready(self):
        await self.change_presence(game=discord.Game(name=self.command_prefix[0] + "help | {} guilds".format(len(self.guilds))))
        startup_message = f"[`{datetime.now().strftime('%H:%M:%S')}`][`Godavaru`]\n"\
                          + "===============\n" \
                          + 'Logged in as:\n'\
                          + str(self.user) + '\n'\
                          + '===============\n'\
                          + 'Ready for use.\n'\
                          + f'Servers: `{len(self.guilds)}`\n'\
                          + f'Users: `{len(self.users)}`\n'\
                          + '===============\n'\
                          + f'Loaded up `{len(self.commands)}` commands in `{len(self.cogs)}` cogs in `{(datetime.now() - self.start_time).total_seconds()}` seconds.\n'\
                          + '==============='
        print(startup_message.replace('`', ''))
        self.webhook.send(startup_message)
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.utcnow()
        url = f"https://api.weeb.sh/images/types"
        while True:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers={"Authorization": config.weeb_token}) as resp:
                    j = await resp.json()
                    self.weeb_types = j["types"]
                    await asyncio.sleep(86400)

    async def on_guild_join(self, server):
        server_count = len(self.guilds)
        member_count = 0
        for server in self.guilds:
            for _ in server.members:
                member_count += 1
        await self.change_presence(game=discord.Game(
            name=self.command_prefix[0] + "help | {} guilds with {} members.".format(server_count, member_count)))
        self.webhook.send(':tada: [`' + str(
            datetime.now().strftime("%d/%m/%y %H:%M:%S")) + '`] I joined the server `' + server.name + '` (' + str(
            server.id) + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + str(
            server.owner.id) + ').')
        guild_count = len(self.guilds)
        headers = {'Authorization': config.dbotstoken}
        data = {'server_count': guild_count}
        api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)

    async def on_guild_remove(self, server):
        server_count = len(self.guilds)
        member_count = 0
        for server in self.guilds:
            for _ in server.members:
                member_count += 1
        await self.change_presence(game=discord.Game(
            name=self.command_prefix[0] + "help | {} guilds with {} members.".format(server_count, member_count)))
        self.webhook.send(content=':frowning: [`' + str(datetime.now().strftime(
            "%d/%m/%y %H:%M:%S")) + '`] I left the server `' + server.name + '` (' + server.id + '), owned by `' + server.owner.name + '#' + server.owner.discriminator + '` (' + server.owner.id + ')')
        guild_count = len(self.guilds)
        headers = {'Authorization': config.dbotstoken}
        data = {'server_count': guild_count}
        api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)

    async def on_message_edit(self, before, after):
        if after.content.startswith(self.command_prefix[0]):
            if after.guild.name is not None and str(after.content) != str(before.content) and before.author.bot is False:
                await self.process_commands(after)

    async def on_message(self, message):
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
                prefix = self.command_prefix[0]
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
                self.webhook.send(content="[`" + str(datetime.now().strftime("%H:%M:%S")) + "`][`Godavaru`]\n"
                                     + "[`CommandHandler`][`InterceptDirectMessage`]\n"
                                     + "[`AuthorInformation`]: {} ({})\n".format(str(message.author),
                                                                                 str(message.author.id))
                                     + "[`MessageInformation`]: {} ({})\n".format(message.clean_content, str(message.id))
                                     + "Intercepted direct message and sent alternate message.")
                print("[" + str(datetime.now().strftime("%H:%M:%S")) + "][Godavaru]\n"
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
            await ctx.send(":x: You are not authorized to use this command.")
        else:
            def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            errid = id_generator()
            await ctx.send(f":x: Unhandled exception. Report this on my support guild (https://discord.gg/ewvvKHM) with the ID **{errid}**")
            self.webhook.send(f"Unhandled exception on command `{ctx.command}`\n"
                              + f"**Content:** {ctx.message.clean_content}\n"
                              + f"**Author:** {ctx.author} ({ctx.author.id})\n"
                              + f"**Guild:** {ctx.guild} ({ctx.guild.name})\n"
                              + f"**Traceback:** ```py\n{''.join(traceback.format_exception(type(error), error, error.__traceback__))}\n```")

Godavaru().run(config.token)


"""
                                        =================================
                                        VERSION 1.0 LEFTOVERS STARTS HERE
                                        =================================

@self.event
async def on_command_completion(ctx):
    global commandsExecuted
    commandsExecuted += 1

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@self.event
async def on_command_error(ctx, error):
    errid = id_generator()
    if isinstance(error, commands.CommandNotFound):
        return
    global totalErrors
    totalErrors += 1
    await ctx.send(
        ":x: I ran into an error! Please report this on the support guild with the error ID, which is **{1}**. ```py\n{0}```".format(
            str(error)[29:], errid))
    webhook.send(content="[`" + str(
        datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S")) + "`][`Godavaru`][:x:]\n"
                         + "[`CommandHandler`][`Error`]\n"
                         + "[`ErrorInformation`][`{}`]: {}\n".format(errid, str(error)[29:])
                         + "[`GuildInformation`]: {}\n".format(
        ctx.message.guild.name + " (" + str(ctx.message.guild.id) + ") owned by " + str(
            ctx.message.guild.owner) + " (" + str(ctx.message.author.id) + ")")
                         + "[`AuthorInformation`]: {} ({})\n".format(str(ctx.message.author),
                                                                     str(ctx.message.author.id))
                         + "[`MessageInformation`]: {} ({})\n".format(ctx.message.clean_content, str(ctx.message.id)))
    print("[" + str(datetime.now(pytz.timezone('America/New_York')).strftime("%H:%M:%S")) + "][Godavaru]\n"
          + "[CommandHandler][Error]\n"
          + "[ErrorInformation]: {}\n".format(str(error)[29:])
          + "[GuildInformation]: {}\n".format(
        ctx.message.guild.name + " (" + str(ctx.message.guild.id) + ") owned by " + str(
            ctx.message.guild.owner) + " (" + str(ctx.message.author.id) + ")")
          + "[AuthorInformation]: {} ({})\n".format(str(ctx.message.author), str(ctx.message.author.id))
          + "[MessageInformation]: {} ({})\n".format(ctx.message.clean_content, str(ctx.message.id)))


 help command
@self.command()
async def help(ctx):
    ""\"Shows a list of commands that I have or requests extra help on a command.

    **Usage:** `g_help [command]`

    **Permission:** User""\"
    umsg = ctx.message.content
    args = umsg.split(' ')
    if len(args) > 1:
        cmd = self.all_commands.get(args[1])
        if not cmd:
            await ctx.send(":x: A command with that name doesn't exist.")
            return
        if cmd.hidden:
            await ctx.send(":x: You cannot request help on a hidden command, you baka. Stop being nosy.")
            return
        desc = cmd.help
        if desc is None:
            desc = "There is no extended help set for this command."
        em = discord.Embed(title="Extended help for: {}".format(args[1]),
                           description=desc + "\n\nNote that arguments surrounded with `[]` are not required while arguments surrounded by `<>` are required. Do not include either of these in the command.",
                           color=ctx.message.author.color)
        em.set_thumbnail(url="https://d30y9cdsu7xlg0.cloudfront.net/png/4439-200.png")
        await ctx.send(embed=em)
        return
    em = discord.Embed(title="Godavaru Help",
                       description="The prefix is `{0}`. Do `{0}help <command>` without the brackets for extended help.".format(
                           self.command_prefix[0]), color=ctx.message.author.color)
    em.set_thumbnail(url=ctx.message.guild.me.avatar_url)
    for cog in sorted(self.cogs, key=str.lower):
        if str(cog) == "Owner" and ctx.message.author.id not in ownerids:
            continue
        cog_cmd_number = 0
        cog_commands = ""
        for command in sorted(self.commands, key=lambda x: x.name):
            if command.cog_name == str(cog) and command.hidden == False:
                cog_cmd_number += 1
                cog_commands += "`{}` ".format(str(command))
        if len(cog_commands) > 1024:
            cog_commands = hastebin.post(cog_commands)
        em.add_field(name=str(cog) + " - " + str(cog_cmd_number), value=cog_commands, inline=False)
    no_cog_commands = ""
    no_cog_number = 0
    for command in sorted(self.commands, key=lambda x: x.name):
        if not command.cog_name and command.hidden == False:
            no_cog_commands += "`{}` ".format(str(command))
            no_cog_number += 1
    if len(no_cog_commands) > 1024:
        no_cog_commands = hastebin.post(no_cog_commands)
    em.add_field(name="No Category - " + str(no_cog_number), value=no_cog_commands, inline=False)
    em.set_footer(icon_url=ctx.message.author.avatar_url.replace("?size=1024", ""),
                  text="Requested by {} | Total commands: {}".format(ctx.message.author.display_name,
                                                                     len(self.commands)))
    await ctx.send(embed=em)


@self.command(pass_context=True)
async def stats(ctx):
    ""\"Get statistics about me.

    **Usage:** `g_stats`

    **Permission:** User""\"
    allMembers = 0
   allChannels = 0
    over50 = 0
    over100 = 0
    over500 = 0
    over1000 = 0
    m = []
    c = []
    for server in self.guilds:
        m += [len(server.members)]
        c += [len(server.channels)]
        if len(server.members) > 50:
            over50 += 1
        if len(server.members) > 100:
            over100 += 1
        if len(server.members) > 500:
            over500 += 1
        if len(server.members) > 1000:
            over1000 += 1
        for _ in server.members:
            allMembers += 1
        for _ in server.channels:
            allChannels += 1
    uma = max(m)
    cma = max(c)
    umi = min(m)
    cmi = min(c)
    ua = round(allMembers / len(self.guilds), 2)
    ca = round(allChannels / len(self.guilds), 2)
    em = discord.Embed(title="Well, I did my maths!", color=ctx.message.author.color)
    em.set_thumbnail(url=ctx.message.guild.me.avatar_url)
    em.add_field(name="Messages Seen", value=str(messageCount))
    em.add_field(name="Commands Executed", value=str(commandsExecuted))
    em.add_field(name="Total Errors", value=str(totalErrors))
    em.add_field(name="Guilds", value=str(len(self.guilds)))
    em.add_field(name="Guilds > 50", value=str(over50))
    em.add_field(name="Guilds > 100", value=str(over100))
    em.add_field(name="Guilds > 500", value=str(over500))
    em.add_field(name="Guilds > 1000", value=str(over1000))
    em.add_field(name="Users", value=str(allMembers))
    em.add_field(name="Channels", value=str(allChannels))
    em.add_field(name="Users Per Server", value="Min: {0}\nMax: {1}\nAverage: {2}".format(umi, uma, ua))
    em.add_field(name="Channels Per Server", value="Min: {0}\nMax: {1}\nAverage: {2}".format(cmi, cma, ca))
    await ctx.send(embed=em)


 cog commands
@self.command(hidden=True)
async def load(ctx, extension_name: str):
    if ctx.message.author.id not in ownerids:
        await ctx.send(":x: You do not have permission to execute this command.")
    else:
        try:
            self.load_extension("cog_" + extension_name)
        except Exception as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
           return
        await ctx.send(":white_check_mark: Cog **`{}`** loaded.".format(extension_name))


@self.command(hidden=True)
async def unload(ctx, extension_name: str):
    if ctx.message.author.id not in ownerids:
        await ctx.send(":x: You do not have permission to execute this command.")
    else:
        self.unload_extension("cog_" + extension_name)
        await ctx.send(":white_check_mark: Cog **`{}`** unloaded.".format(extension_name))


@self.command(hidden=True)
async def reload(ctx, extension_name: str):
    if ctx.message.author.id not in ownerids:
        await ctx.send(":x: You do not have permission to execute this command.")
    else:
        try:
            self.unload_extension("cog_" + extension_name)
            self.load_extension("cog_" + extension_name)
        except Exception as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await ctx.send(":white_check_mark: Cog **`{}`** reloaded.".format(extension_name))

 This is a meme now
 @self.command(hidden=True)
 async def test(ctx):
     await ctx.send(
         "hey look, you found a dead meme that isn't even in the help menu. now stop stalking the github :eyes:")

 Mantaro Hub Memes
 @self.command(hidden=True)
 async def lol(ctx):
    if ctx.message.guild.id == 213468583252983809:
        msg = await ctx.send("Searching channels... (this may take a while)")
        l = 0
        for c in ctx.message.guild.channels:
            if isinstance(c, discord.TextChannel):
                if c.permissions_for(ctx.message.guild.me).read_messages:
                    async for m in c.history():
                        if m.author.id == 132584525296435200 and "lol" in m.content.lower():
                            l = l + 1
        await msg.edit(content="Lars' total lol counter so far is: `{}`".format(l))

 force update
 @self.command(hidden=True)
 async def update(ctx):
    if ctx.message.author.id in ownerids:
        guild_count = len(self.guilds)
        headers = {'Authorization': config['Main']['dbotstoken']}
        data = {'server_count': guild_count}
        api_url = 'https://discordbots.org/api/bots/311810096336470017/stats'
        async with aiohttp.ClientSession() as session:
            await session.post(api_url, data=data, headers=headers)
        await ctx.send("Sent stats to discordbots.org")
    else:
        return


 if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            self.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))

 self.remove_command("help")
 self.run(config['Main']['token'])
"""