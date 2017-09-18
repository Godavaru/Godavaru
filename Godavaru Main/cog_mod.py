import os
from discord.ext import commands
import datetime, re
import json
import discord
import asyncio
import random
import time
import platform
import datetime
import inspect

class Mod():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True,aliases=["dc", "getthefuckoutofthatvoicechannel"])
    async def disconnect(self, ctx):
        if ctx.message.server.me.server_permissions.manage_channels == True and ctx.message.server.me.server_permissions.move_members == True:
            if ctx.message.author.server_permissions.move_members == True:
                if len(ctx.message.mentions) > 0:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        if ctx.message.mentions[0].voice_channel is not None:
                            v = await self.bot.create_channel(ctx.message.server, 'wew', type=discord.ChannelType.voice)
                            await self.bot.move_member(ctx.message.mentions[0], v)
                            await self.bot.delete_channel(v)
                            b = ctx.message.content
                            a = b.split(' ')
                            m = b.replace(a[0]+" "+a[1], "")
                            m = m[1:]
                            if m == "":
                                await self.bot.say(":white_check_mark: disconnected {} from their voice channel.".format(str(ctx.message.mentions[0])))
                            else:
                                await self.bot.say(":ok_hand: disconnected {0} from their voice channel. (`{1}`)".format(str(ctx.message.mentions[0]), m))
                        else:
                            await self.bot.say(':x: That person is not in a voice channel.')
                    else:
                        await self.bot.say(':x: You can\'t disconnect someone with a higher than or equal role.')
                else:
                    await self.bot.say(":x: Mention a user.")
            else:
                await self.bot.say(":x: You don't have permission for that.")
        else:
            await self.bot.say(":x: I need the `MANAGE_CHANNELS` permission to do that.")

    @commands.command(pass_context=True)
    async def kick(self, ctx):
        if ctx.message.server.me.server_permissions.kick_members == True:
            if ctx.message.author.server_permissions.kick_members == True:
                if len(ctx.message.mentions) == 0:
                    await self.bot.say(":x: Tell me who to kick.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            msg = ctx.message.content
                            args = msg.split(' ')
                            if args[1] != ctx.message.mentions[0]:
                                await self.bot.say(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                            else:
                                reason = msg.replace(args[0]+" "+args[1]+" ", "")
                                await self.bot.kick(ctx.message.mentions[0])
                                await self.bot.say(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason:"+str(reason))
                            try:
                                if args[2] != "":
                                    await self.bot.kick(ctx.message.mentions[0])
                                    await self.bot.say(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            except IndexError:
                                await self.bot.say(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                        except IndexError:
                            await self.bot.say(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
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
                    umsg = ctx.message.content
                    args = umsg.split(' ')
                    try:
                        uid = int(args[1])
                        try:
                            member = await self.bot.get_user_info(uid)
                        except discord.NotFound:
                            await self.bot.say(":x: That user doesn't exist.")
                        else:
                            reason = umsg.replace(args[0]+" "+args[1], "")
                            if reason == "":
                                await self.bot.http.ban(uid, ctx.message.server.id, delete_message_days=1)
                                await self.bot.say(":white_check_mark: Banned **"+str(member)+"** with reason: Undefined")
                            else:
                                await self.bot.http.ban(uid, ctx.message.server.id, delete_message_days=1)
                                await self.bot.say(":white_check_mark: Banned **"+str(member)+"** with reason: "+str(reason[1:]))
                    except ValueError:
                        await self.bot.say(":x: That is not an ID.")
                    except IndexError:
                        await self.bot.say("Usage: `{}ban <@user/id> [reason]`".format(bot.command_prefix))
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        args = ctx.message.content
                        args = args.replace(bot.command_prefix+"ban <@"+ctx.message.mentions[0].id+">", "")
                        args = args.replace(bot.command_prefix+"ban <@!"+ctx.message.mentions[0].id+">", "")
                        try:
                            days = int(args[1:2])
                            reason = args[3:]
                        except ValueError:
                            days = 0
                            reason = args[1:]
                        if reason != "":
                            try:
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=days)
                                await self.bot.say(":white_check_mark: Banned **"+str(member)+"** with reason: "+str(reason))
                            except discord.Forbidden:
                                await bot.say("I can't ban someone higher or equal to myself.")
                        else:
                            try:
                                await self.bot.ban(ctx.message.mentions[0], delete_message_days=days)
                                await self.bot.say(":white_check_mark: Banned **"+str(member)+"** with reason: Undefined")
                            except discord.Forbidden:
                                await self.bot.say(":x: I can't ban someone higher or equal to myself.")
                    else:
                        await self.bot.say(":x: You can't ban someone higher or equal to yourself.")
            else:
                await self.bot.say(":x: You don't have the permission to do that.")
        else:
            await self.bot.say(":x: I don't have the permission to do that.")
            

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
                            args = args.replace(self.bot.command_prefix[0]+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[0]+"softban <@!"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"softban <@!"+ctx.message.mentions[0].id+">", "")
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
            

    @commands.command(pass_context=True, aliases=["purge", "clean"])
    async def prune(self, ctx):
        args = ctx.message.content
        args = args.split(' ')
        if ctx.message.server.me.server_permissions.manage_messages == True:
            if ctx.message.author.server_permissions.manage_messages == True:
                try:
                    if args[1] != "":
                        try:
                            mgs = [] 
                            number = int(str(args[1]))
                            async for x in self.bot.logs_from(ctx.message.channel, limit=number):
                                mgs.append(x)
                            await self.bot.delete_messages(mgs)
                            prunemsg = await self.bot.say(":white_check_mark: Deleted **{}** messages!".format(number))
                            await asyncio.sleep(5)
                            await self.bot.delete_message(prunemsg)
                        except ValueError:
                            await self.bot.say(":x: That's not a valid number.")
                except IndexError:
                    await self.bot.say(":x: Specify messages to prune.")
            else:
                await self.bot.say(":x: You cannot manage messages.")
        else:
            await self.bot.say(":x: I cannot manage messages.")
            

    @commands.command(pass_context=True)
    async def unban(self, ctx):
        if ctx.message.server.me.server_permissions.ban_members == True:
            if ctx.message.author.server_permissions.ban_members == True:
                try:
                    umsg = ctx.message.content
                    args = umsg.split(' ')
                    uid = int(args[1])
                    try:
                        member = await self.bot.get_user_info(uid)
                    except discord.NotFound:
                        await self.bot.say("I didn't find that user.")
                    else:
                        await self.bot.unban(ctx.message.server, member)
                        await self.bot.say(":white_check_mark: unbanned "+str(member))
                except ValueError:
                    await self.bot.say("That is not an ID.")
                except IndexError:
                    await self.bot.say("Usage: `{}unban <user id>`".format(self.bot.command_prefix))
            else:
                await self.bot.say("You can't manage bans.")
        else:
            await self.bot.say("I can't manage bans.")
        
def setup(bot):
    bot.add_cog(Mod(bot))
