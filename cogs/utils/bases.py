import discord
import datetime


class ModLog(discord.Embed):
    def __init__(self, action: str, mod: discord.Member, user: discord.User or discord.Member, case: int, reason: str = None):
        super().__init__()
        self.types = {
            'unban': 0x00ff00,
            'unmute': 0x00ff00,
            'warn': 0xffff00,
            'mute': 0xffaa00,
            'kick': 0xffaa00,
            'ban': 0xff0000,
            'hackban':0xff0000
        }
        if action not in self.types.keys():
            return
        self.set_author(name=f'{mod} ({mod.id})', icon_url=mod.avatar_url)
        self.description(f'**User:** {user} ({user.id})\n**Action:** {action.capitalize()}\n**Reason:** '
                         + reason if reason else f'Not set, responsible moderator please do `g_reason {case} <reason>`')
        self.set_footer(text=f'Case #{case}')
        self.timestamp = datetime.datetime.now()
