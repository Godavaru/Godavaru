import discord
from discord.ext import commands
import time
import platform
import random
import traceback
import datetime

class Info():
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context = True)
    async def about(self, ctx):
        server_count = 0
        member_count = 0
        for server in self.bot.servers:
            server_count += 1
            for member in server.members:
                member_count += 1
        if ctx.message.content[8:] == "credits":
            embed = discord.Embed(title='Credits!', description='Here are some very honorable mentions for the creation, support, and overall community of the bot!',color=0x9B59B6).add_field(name='First Donator',value='MrLar#8117').add_field(name='Developers',value='Desiree#3658, AttributeError#2513, Yuvira#7842, and Jonas B.#9089').set_footer(text='Hope you enjoy the bot!').set_thumbnail(url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        elif ctx.message.content[8:] == "patreon":
            avatar1 = ctx.message.author.avatar_url
            avatar1 = avatar1.replace("?size=1024", " ")
            embed = discord.Embed(description='Here are all of our Patreon supporters! Thank you!\n\n`MrLar#8117`', color=0x9B59B6).set_author(name='Patrons!', icon_url=avatar1)
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        else:
            embed = discord.Embed(title='About Godavaru!', description = "Hello! My name is Godavaru! I am Desiree#3658's very first bot, very much in production still. I hope you enjoy the bot so far!", color=0x9B59B6).add_field(name='Version Number', value='0.6.5', inline=False).add_field(name='Servers', value=str(server_count)).add_field(name='Users',value=str(member_count) + '\n\n[Invite me](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)\n[Patreon page](https://www.patreon.com/godavaru)', inline=False).set_footer(text="Made with love <3 | Do g!about credits for credits! | Do g!about patreon for our patrons!").set_thumbnail(url="https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png")
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def invite(self, ctx):
        embed = discord.Embed(description='Here are some useful links for the Godavaru bot. If you have any questions at all, feel free to join the support guild and tag Desiree#3658 with your questions!\nBelow you can also find the links to the support guild itself and the Patreon URL. Thanks for using the bot!', color=0x9B59B6).set_author(name='Useful Links for Godavaru!', icon_url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Invite URL', value='http://polr.me/godavaru').add_field(name='Support Guild', value='https://discord.gg/ewvvKHM').add_field(name="Patreon URL", value='https://patreon.com/godavaru')
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def request(self, ctx, server):
        request_channel = discord.Object('316674935898636289')
        request = ctx.message.content[10:]
        request = request.replace("`", " ")
        if ctx.message.content[12:] != "":
            await self.bot.send_message(request_channel, '__Request from **' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '**__: \n```css\n' + request + '```')
            await self.bot.say ("Your request has been received! :slight_smile:")
        else:
            await self.bot.say ("Please specify something to request or make the request longer!")

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        console = discord.Object("316688736089800715")
        before = datetime.datetime.utcnow()
        ping_msg = await self.bot.send_message(ctx.message.channel, content=":mega: **Pinging...**")
        ping = (datetime.datetime.utcnow() - before) * 1000
        before2 = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping2 = (after - before2) * 1000
        var = int(random.random() * 5)
        if (var == 0):
            v = 'a'
        elif (var == 1):
            v = 'e'
        elif (var == 2):
            v = 'i'
        elif (var == 3):
            v = 'o'
        elif (var == 4):
            v = 'u'
        elif (var == 5):
            v = 'y'
        await self.bot.edit_message(ping_msg, new_content=":mega: P"+str(v)+"ng! The message took **{:.2f}ms**!".format(ping.total_seconds())+" `Websocket: {0:.0f}ms` :thinking:".format(ping2))
        await self.bot.send_message(console, '`' + ctx.message.author.name + '#' + ctx.message.author.discriminator + '` checked my ping in the channel `' + ctx.message.channel.name + '` in the server `' + ctx.message.server.name + '`. The result was {:.2f}ms'.format(ping.total_seconds())+" with a websocket ping of {0:.0f}ms".format(ping2))

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
        version = discord.__version__
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        ping = (after - before) * 1000
        pversion = platform.python_version()
        server_count = 0
        member_count = 0
        for server in self.bot.servers:
            server_count += 1
            for member in server.members:
                member_count += 1
        await self.bot.say("```prolog\n --------- Bot Information --------- \n\nCommands: 37\nVersion: 0.6.5\nDiscord.py Version: " + str(version) + "\nPython Version: " + str(pversion) + "\nWebsocket Ping: {0:.0f}ms".format(ping) + "\nUptime: {}".format(self.get_bot_uptime()) + "\n\n --------- Guild Information --------- \n\nGuilds: " + str(server_count) + "\nUsers: " + str(member_count) + "\nHost: Heroku```")
        
    @commands.command(pass_context=True)
    async def avatar(self, ctx):
        mavi = ctx.message.author.avatar_url
        mavi = mavi.replace("?size=1024", "")
        if ctx.message.content == "":
            embed = discord.Embed(title="Your avatar!",description="Click [here]("+mavi+")!",color=ctx.message.author.color).set_image(url=mavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        if len(ctx.message.mentions) > 0:
            yavi = ctx.message.mentions[0].avatar_url
            yavi = yavi.replace("?size=1024", "")
            embed = discord.Embed(title=ctx.message.mentions[0].display_name+"'s avatar!",description="Click [here]("+yavi+")!",color=ctx.message.author.color).set_image(url=yavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        else:
            embed = discord.Embed(title="Your avatar!",description="Click [here]("+mavi+")!",color=ctx.message.author.color).set_image(url=mavi).set_footer(icon_url=mavi, text="Requested by "+ctx.message.author.display_name)
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

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

    @commands.command()
    async def uptime(self):
        await self.bot.say('**Bot Uptime**\nI was  started up `{}` ago.'.format(self.get_bot_uptime()))

def setup(bot):
    bot.add_cog(Info(bot))
