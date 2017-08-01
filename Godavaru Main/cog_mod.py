import discord
from discord.ext import commands
import time

class Mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kick(self, ctx):
        if ctx.message.server.me.server_permissions.kick_members == True:
            if ctx.message.author.server_permissions.kick_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to kick.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            args = ctx.message.content
                            args = args.replace(self.bot.command_prefix+"kick <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix+"kick <@!"+ctx.message.mentions[0].id+">", "")
                            if args == "":
                                await self.bot.kick(ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            else:
                                await self.bot.kick(ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason:"+str(args))
                        except Exception as e:
                            await self.bot.say(":x: I can't kick someone equal to or higher than me.")
                    else:
                        await self.bot.say(":x: You can't kick someone equal to or higher than yourself.")
            else:
                await self.bot.say(":x: You cannot kick members.")
        else:
            await self.bot.say(":x: I cannot kick members.")

    @commands.command(pass_context=True)
    async def ban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to ban.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            args = ctx.message.content
                            args = args.replace(self.bot.command_prefix+"ban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix+"ban <@!"+ctx.message.mentions[0].id+">", "")
                            if args == "":
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.say(":white_check_mark: Banned **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            else:
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.say(":white_check_mark: Banned **"+str(ctx.message.mentions[0])+"** with reason:"+str(args))
                        except Exception as e:
                            await self.bot.say(":x: I can't ban someone equal to or higher than me.")
                    else:
                        await self.bot.say(":x: You can't ban someone equal to or higher than yourself.")
            else:
                await self.bot.say(":x: You cannot ban members.")
        else:
            await self.bot.say(":x: I cannot ban members.")

    @commands.command(pass_context=True)
    async def softban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to softban.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            args = ctx.message.content
                            args = args.replace(self.bot.command_prefix+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix+"softban <@!"+ctx.message.mentions[0].id+">", "")
                            if args == "":
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.unban(ctx.message.server, ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Softbanned **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            else:
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=1)
                                await self.bot.unban(ctx.message.server, ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Softbanned **"+str(ctx.message.mentions[0])+"** with reason:"+str(args))
                        except Exception as e:
                            await self.bot.say(":x: I can't softban someone equal to or higher than me.")
                    else:
                        await self.bot.say(":x: You can't softban someone equal to or higher than yourself.")
            else:
                await self.bot.say(":x: You cannot ban members.")
        else:
            await self.bot.say(":x: I cannot ban members.")
        
def setup(bot):
    bot.add_cog(Mod(bot))
