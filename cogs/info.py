import datetime
import platform
import time
import discord

from discord.ext import commands

import config
from cogs.utils.tools import resolve_emoji

about_description = """
**H-hello!~~**
My name is Godavaru, but you can call me Goda, as many people do. I was named after a community server that my mom made when she first started out in discord, but she no longer focuses on it, and rather develops me as an individual project.
Below, you can find a link to the actual support guild for me, where you may tell my mom if I misbehave and throw errors around again. :< Below, you can also find a link to invite me, if you so wish! I promise that I will do you good!
I have quite a few features; I can list them for you now!

**__I come with:__**
-> Action Commands (hug, kiss, and many more)
-> Moderation Commands (ban, kick, prune, and more!)
-> Utility Commands (urbandictionary search, normal dictionary, complex maths, and much more!)
-> Fun Commands (slots, trivia, and other miscellanious features to keep you occupied!)
-> Information Commands (userid lookup, discriminator lookup, role information, and more!)
-> Customisation (set your prefix, enable logging, enable modlogs and even change modlog reasons!)
-> NSFW commands (rule34, yandere, and a fuck action :eyes:)

Check all my commands with `g_help` or `godavaru help`!
"""


def get_pressure(n):
    bar = n / 1000
    return f"{round(bar)} bar | {n} hPA"


def get_wind(n):
    imp = n * 2.2
    return f"{n} m/s | {round(imp)} mph"


def get_temp(n):
    cel = n - 273.15
    fa = n * 9 / 5 - 459.67
    return f"{round(cel)} °C | {round(fa)} °F"


class Info:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roleinfo(self, ctx, *, role: discord.Role = None):
        """Get information on a role.
        Note that the role name is case sensitive. If the role name is `Member`, then you must pass the role argument as `Member` and not `member`."""
        if role is None:
            role = ctx.author.top_role
        em = discord.Embed(title="Role Info", description="Information for role **{}**".format(role.name),
                           color=role.color)
        em.add_field(name="Permissions", value=role.permissions.value, inline=True)
        em.add_field(name="Colour", value=role.colour, inline=True)
        em.add_field(name="Managed", value=role.managed, inline=True)
        em.add_field(name="Hoisted", value=role.hoist, inline=True)
        em.add_field(name="Role ID", value=role.id, inline=True)
        em.add_field(name="Position", value=role.position, inline=True)
        em.add_field(name="Mentionable", value=role.mentionable, inline=True)
        em.add_field(name="Creation Date", value=role.created_at.strftime('%a %d %b %Y at %H:%M:%S'), inline=True)
        em.set_thumbnail(url="https://i.imgur.com/La0f2NY.png")
        await ctx.send(embed=em)

    @commands.group()
    async def about(self, ctx):
        """Show the stuff about me! I promise I'm interesting uwu"""
        if ctx.invoked_subcommand is None:
            member_count = 0
            server_count = len(self.bot.guilds)
            for server in self.bot.guilds:
                for _ in server.members:
                    member_count += 1
            em = discord.Embed(title='About Godavaru!', description=about_description, color=0x9B59B6)
            em.add_field(name='Version', value=self.bot.version + '\n' + self.bot.version_info, inline=False)
            em.add_field(name='Servers', value=str(server_count))
            em.add_field(name='Users', value=f'{len(self.bot.users)} unique/{member_count} total')
            em.add_field(
                name='Invite Me!',
                value='[Click Here](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)\n[Patreon page](https://www.patreon.com/desii)',
                inline=False)
            em.set_footer(text="Made with love <3")
            await ctx.send(embed=em)

    @about.command()
    async def credits(self, ctx):
        """List the users that have been credited for this bot."""
        creds = {
            '267207628965281792': 'Main developer',
            '99965250052300800': 'Secondary developer',
            '132584525296435200': 'Web Developer',
            '188663897279037440': 'Provided python basic knowledge at the beginning',
            '170991374445969408': 'Helped with early on commands & initial hosting'
        }
        mods = discord.utils.get(self.bot.get_guild(315251940999299072).roles, id=315252093239820289).members
        full_credits = ""
        for key in creds.keys():
            full_credits += f'**{self.bot.get_user(int(key))}** - {creds.get(key)}\n'
        em = discord.Embed(description=full_credits, color=ctx.author.color)
        em.set_author(name='Credited users', icon_url=ctx.me.avatar_url)
        em.add_field(name="Server Moderators", value="**" + "\n".join([str(m) for m in mods]) + "**")
        await ctx.send(embed=em)

    @commands.command(aliases=["links"])
    async def invite(self, ctx, noembed: str = None):
        """Get some important links about me.
        You can also place `noembed` at the end to send a mobile friendly message."""
        if noembed != "noembed" and ctx.channel.permissions_for(ctx.me).embed_links:
            em = discord.Embed(
                description='Here are some useful links for the Godavaru bot. If you have any questions at all, '
                            + f'feel free to join the support guild and tag {self.bot.get_user(267207628965281792)} with your questions!\n'
                            + 'Below you can also find the links to the support guild itself and the Patreon URL. '
                            + 'Thanks for using the bot!',
                color=0x9B59B6)
            em.set_author(
                name='Useful Links for Godavaru!',
                icon_url=ctx.me.avatar_url)
            em.add_field(name='Invite Links', value='[Add Me To Your Server](http://is.gd/godavaru)\n[Join My Support Guild](https://discord.gg/ewvvKHM)')
            em.add_field(name="Patreon URL", value='https://patreon.com/desii')
            em.add_field(name="Github", value="[Godavaru/Godavaru](https://github.com/Godavaru/Godavaru)")
            em.add_field(name="Website", value="https://godavaru.site/")
            em.set_thumbnail(url=ctx.me.avatar_url)
            await ctx.send(embed=em)
        else:
            await ctx.send('**Useful Links for Godavaru!**\n'
                           + 'Here are some useful links for the Godavaru bot. If you have any questions at all,'
                           + ' feel free to join the support guild and tag '
                           + f'{self.bot.get_user(267207628965281792)} with your questions!\n'
                           + 'Below you can also find the links to the support guild itself and the Patreon URL. '
                           + 'Thanks for using the bot!\n\n'
                           + '**Invite:** <http://is.gd/godavaru>\n'
                           + '**Support Guild:** <https://discord.gg/ewvvKHM>\n'
                           + '**Patreon URL:** <https://patreon.com/desii>\n'
                           + '**Github:** <https://github.com/Godavaru/Godavaru>\n'
                           + '**Website:** <https://godavaru.site>')

    @commands.command()
    async def ping(self, ctx):
        """Check my response time and my websocket ping"""
        received = ctx.message.created_at
        send = await ctx.send(":mega: If you see this message you are cool... jk. It's just a ping message.")
        ping = (send.created_at - received).total_seconds() * 1000
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ws = (after - before) * 1000
        await send.edit(
            content=f':mega: Pong! My ping is {round(ping)}ms! `Websocket: {round(ws)}ms`')

    def get_bot_uptime(self, *, brief=False):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command(name="help", aliases=["cmds", "commands", "halp"])
    @commands.bot_has_permissions(embed_links=True)
    async def _help(self, ctx, *, command_or_category: str = None):
        """Shows a list of commands or gives extended help on the command/category you supplied."""
        prefix = ctx.prefix.replace(ctx.me.mention, f'@{ctx.me}')
        if command_or_category:
            cmd = self.bot.all_commands.get(command_or_category)
            if cmd is None:
                if self.bot.get_cog(command_or_category) is None:
                    return await ctx.send(resolve_emoji('ERROR', ctx) + " I did not find that command or category.")
                cmds = sorted(list(self.bot.get_cog_commands(command_or_category)), key=lambda c: c.name)
                if len(cmds) == 0:  # Shouldn't happen, but it's a failsafe
                    return await ctx.send(resolve_emoji('ERROR', ctx) + " There are no commands in that category.")
                msg = ""
                for i in range(len(cmds)):
                    msg += f"`{cmds[i].name}` - {cmds[i].short_doc}\n"
                em = discord.Embed(title=f"Commands in Category {cmds[0].cog_name} - [{len(cmds)}]", description=msg,
                                   color=ctx.author.color)
                em.set_footer(
                    text=f"Requested by {ctx.author.display_name} | For extended help, do {prefix}help <command>",
                    icon_url=ctx.author.avatar_url)
                return await ctx.send(embed=em)
            em = discord.Embed(title="Extended help for command: " + cmd.name, description=cmd.help,
                               color=ctx.author.color)
            comm = cmd.signature.split(' ')[0].split('|')[0].replace('[', '')
            usage = cmd.signature.split(' ')
            del usage[0]
            em.add_field(name="Usage", value=f"`{prefix}{comm} {' '.join(usage)}`", inline=False)
            if len(cmd.aliases) > 0:
                em.add_field(name="Alias(es)", value="`" + "`, `".join(cmd.aliases) + "`", inline=False)
            if hasattr(cmd, 'commands'):
                cmds = sorted(list(cmd.commands), key=lambda c: c.name)
                msg = ""
                for i in range(len(cmds)):
                    msg += f"`{cmds[i].name}` - {cmds[i].short_doc}\n"
                em.add_field(name="Subcommands", value=msg, inline=False)
            em.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=em)
        em = discord.Embed(
            title="Godavaru Help",
            description=f"Here is a list of all of my commands! You can do `{prefix}help <command>` without the brackets for extended help!",
            color=ctx.author.color)
        for cog in sorted(self.bot.cogs):
            if str(cog) == "Owner" and ctx.author.id not in config.owners:
                continue
            cmds = sorted(list(self.bot.get_cog_commands(str(cog))), key=lambda c: c.name)
            if len(cmds) == 0:
                continue
            em.add_field(name=f'[{len(cmds)}] - {cog}', value=f"`{'`, `'.join([c.name for c in cmds])}`", inline=False)
        em.set_footer(text=f"Requested by {ctx.author.display_name} | Total commands: {len(self.bot.commands)}",
                      icon_url=ctx.author.avatar_url)
        em.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command(aliases=['botinfo'])
    async def info(self, ctx):
        """Show some of the more statistical information about me.
        This information includes the current version(s), number of commands, amount of servers, channels, users, uptime, and average websocket ping."""
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping = (after - before) * 1000
        member_count = 0
        channel_count = 0
        for server in self.bot.guilds:
            for _ in server.channels:
                channel_count += 1
            for _ in server.members:
                member_count += 1
        await ctx.send("```prolog\n"
                       + '=========[ Bot Information ]=========\n\n'
                       + f'Commands           :  {len(self.bot.commands)}\n'
                       + f'Cogs               :  {len(self.bot.cogs)}\n'
                       + f'Guilds             :  {len(self.bot.guilds)}\n'
                       + f'Users              :  {member_count}\n'
                       + f'Channels           :  {channel_count}\n'
                       + f'Messages Seen      :  {self.bot.seen_messages}\n'
                       + f'Reconnects         :  {self.bot.reconnects}\n'
                       + f'DB Calls           :  {self.bot.db_calls}\n'
                       + f'Commands Executed  :  {self.bot.executed_commands}\n\n'
                       + '=========[ Technical Information ]=========\n\n'
                       + f'Version            :  {self.bot.version}\n'
                       + f'DiscordPY Version  :  {discord.__version__}\n'
                       + f'Python Version     :  {platform.python_version()}\n'
                       + f'Hostname           :  {platform.node()}\n'
                       + f'OS                 :  {platform.system()}\n'
                       + f'Uptime             :  {self.get_bot_uptime()}\n'
                       + 'Websocket Ping     :  {:.0f}ms\n```'.format(ping))

    @commands.command()
    @commands.cooldown(3, 1, commands.BucketType.user)
    @commands.bot_has_permissions(attach_files=True)
    async def avatar(self, ctx, *, user: discord.Member = None):
        """Get the avatar of a user!
        If the user is none, it will grab your avatar. If the user is not found, this message will be shown."""
        if user is None:
            user = ctx.author
        img = await (await self.bot.session.get(user.avatar_url)).read()
        await ctx.send(content=resolve_emoji('SUCCESS', ctx) + f' **{user.display_name}**\'s avatar!',
                       file=discord.File(img, filename=f'{user.avatar}.{"png" if not user.avatar or not user.avatar.startswith("a_") else "gif"}'))

    @commands.command(aliases=["guild", "ginfo", "server", "serverinfo", "sinfo"])
    async def guildinfo(self, ctx):
        """Get information on the guild you are currently in!"""
        g = ctx.guild
        online = len([m for m in g.members if m.status == discord.Status("online")])
        idle = len([m for m in g.members if m.status == discord.Status("idle")])
        dnd = len([m for m in g.members if m.status == discord.Status("dnd")])
        roles = ", ".join([r.name for r in sorted(g.roles, key=lambda x: -x.position) if not r.is_default()])
        roles_haste = await self.bot.post_to_haste(roles)
        emotes = " ".join([str(e) for e in g.emojis]) if len(g.emojis) > 0 else "No emotes are in this guild."
        emotes_haste = await self.bot.post_to_haste("\n".join([e.name for e in g.emojis]))
        guild_embed = discord.Embed(
            title=g.name,
            description=f"Guild ID: {g.id}",
            color=ctx.author.color
        ).set_thumbnail(
            url=g.icon_url
        ).add_field(
            name="Created At",
            value=g.created_at.strftime("%A %d %B %Y at %H:%M:%S"),
            inline=False
        ).add_field(
            name="Users - " + str(len(g.members)),
            value=f"{resolve_emoji('ONLINE', ctx)} Online: {online}\n"
                  + f"{resolve_emoji('IDLE', ctx)} Idle: {idle}\n"
                  + f"{resolve_emoji('DND', ctx)} DnD: {dnd}",
            inline=False
        ).add_field(
            name="Days Since Creation",
            value=(datetime.datetime.now() - g.created_at).days
        ).add_field(
            name="Guild Region:",
            value=str(g.region).capitalize()
        ).add_field(
            name="AFK Timeout",
            value=f"{int(g.afk_timeout/60)} minutes"
        ).add_field(
            name="Owner",
            value=str(g.owner)
        ).add_field(
            name="Total Channels",
            value=len(g.channels)
        ).add_field(
            name="Category Channels",
            value=len([c.name for c in g.channels if isinstance(c, discord.CategoryChannel)])
        ).add_field(
            name="Text Channels",
            value=len([c.name for c in g.channels if isinstance(c, discord.TextChannel)])
        ).add_field(
            name="Voice Channels",
            value=len([c.name for c in g.channels if isinstance(c, discord.VoiceChannel)])
        ).add_field(
            name="Verification Level",
            value=str(g.verification_level).capitalize()
        ).add_field(
            name="Explicit Content Filter",
            value=str(g.explicit_content_filter).capitalize()
        ).add_field(
            name=f"Roles - {len(g.roles)-1}",
            value=roles if len(roles) < 1000 else f'[Click Me]({roles_haste})'
        ).add_field(
            name=f"Emotes - {len(g.emojis)}",
            value=emotes if len(emotes) < 1000 else f'[Click Me (yes they will look odd)]({emotes_haste})'
        )
        await ctx.send(embed=guild_embed)

    @commands.command(aliases=["user", "uinfo"])
    async def userinfo(self, ctx, *, user: discord.Member = None):
        """Display information about a user."""
        if not user:
            user = ctx.author
        em = discord.Embed(color=user.color)
        em.add_field(name="Joined At:", value=user.joined_at.strftime("%A %d %B %Y at %H:%M:%S"), inline=False)
        em.add_field(name="Created At:", value=user.created_at.strftime("%A %d %B %Y at %H:%M:%S"), inline=False)
        em.add_field(name="Days Since Join:", value=(datetime.datetime.now() - user.joined_at).days)
        em.add_field(name="Days Since Creation:", value=(datetime.datetime.now() - user.created_at).days)
        em.add_field(name="Status:", value=user.status)
        em.add_field(name="Nickname:", value=user.nick)
        em.add_field(name="Voice Channel:", value=user.voice.channel if user.voice is not None else None)
        em.add_field(name="Is Bot:", value=user.bot)
        em.add_field(name="Game:", value=user.activity, inline=False)
        em.add_field(name="Top Role:", value=user.top_role.name)
        em.add_field(name="Highest Position:", value=user.top_role.position)
        em.add_field(name=f"Roles [{len(user.roles) - 1}]:", value=(", ".join(
            [r.name for r in sorted(user.roles, key=lambda x: -x.position) if not r.is_default()])) if len(
            user.roles) > 1 else "This user has no roles.")
        em.set_thumbnail(url=user.avatar_url.replace("?size=1024", ""))
        em.set_author(name=f"{user} ({user.id})", icon_url=user.avatar_url.replace("?size=1024", ""),
                      url=user.avatar_url.replace("?size=1024", ""))
        em.set_footer(text=f"Requested by {ctx.author.display_name}",
                      icon_url=ctx.author.avatar_url.replace("?size=1024", ""))
        await ctx.send(embed=em)

    @commands.command()
    async def weather(self, ctx, *, city: str):
        """Get weather information for a specified city."""
        r = await self.bot.session.get(
            f"http://api.openweathermap.org/data/2.5/weather/?q={city}&APPID={config.weather_token}")
        if (await r.text()).startswith('{"coord"'):
            j = await r.json()
            em = discord.Embed(
                title=f":flag_{j['sys']['country'].lower()}: Weather for {j['name']}, {j['sys']['country']}",
                description=f"{j['weather'][0]['main']} ({j['clouds']['all']}% clouds)",
                color=ctx.author.color
            )

            em.add_field(
                name="🌡 Temperature",
                value=f"Current: { get_temp(j['main']['temp'])}\n"
                      + f"Max: { get_temp(j['main']['temp_max'])}\n"
                      + f"Min: { get_temp(j['main']['temp_min'])}"
            ).add_field(
                name="💧 Humidity",
                value=f"{j['main']['humidity']}%"
            ).add_field(
                name="💨 Wind Speeds",
                value=get_wind(j['wind']['speed'])
            ).add_field(
                name="🎐 Pressure",
                value=get_pressure(j['main']['pressure'])
            ).set_thumbnail(
                url=f"http://openweathermap.org/img/w/{j['weather'][0]['icon']}.png"
            )
            await ctx.send(embed=em)
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + " U-uh, I'm sorry, but that c-city doesn't seem to exist!")

    @commands.command()
    async def status(self, ctx, *, user: discord.Member = None):
        """Display the current status of the specified member.
        If the member is not specified or an invalid member argument is passed, the member is the author."""
        a = " is "
        if not user:
            user = ctx.author
            a = ", you are "
        if user.activity is None:
            return await ctx.send('You are' if user is ctx.author else 'That person is' + ' not playing anything!')
        else:
            game = user.activity
            if game.type == discord.ActivityType.listening:
                b = "listening to:"
            elif game.type == discord.ActivityType.streaming:
                b = "streaming:"
            elif game.type == discord.ActivityType.watching:
                b = "watching:"
            else:
                b = "playing:"  # should only fire an else on playing, but "generally" is not very confident (https://lars-is-the-love.of-my.life/kNCNqh.png)
            em = discord.Embed(title=user.display_name + a + b, description=game.name, colour=user.color)
            if isinstance(game, discord.Spotify):
                em.add_field(name='Title', value='`' + game.title + '`')
                em.add_field(name="Album", value='`' + game.album + '`')
                em.add_field(name="Track ID", value='`' + game.track_id + '`', inline=False)
                em.add_field(name="Party ID", value='`' + game.party_id + '`', inline=False)
                em.add_field(name="Artist" + ("s" if len(game.artists) > 1 else ""),
                             value='`' + "; ".join(game.artists) + '`')
                m, s = divmod((datetime.datetime.utcnow() - game.start).total_seconds(), 60)
                m2, s2 = divmod(game.duration.total_seconds(), 60)
                em.add_field(name="Duration", value="`%02d:%02d/%02d:%02d`" % (m, s, m2, s2))
                em.set_thumbnail(url=game.album_cover_url)
            em.set_footer(text="Hope you enjoy it!")
        await ctx.send(embed=em)

    @commands.command()
    async def changelog(self, ctx, noembed: str = None):
        """Check the most recent changelog for all of the newer features!
        You can also place `noembed` at the end to send a mobile friendly message."""
        changelog_channel = self.bot.get_channel(315602734235516928)
        m = (await changelog_channel.history(limit=1).flatten())[0]
        changelog = m.clean_content
        if noembed != "noembed" and ctx.channel.permissions_for(ctx.me).embed_links:
            em = discord.Embed(description=changelog, color=ctx.author.color)
            em.set_author(icon_url=m.author.avatar_url,
                          name="Found the latest changelog from my support guild!")
            em.timestamp = m.created_at
            await ctx.send(embed=em)
        else:
            await ctx.send("Found the latest changelog from my support guild!\n" + changelog)

    @commands.command()
    async def news(self, ctx, noembed: str = None):
        """Get the latest five messages from my announcements channel!
        You can also place `noembed` at the end to send a mobile friendly message."""
        announcements = self.bot.get_channel(315252885682389012)
        msgs = sorted(await announcements.history(limit=5).flatten(), key=lambda m: m.created_at)
        msg = '\n\n'.join(map(lambda m: f'**{m.author.display_name} ({m.author})**\n{m.clean_content}', msgs))
        if noembed != "noembed" and ctx.channel.permissions_for(ctx.me).embed_links:
            em = discord.Embed(description=msg, color=ctx.author.color)
            em.set_author(icon_url=msgs[0].author.avatar_url,
                          name="The latest five announcements from my support guild!")
            em.timestamp = msgs[0].created_at
            await ctx.send(embed=em)
        else:
            await ctx.send("The latest 5 announcements from my support guild!\n" + msg)


def setup(bot):
    bot.add_cog(Info(bot))
