from discord import Embed, User, Member
import datetime


class ModLog(Embed):
    def __init__(self, action: str, mod: Member, user: User or Member, case: int, reason: str):
        super().__init__()
        self.types = {
            'unban': 0x00ff00,
            'unmute': 0x00ff00,
            'warn': 0xffff00,
            'mute': 0xffaa00,
            'kick': 0xffaa00,
            'softban': 0xffaa00,
            'ban': 0xff0000,
            'hackban': 0xff0000
        }
        if action not in self.types.keys():
            return
        self.set_author(name=f'{mod} ({mod.id})', icon_url=mod.avatar_url)
        self.description = f'**User:** {user} ({user.id})\n**Action:** {action.capitalize()}\n**Reason:** {reason}'
        self.set_footer(text=f'Case #{case}')
        self.timestamp = datetime.datetime.utcnow()
        self.color = self.types[action]


"""class SimpleActionCommand:
    def __init__(self, name, bot, weebsh_name=None):
        self.name = name
        self.bot = bot
        self.weebsh = weebsh_name if weebsh_name else name

    async def run(self, ctx):
        if len(ctx.message.mentions) == 0:
            return await ctx.send(
                get_lang_string('en_US', 'action.no_mentions').format(emote=resolve_emoji('ERROR', ctx)))
        msg = get_lang_string('en_US', 'action.' + self.name).format(author=ctx.author.display_name, members=', '.join(
            [m.display_name for m in ctx.message.mentions])).replace(
            ', ' + ctx.message.mentions[len(ctx.message.mentions) - 1].display_name,
            ' and ' + ctx.message.mentions[len(ctx.message.mentions) - 1].display_name)
        if ctx.author in ctx.message.mentions:
            msg = get_lang_string('en_US', 'action.self_mentions.' + self.name).format(author=ctx.author.display_name)
        gif = await self.bot.weeb.get_image(imgtype=self.weebsh, filetype="gif")
        img = await self.bot.session.get(url=gif[0])
        await ctx.send(content=msg, file=File(img, filename=f"{self.name}-{gif[1]}.gif"))
"""
