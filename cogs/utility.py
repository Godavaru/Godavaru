import datetime
import json
import random
import urllib
import pytz
from discord.ext import commands

from cogs.utils.tools import *
from cogs.utils import weeb


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


class Utils:
    def __init__(self, bot):
        self.bot = bot

    def random_colour(self):
        co = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = int(random.random() * len(co))
        b = int(random.random() * len(co))
        c = int(random.random() * len(co))
        d = int(random.random() * len(co))
        e = int(random.random() * len(co))
        f = int(random.random() * len(co))
        col = "{}{}{}{}{}{}".format(co[a], co[b], co[c], co[d], co[e], co[f])
        return discord.Colour(int(col, 16))

    @commands.command(name="time")
    async def _time(self, ctx, *, timezone: str):
        """Determine the current time in a timezone specified.
        The timezone is case sensitive as seen in [this list](https://pastebin.com/B5tLQdEY)."""
        timezone = timezone.upper()
        try:
            if timezone.startswith('GMT'):
                if timezone.startswith('GMT+'):
                    t = timezone.replace('+', '-')
                elif timezone.startswith('GMT-'):
                    t = timezone.replace('-', '+')
                tz = pytz.timezone('Etc/'+t)
            else:
                tz = pytz.timezone(timezone)
            await ctx.send("The time in **{0}** is {1}".format(timezone, datetime.datetime.now(tz).strftime("`%H:%M:%S` on `%d-%b-%Y`")))
        except pytz.UnknownTimeZoneError:
            await ctx.send('Couldn\'t find that timezone, make sure to use one from this list: <https://pastebin.com/B5tLQdEY>\nAlso remember that timezones are case sensitive.')

    @commands.command()
    async def urban(self, ctx, *, params):
        """Search up a word on urban dictionary.
        To get another result for the same argument, simply use `urban <word> -number <int>`"""
        params = params.split(' -number ')
        word = params[0]
        if len(params) > 1:
            try:
                num = int(params[1]) - 1
            except:
                await ctx.send(":x: You gave me an improper number!")
                return
        else:
            num = 0
        r = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
        j = r.json()
        try:
            request = j['list'][num]
        except IndexError:
            await ctx.send(":x: There are no more results.")
            return
        definition = request['definition']
        if len(definition) > 1000:
            definition = definition[997:] + "..."
        if definition == "":
            definition = "None"
        example = request['example']
        if len(example) > 1000:
            example = example[997:] + "..."
        if example == "":
            example = "None"
        em = discord.Embed(description=f"Definition #{num+1}", color=ctx.author.color)
        em.add_field(name="Definition", value=definition, inline=False)
        em.add_field(name="Example", value=example, inline=False)
        em.add_field(name="👍", value=request['thumbs_up'], inline=True)
        em.add_field(name="👎", value=request['thumbs_down'], inline=True)
        em.set_author(name=f"Urban dictionary definition for {word}", url=request['permalink'])
        em.set_footer(text=f"Author: {request['author']}")
        await ctx.send(embed=em)

    @commands.command()
    async def choose(self, ctx, *choices):
        """Choose a random item from a list."""
        if len(choices) < 2:
            await ctx.send(":x: I-I need at least two things to choose!")
            return
        await ctx.send(f":thinking: O-oh, you want me to choose? I guess I choose `{random.choice(choices)}`")

    @commands.command(aliases=["len"])
    async def length(self, ctx, *, string: str):
        """Determine the length of a string.
        Note that this does have a joke if the word "dick" is included. To avoid this, end the string with '--bypass'"""
        if 'dick' in string.lower():
            if not string.lower().endswith('--bypass'):
                await ctx.send("\N{CROSS MARK} That is too " + ("small" if 'lars' not in string.lower() else 'long'))
            else:
                await ctx.send(
                    "\N{WHITE HEAVY CHECK MARK} That string is `{}` characters long (excluding the bypass)".format(
                        len(string) - 9))
        else:
            await ctx.send(f"\N{WHITE HEAVY CHECK MARK} The string you gave me is `{len(string)}` characters long.")

    @commands.command(name="8ball", aliases=['mb', 'magicball'])
    async def _8ball(self, ctx, *, question):
        """Consult the magic 8ball with a question!"""
        url = 'https://8ball.delegator.com/magic/JSON/' + question.replace('/', '\/').replace('.', '\.')
        r = requests.get(url)
        j = r.json()
        q = j['magic']['question']
        a = j['magic']['answer']
        t = j['magic']['type']
        em = discord.Embed(description=f"**Question:** {q}\n**Answer:** {a}\n**Response Type:** {t}", color=0x00ff00)
        em.set_thumbnail(url="https://8ball.delegator.com/images/8ball.png")
        em.set_author(name="You consult the magic 8 ball...", icon_url=ctx.author.avatar_url.replace("?size=1024", ""))
        em.set_footer(text="Powered by 8ball.delegator.com")
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)

    @commands.command()
    async def cat(self, ctx):
        """Get a random cat image!"""
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457,
                   0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        content = [";w; Don't be sad, here's a cat!", "You seem lonely, {0.mention}. Here, have a cat".format(ctx.author),
                   "Meeeooowwww!", "Awww, so cute! Look at the kitty!!1!", "Woof... wait wrong animal."]
        con = int(random.random() * len(content))
        r = requests.get('http://random.cat/meow')
        js = r.json()
        em = discord.Embed(color=colours[col])
        em.set_image(url=js['file'])
        await ctx.send(content=content[con], embed=em)


    @commands.command()
    async def dog(self, ctx):
        """Get a random cat image!"""
        is_video = True
        while is_video:
            r = requests.get('https://random.dog/woof.json')
            js = r.json()
            if js['url'].endswith('.mp4'):
                pass
            else:
                is_video = False
        colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = int(random.random() * len(colours))
        content = [":dog: Don't be sad! This doggy wants to play with you!",
                   "You seem lonely, {0.display_name}. Here, have a dog. They're not as nice as cats, but enjoy!".format(ctx.author),
                   "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait wrong animal."]
        con = int(random.random() * len(content))
        em = discord.Embed(color=colours[col])
        em.set_image(url=js['url'])
        await ctx.send(content=content[con], embed=em)

    @commands.command()
    async def jumbo(self, ctx, emote: str):
        """Get a larger version of a custom emote."""
        e = emote.split(':')
        anim = False
        if e[0] == '<a':
            anim = True
        suffix = ".png"
        if anim is True:
            suffix = ".gif"
        url = f"https://cdn.discordapp.com/emojis/{e[2].replace('>', '')}{suffix}"
        weeb.save_to_image(url=url, name=e[1] + suffix)
        await ctx.send(file=discord.File(f'./images/{e[1]}{suffix}'))
        os.remove(f'./images/{e[1]}{suffix}')

    @commands.command(aliases=["color"])
    async def colour(self, ctx, hexcode: str):
        """Show a preview of a hex colour."""
        colour = hexcode.replace('#', '')
        for char in colour:
            if char not in "abcdef0123456789":
                await ctx.send(":x: T-that's not a valid hex code!")
                return
        if len(colour) != 6:
            await ctx.send(":x: Hex codes are six characters long!")
            return
        c = discord.Color(int(colour, 16))
        em = discord.Embed(color=c)
        em.set_image(url='https://www.colorcombos.com/images/colors/' + colour + '.png')
        em.set_author(name="Here is a preview of your colour.", icon_url=get_friendly_avatar(ctx.author))
        await ctx.send(embed=em)

    @commands.command()
    async def discrim(self, ctx, *, discrim: str):
        """Find users with the discriminator provided.
        If you are unaware, a discriminator is the 4 digit number following your discord name, as seen [here](https://i.imgur.com/kdbY9Nx.png)."""
        discrim = discrim.replace('#')
        num = 0
        msg = ""
        for user in self.bot.users.filter(lambda u: u.discriminator == discrim):
            num += 1
            if num == 6:
                break
            msg += f'{user} ({user.id})\n'
        if msg == "":
            return await ctx.send("Found no users with that discriminator.")
        em = discord.Embed(title="Sorted with: User tag (User id)",description=msg, color=ctx.author.color)
        em.set_author(
            name="First 6 users found matching discriminator #{}".format(discrim),
            icon_url=ctx.author.avatar_url.replace("?size=1024", ""))
        em.set_footer(text="Requested by {}".format(str(ctx.message.author)))
        await ctx.send(embed=em)

    @commands.command()
    async def math(self, ctx, *, expression: str):
        """Evaluate complex mathematical equations (or simple ones, whatever you prefer).
        The available operations are as follows:
        `simplify, factor, derive, integrate, zeroes, tangent, area, cos, tan, arccos, arcsin, arctan, abs, log`"""
        available_endpoints = ["simplify", "factor", "derive", "integrate", "zeroes", "tangent", "area", "cos", "tan", "arccos", "arcsin", "arctan", "abs", "log"]
        oper = expression.split(' -operation ')
        if len(oper) > 1:
            try:
                if oper[1].lower() in available_endpoints:
                    op = oper[1].lower()
                else:
                    return await ctx.send(":x: The operation you gave me was invalid.")
            except:
                return await ctx.send(":x: You never gave me an operation. Check the command help.")
        expr = oper[0].replace('/', '%2F')
        r = requests.get("https://newton.now.sh/"+op+"/"+expr)
        try:
            js = r.json()
        except json.decoder.JSONDecodeError:
            return await ctx.send(":x: I-I'm sorry! Something happened with the api.")
        em = discord.Embed(title="Expression Evaluation",color=ctx.message.author.color)
        em.add_field(name="Operation",value=js['operation'],inline=False)
        em.add_field(name="Expression",value=js['expression'],inline=False)
        em.add_field(name="Result",value=js['result'],inline=False)
        em.set_footer(text="Requested by "+str(ctx.message.author))
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)
        

    @commands.command(aliases=["define"])
    async def dictionary(self, ctx, word: str):
        """Define a word."""
        r = requests.get('http://api.pearson.com/v2/dictionaries/laes/entries?headword='+word)
        js = r.json()
        if len(js['results']) > 0:
            try:
                define = js['results'][0]['senses'][0]['definition'][0]
                pos = js['results'][0]['part_of_speech']
                ex = js['results'][0]['senses'][0]['translations'][0]['example'][0]['text']
                word = js['results'][0]['headword']
                em = discord.Embed(description="**Part Of Speech:** `{1}`\n**Headword:** `{0}`".format(word, pos),color=0x8181ff)
                em.set_thumbnail(url="https://www.shareicon.net/download/2016/05/30/575440_dictionary_512x512.png")
                em.set_footer(text="Requested by {} | Powered by http://api.pearson.com/".format(str(ctx.message.author)))
                em.add_field(name="Definition",value="**{}**".format(define))
                em.add_field(name="Example",value="**{}**".format(ex))
                em.set_author(name="Definition for {}".format(word), icon_url=ctx.message.author.avatar_url.replace('?size=1024', ''))
                await ctx.send(embed=em)
            except KeyError:
                await ctx.send(":x: No results found.")
        else:
            await ctx.send(":x: No results found.")


def setup(bot):
    bot.add_cog(Utils(bot))

    """
        @commands.command(aliases=["nekos"])
        async def catgirls(self, ctx):
            ""\"Get some neko images from nekos.life

            Make sure to specify the second parameter as `nsfw` if you want it to be lewd images. (only in NSFW channels)

            **Usage:** `g_catgirls [nsfw]`

            **Permission:** User""\"
            args = ctx.message.content
            args = args.split(' ')
            if len(args) > 1:
                if args[1] == "nsfw":
                    if ctx.message.channel.is_nsfw():
                        r = requests.get('http://nekos.life/api/lewd/neko')
                        js = r.json()
                        img = js['neko']
                    else:
                        await ctx.send(":x: Can't send lewd/questionable images in a non-nsfw channel.")
                        return
                else:
                    r = requests.get('http://nekos.life/api/neko')
                    js = r.json()
                    img = js['neko']
            else:
                r = requests.get('http://nekos.life/api/neko')
                js = r.json()
                img = js['neko']
            colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
            col = int(random.random() * len(colours))
            em = discord.Embed(color=colours[col])
            em.set_image(url=img)
            await ctx.send(embed=em)
            
    @commands.command(name="permissions",aliases=["perms"])
    async def _permissions(self, ctx):
        ""\"Get a user's server permissions via either mention or id, or leave blank to get your own permissions.

        **Usage:** `g_permissions [user]`

        **Permission:** User""\"
        umsg = ctx.message.content
        args = umsg.split(' ')
        if len(ctx.message.mentions) > 0:
            user = ctx.message.mentions[0]
        else:
            try:
                user = ctx.message.guild.get_member(args[1])
            except (IndexError, discord.NotFound):
                user = ctx.message.author
        em = discord.Embed(title="Server Permissions for {}".format(str(user)),color=user.color)
        emb = discord.Embed(title="Server Permissions for {} (cont.)".format(str(user)),color=user.color)
        up = user.guild_permissions
        # Embed #1
        em.add_field(name="Can create invite",value=up.create_instant_invite)
        em.add_field(name="Can Kick Members",value=up.kick_members)
        em.add_field(name="Can Ban Members",value=up.ban_members)
        em.add_field(name="Is Administrator",value=up.administrator)
        em.add_field(name="Can Manage Channels",value=up.manage_channels)
        em.add_field(name="Can Manage Server",value=up.manage_guild)
        em.add_field(name="Can Add Reactions",value=up.add_reactions)
        em.add_field(name="Can View Audit Logs",value=up.view_audit_log)
        em.add_field(name="Can Read Messages",value=up.read_messages)
        em.add_field(name="Can Send Messages",value=up.send_messages)
        em.add_field(name="Can Send TTS Messages",value=up.send_tts_messages)
        em.add_field(name="Can Manage Messages",value=up.manage_messages)
        em.add_field(name="Can Embed Links",value=up.embed_links)
        em.add_field(name="Can Attach Files",value=up.attach_files)
        em.add_field(name="Can Read Message History",value=up.read_message_history)
        em.add_field(name="Is Owner",value=(ctx.message.guild.owner == user))
        # Embed #2
        emb.add_field(name="Can Mention Everyone",value=up.mention_everyone)
        emb.add_field(name="Can Use External Emojis",value=up.external_emojis)
        emb.add_field(name="Can Connect to VCs",value=up.connect)
        emb.add_field(name="Can Speak in VCs",value=up.speak)
        emb.add_field(name="Can Mute Members",value=up.mute_members)
        emb.add_field(name="Can Deafen Members",value=up.deafen_members)
        emb.add_field(name="Can Move Members",value=up.mute_members)
        emb.add_field(name="Can Change Nickname",value=up.change_nickname)
        emb.add_field(name="Can Manage Nicknames",value=up.manage_nicknames)
        emb.add_field(name="Can Manage Roles",value=up.manage_roles)
        emb.add_field(name="Can Manage Webhooks",value=up.manage_webhooks)
        emb.add_field(name="Can Manage Emojis",value=up.manage_emojis)
        await ctx.send(embed=em)
        await ctx.send(embed=emb)
    
    @commands.command(name="embed")
    async def _embed(self, ctx):
        ""\"Create an embed using the embed builder.

        Note that this feature is 100% experimental and probably will not work. A tutorial will be provided soon.

        **Usage:** `g_embed <args split with an |>`

        **Permission:** User""\"
        umsg = ctx.message.content
        smsg = umsg.split(' ')
        msg = umsg.replace(smsg[0], "")
        msg = msg[1:]
        args = msg.split(' | ')
        if not msg == "":
            for i in range(0, len(args)):
                if args[i].startswith('title:'):
                    t = args[i].replace('title:', "")
                if args[i].startswith('description:'):
                    d = args[i].replace('description:', '')
                if args[i].startswith('color:'):
                    c = args[i].replace('color:', '')
                    co = discord.Color(int(str(c), 16))
            try:
                t
            except NameError:
                t = None
            try:
                d
            except NameError:
                d = None
            try:
                co
            except NameError:
                co = 0x000000
            em = discord.Embed(title=t,description=d,color=co)
            for x in range(0, len(args)):
                if args[x].startswith('addfield:'):
                    addfieldname = args[x].replace('addfield:', "")
                    fieldargs = addfieldname.split(',')
                    if len(fieldargs) > 2:
                        if fieldargs[2] == "False":
                            isInline = False
                        else:
                            isInline = True
                    else:
                        isInline = True
                    em.add_field(name=fieldargs[0],value=fieldargs[1],inline=isInline)
                if args[x].startswith('footer:'):
                    f = args[x].replace('footer:', '')
                    footerargs = f.split(',')
                    if len(footerargs) > 1:
                        iconURL = footerargs[1]
                    else:
                        iconURL = None
                    em.set_footer(icon_url=iconURL,text=footerargs[0])
                if args[x].startswith('image:'):
                    img = args[x].replace('image:', '')
                    em.set_image(url=img)
                if args[x].startswith('thumbnail:'):
                    thumb = args[x].replace('thumbnail:', '')
                    em.set_thumbnail(url=thumb)
                if args[x].startswith('author:'):
                    auth = args[x].replace('author:', '')
                    authargs = auth.split(',')
                    if len(authargs) > 1:
                        iconURL = authargs[1]
                    else:
                        iconURL = None
                    em.set_author(name=authargs[0],icon_url=iconURL)
            await ctx.send(embed=em)
        else:
            await ctx.send(":x: You need at least one argument, split with `|` (guide coming soon)")
"""

