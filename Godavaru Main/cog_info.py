import discord
from discord.ext import commands
import time
import platform
import random
import traceback
import datetime

botVers = "1.2.0"

ownerids = [
    '267207628965281792',
    '99965250052300800',
    '170991374445969408',
    '188663897279037440'
]
helperids = [
    '267207628965281792',
    '99965250052300800',
    '170991374445969408',
    '188663897279037440',
    '296049853056679937'
]
donatorids = [
    "132584525296435200"
]
creditedids = [
    '267207628965281792',
    '99965250052300800',
    '170991374445969408',
    '188663897279037440',
    '132584525296435200',
    '155867458203287552',
    '213466096718708737'
]

class Info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roleinfo(self, ctx):
        try:
            msg = ctx.message.content
            a = msg.split(' ')
            role = msg.replace(a[0], "")
            role = role[1:]
            if role == "":
                await self.bot.say(":x: Specify a role to get.")
                return
            getId = discord.utils.get(ctx.message.server.roles, name=str(role))
            em = discord.Embed(title="Role Info", description="Information for role **{}**".format(getId.name),color=getId.color)
            em.add_field(name="Permissions",value=getId.permissions.value, inline=True)
            em.add_field(name="Colour",value=getId.colour,inline=True)
            em.add_field(name="Managed",value=getId.managed, inline=True)
            em.add_field(name="Hoisted",value=getId.hoist,inline=True)
            em.add_field(name="Role ID",value=getId.id,inline=True)
            em.add_field(name="Position",value=getId.position,inline=True)
            em.add_field(name="Mentionable",value=getId.mentionable,inline=True)
            em.add_field(name="Creation Date",value=getId.created_at.strftime('%a %d %b %Y at %H:%M:%S'),inline=True)
            em.set_thumbnail(url="https://i.imgur.com/La0f2NY.png")
            await self.bot.send_message(ctx.message.channel, embed=em)
        except (discord.NotFound, AttributeError):
            await self.bot.say(":x: I couldn't find that role. Make sure it has capitals in the proper place, as this is case-sensitive.")
            
        
    @commands.command(pass_context = True)
    async def about(self, ctx):
        args = ctx.message.content
        args = args.split(' ')
        member_count = 0
        server_count = len(self.bot.servers)
        for server in self.bot.servers:
            for member in server.members:
                member_count += 1
        abtEm = discord.Embed(title='About Godavaru!', description = "Hello! My name is Godavaru! I am Desiree#3658's very first bot, very much in production still. I hope you enjoy the bot so far!", color=0x9B59B6).add_field(name='Version Number', value='{}'.format(botVers), inline=False).add_field(name='Servers', value=str(server_count)).add_field(name='Users',value=str(member_count) + '\n\n[Invite me](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)\n[Patreon page](https://www.patreon.com/godavaru)', inline=False).set_footer(text="Made with love <3 | Check out g_about credits for special credits.").set_thumbnail(url="https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png")
        try:
            if args[1] == "credits":
                embed = discord.Embed(title="Special Recognition",description=""
                                      +"**Primary Developer:** Desiree#3658\n"
                                      +"**Developers:** Yuvira#7655, AttributeError#2513, and Jonas B.#9089\n"
                                      +"**Sensei:** Yuvira#7655\n"
                                      +"**Inspiration:** Kodehawa#3457 (`and MantaroBot, if it wasn't for that project I probably would never have tried to make a bot`)\n"
                                      +"**Emotional Support:** MrLar#8117 (`has helped me through personal issues, one reason the bot stayed a project of mine`)\n\n"
                                      +"And thanks to everyone who has used the bot. Much love <3",
                                      color=0x1abc9c)
            else:
                embed = abtEm
        except IndexError:
            embed = abtEm
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)


    @commands.command(pass_context = True)
    async def invite(self, ctx):
        embed = discord.Embed(description='Here are some useful links for the Godavaru bot. If you have any questions at all, feel free to join the support guild and tag Desiree#3658 with your questions!\nBelow you can also find the links to the support guild itself and the Patreon URL. Thanks for using the bot!', color=0x9B59B6).set_author(name='Useful Links for Godavaru!', icon_url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Invite URL', value='http://polr.me/godavaru').add_field(name='Support Guild', value='https://discord.gg/ewvvKHM').add_field(name="Patreon URL", value='https://patreon.com/godavaru').add_field(name="Github", value="https://github.com/Desiiii/Godavaru")
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)


    @commands.command(pass_context = True)
    async def request(self, ctx):
        request_channel = discord.Object('316674935898636289')
        request = ctx.message.content[10:] # this command is shit, i need to revamp later (or remove)
        request = request.replace("`", " ")
        if ctx.message.content[12:] != "":
            await self.bot.send_message(request_channel, '__Request from **' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '** in server **'+ctx.message.server.name+'**__: \n```css\n' + request + '```')
            await self.bot.say ("Your request has been received! :slight_smile:")
        else:
            await self.bot.say ("Please specify something to request or make the request longer!")


    @commands.command(pass_context=True)
    async def ping(self, ctx):
        console = discord.Object("316688736089800715")
        before = datetime.datetime.utcnow()
        ping_msg = await self.bot.send_message(console, content=":mega: **Pinging...**")
        ping = (datetime.datetime.utcnow() - before) * 1000
        before2 = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping2 = (after - before2) * 1000
        var = int(random.random() * 5)
        v = ["a", "e", "i", "o", "u"]
        await self.bot.edit_message(ping_msg, new_content=':warning: [`'+str(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))+'`] `' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` checked my ping in the channel `' + ctx.message.channel.name + '` in the server `' + ctx.message.server.name + '`. The result was {:.2f}ms'.format(ping.total_seconds())+" with a websocket ping of {0:.0f}ms".format(ping2))
        await self.bot.send_message(ctx.message.channel, ":mega: P"+v[var]+"ng! The message took **{:.2f}ms**!".format(ping.total_seconds())+" `Websocket: {0:.0f}ms` :thinking:".format(ping2))


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
    

    @commands.command(pass_context = True)
    async def info(self, ctx):
        commands = len(self.bot.commands)
        cogs = len(self.bot.cogs)
        version = discord.__version__
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping = (after - before) * 1000
        pversion = platform.python_version()
        server_count = 0
        member_count = 0
        channel_count = 0
        for server in self.bot.servers:
            server_count += 1
            for channel in server.channels:
                channel_count += 1
            for member in server.members:
                member_count += 1
        await self.bot.say("```prolog\n =========[ Bot Information ]========= \n\nCommands           :  {0}\nCogs               :  {1}\nVersion            :  {2}\nDiscordPY Version  :  {3}\nPython Version     :  {4}\nWebsocket Ping     :  {5:.0f}ms\nUptime             :  {6}".format(commands, cogs, botVers, version, pversion, ping, self.get_bot_uptime()) + "\n\n =========[ Guild Information ]========= \n\nGuilds             :  {0}\nUsers              :  {1}\nChannels           :  {2}\nHost               :  heroku```".format(server_count, member_count, channel_count))

        
    @commands.command(pass_context=True)
    async def avatar(self, ctx):
        mavi = ctx.message.author.avatar_url
        mavi = mavi.replace("gif?size=1024", "gif")
        mavi = mavi.replace("webp?size=1024", "png?size=512")
        mavi = mavi.replace("?size=1024", "?size=512")
        if len(ctx.message.mentions) == 0:
            if mavi == "":
                embed = discord.Embed(title="Your avatar!",description="Click [here]("+ctx.message.author.default_avatar_url+")!",color=ctx.message.author.color).set_image(url=ctx.message.author.default_avatar_url).set_footer(icon_url=ctx.message.author.default_avatar_url, text="Requested by "+ctx.message.author.display_name)
            else:
                embed = discord.Embed(title="Your avatar!",description="Click [here]("+mavi+")!",color=ctx.message.author.color).set_image(url=mavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif len(ctx.message.mentions) > 0:
            yavi = ctx.message.mentions[0].avatar_url
            yavi = yavi.replace("gif?size=1024", "gif")
            yavi = yavi.replace("webp?size=1024", "png?size=512")
            yavi = yavi.replace("?size=1024", "?size=512")
            if yavi == "":
                if mavi == "":
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+ctx.message.mentions[0].default_avatar_url+")!",color=ctx.message.author.color).set_image(url=ctx.message.mentions[0].default_avatar_url).set_footer(icon_url=ctx.message.author.default_avatar_url, text="Requested by "+ctx.message.author.display_name)
                else:
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+ctx.message.mentions[0].default_avatar_url+")!",color=ctx.message.author.color).set_image(url=ctx.message.mentions[0].default_avatar_url).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            else:
                if mavi == "":
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+yavi+")!",color=ctx.message.author.color).set_image(url=yavi).set_footer(icon_url=ctx.message.author.default_avatar_url, text="Requested by "+ctx.message.author.display_name)
                else:
                    embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+yavi+")!",color=ctx.message.author.color).set_image(url=yavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        else:
            await self.bot.send_message(ctx.message.channel, "There was an unexpected error.")
            

    @commands.command(pass_context=True, aliases=["sinfo", "ginfo", "guildinfo"])
    async def serverinfo(self, ctx):
        try: # catch errors via try/except block
            roles = len(ctx.message.server.roles) - 1 # w/ role_list
            created = ctx.message.server.created_at.strftime("%d/%m/%y %H:%M:%S") # 2
            region = ctx.message.server.region # 3
            verification = ctx.message.server.verification_level # 4
            text_channels = len([x for x in ctx.message.server.channels #5
                                 if x.type == discord.ChannelType.text])
            voice_channels = len(ctx.message.server.channels) - text_channels # 5
            online = len([m.status for m in ctx.message.server.members # 6
                          if m.status == discord.Status.online or
                          m.status == discord.Status.idle])
            total_users = len(ctx.message.server.members) # 6
            passed = (ctx.message.timestamp - ctx.message.server.created_at).days # 2
            owner = ctx.message.server.owner # 8
            role_list = ""
            for x in range(0, len(ctx.message.server.roles)): # alone
                if ctx.message.server.roles[x].is_everyone:
                    continue
                if x == len(ctx.message.server.roles) - 1:
                    role_list += ctx.message.server.roles[x].name
                else:
                    role_list += ctx.message.server.roles[x].name + ", "
            # start embed building
            em = discord.Embed(description="Information about the server **{}**".format(ctx.message.server.name),color=ctx.message.author.color)
            em.set_author(name="Server information",icon_url=ctx.message.server.icon_url)
            em.add_field(name="Region",value=str(region),inline=True)
            em.add_field(name="Users",value="{} online/{} total".format(online, total_users),inline=True)
            em.add_field(name="Verification Level",value=str(verification), inline=True)
            em.add_field(name="Channels",value="{} text/{} voice".format(text_channels, voice_channels),inline=True)
            em.add_field(name="Owner",value=str(owner),inline=True)
            em.add_field(name="Owner ID",value=str(owner.id),inline=True)
            em.add_field(name="Created At",value="{}, around {} days ago.".format(created, passed),inline=False)
            if role_list == "":
                em.add_field(name="Roles - "+str(roles),value="None",inline=False)
            elif role_list != "":
                em.add_field(name="Roles - "+str(roles),value=str(role_list),inline=False)
            em.set_thumbnail(url=ctx.message.server.icon_url)
            em.set_footer(text="Server ID: {}".format(ctx.message.server.id))
            await self.bot.send_message(ctx.message.channel, embed=em)
        except Exception as e: # get any error
            await self.bot.say("An unexpected error occurred when running the command! `{}`".format(e)
                          +"\nYou shouldn't receive an error like this."
                          +"\nPlease contact Desiree#3658.")
            

    @commands.command(pass_context=True, aliases=["uinfo", "whois"])
    async def userinfo(self, ctx):
        try: # error catcher p1
            if len(ctx.message.mentions) == 0:
                try:
                    args = ctx.message.content
                    args = args.split(' ')
                    u = int(args[1])
                    try:
                        getInfo = await self.bot.get_user_info(u)
                        user = getInfo
                    except discord.NotFound:
                        user = ctx.message.author
                except IndexError:
                    user = ctx.message.author
                except ValueError:
                    user = ctx.message.author
            else:
                user = ctx.message.mentions[0]
            # wew
            try:
                if user == getInfo:
                    join = "N/A"
                    toprole = "N/A"
                    color = 0x000000
                    vc = "N/A"
                    game = "None or I can't tell."
                    status = "None or I can't tell."
                    roles = "N/A"
                    role_list = "N/A"
            except UnboundLocalError:
                join = user.joined_at.strftime("%d/%m/%y %H:%M:%S")
                toprole = user.top_role.name
                color = user.color
                vc = user.voice_channel
                game = user.game
                status = user.status
                roles = len(user.roles) - 1
                role_list = ""
                for x in range(0, len(user.roles)):
                    if user.roles[x].is_everyone:
                        continue
                    if x == len(user.roles) - 1:
                        role_list += user.roles[x].name
                    else:
                        role_list += user.roles[x].name + ", "
            created = user.created_at.strftime("%d/%m/%y %H:%M:%S")
            uid = user.id
            isbot  = user.bot
            nick = user.display_name
            avatar = user.avatar_url.replace("?size=1024", "")
            defAvi = user.default_avatar_url
            # badges
            badges = ""
            if user.id in creditedids:
                badges = ":star: "+badges
                top = "Credited in `about credits`"
            if user.id in donatorids:
                badges = ":moneybag: "+badges
                top = "Donator"
            if user.id in helperids:
                badges = ":wrench: "+badges
                top = "Support Server Moderator"
            if user.id in ownerids:
                badges = ":tools: "+badges
                top = "Developer"
            if badges == "":
                badges = "None"
                top = "User"
            # start embed creation
            em = discord.Embed(title=str(user)+"'s user info",description="**{}**".format(top),color=color)
            em.add_field(name="Join Date",value=str(join),inline=True)
            em.add_field(name="Account Creation",value=str(created),inline=True)
            em.add_field(name="User ID",value=str(uid),inline=True)
            em.add_field(name="Is Bot",value=str(isbot),inline=True)
            # send badges
            em.add_field(name="Badges",value="{}".format(badges))
            # avatars
            if defAvi == "https://cdn.discordapp.com/embed/avatars/0.png":
                em.add_field(name="Default Avatar",value="<:avi0:343852806563692554> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/1.png":
                em.add_field(name="Default Avatar",value="<:avi1:343852807322992650> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/2.png":
                em.add_field(name="Default Avatar",value="<:avi2:343852808191344640> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/3.png":
                em.add_field(name="Default Avatar",value="<:avi3:343852808610775042> **[Click here!]({})**".format(defAvi))
            elif defAvi == "https://cdn.discordapp.com/embed/avatars/4.png":
                em.add_field(name="Default Avatar",value="<:avi4:343852809340583937> **[Click here!]({})**".format(defAvi))
            # status
            if status == discord.Status.online:
                em.add_field(name="Status", value="Online")
            elif status == discord.Status.idle:
                em.add_field(name="Status", value="Idle")
            elif status == discord.Status.dnd:
                em.add_field(name="Status", value="Do Not Disturb")
            elif status == discord.Status.offline:
                em.add_field(name="Status", value="Offline")
            elif status == "None or I can't tell.":
                em.add_field(name="Status", value=status)
            # nickname
            if user.name == user.display_name:
                em.add_field(name="Nickname",value="None",inline=True)
            elif user.name != user.display_name:
                em.add_field(name="Nickname",value=str(nick),inline=True)
            # standard embed creation
            em.add_field(name="Voice Channel",value=str(vc),inline=True)
            em.add_field(name="Colour",value=str(color),inline=True)
            # top role, game, and role list
            if toprole == "@everyone":
                em.add_field(name="Top Role",value="User has no roles.",inline=True)
            elif toprole != "@everyone":
                em.add_field(name="Top Role",value=str(toprole),inline=True)
            em.add_field(name="Game",value=str(game),inline=False)
            if role_list == "":
                em.add_field(name="Roles - "+str(roles),value="None",inline=False)
            elif role_list != "":
                em.add_field(name="Roles - "+str(roles),value=str(role_list),inline=False)
            # finish embed creation and send
            em.set_thumbnail(url=avatar)
            await self.bot.send_message(ctx.message.channel, embed=em)
        except Exception as e: # error catcher p2
            await self.bot.say("An unexpected error occurred when running the command! `{}`".format(type(e).__name__+": "+str(e))
                          +"\nYou shouldn't receive an error like this."
                          +"\nPlease contact Desiree#3658.")

def setup(bot):
    bot.add_cog(Info(bot))
