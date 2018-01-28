# Discord
# Useful
import asyncio

from discord.ext import commands

from cogs.utils.tools import *


# Other

# Code Interpreters
#import js2py

class Mod():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True,aliases=["dc", "getthefuckoutofthatvoicechannel"])
    async def disconnect(self, ctx):
        """Disconnect a user from a voice channel by creating a voice channel, moving the user to it, then deleting it.

        **Usage:** `g_disconnect <user>`

        **Permission:** MOVE_MEMBERS"""
        if ctx.message.guild.me.guild_permissions.manage_channels == True and ctx.message.guild.me.guild_permissions.move_members == True:
            if ctx.message.author.guild_permissions.move_members == True:
                if len(ctx.message.mentions) > 0:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        if ctx.message.mentions[0].voice.channel is not None:
                            v = await ctx.message.guild.create_voice_channel('wew')
                            await ctx.message.mentions[0].move_to(v)
                            await v.delete()
                            b = ctx.message.content
                            a = b.split(' ')
                            m = b.replace(a[0]+" "+a[1], "")
                            m = m[1:]
                            if m == "":
                                await ctx.send(":white_check_mark: disconnected {} from their voice channel.".format(str(ctx.message.mentions[0])))
                            else:
                                await ctx.send(":ok_hand: disconnected {0} from their voice channel. (`{1}`)".format(str(ctx.message.mentions[0]), m))
                        else:
                            await ctx.send(':x: That person is not in a voice channel.')
                    else:
                        await ctx.send(':x: You can\'t disconnect someone with a higher than or equal role.')
                else:
                    await ctx.send(":x: Mention a user.")
            else:
                await ctx.send(":x: You don't have permission for that.")
        else:
            await ctx.send(":x: I need the `MANAGE_CHANNELS` permission to do that.")

    @commands.command(pass_context=True)
    async def kick(self, ctx):
        """Kick a user from the server.

        **Usage:** `g_kick <user> [reason]`

        **Permission:** KICK_MEMBERS"""
        if ctx.message.guild.me.guild_permissions.kick_members == True:
            if ctx.message.author.guild_permissions.kick_members == True:
                if len(ctx.message.mentions) == 0:
                    await ctx.send(":x: Tell me who to kick.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            msg = ctx.message.content
                            args = msg.split(' ')
                            if args[1] != ctx.message.mentions[0]:
                                await ctx.send(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                            else:
                                reason = msg.replace(args[0]+" "+args[1]+" ", "")
                                await ctx.message.guild.kick(ctx.message.mentions[0], reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.name)+")")+" Reason:"+str(reason))
                                await ctx.send(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason:"+str(reason))
                            try:
                                if args[2] != "":
                                    await ctx.message.guild.kick(ctx.message.mentions[0], reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.name)+")"))
                                    await ctx.send(":white_check_mark: Kicked **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            except IndexError:
                                await ctx.send(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                        except IndexError:
                            await ctx.send(":x: Usage: `{}kick <user> [reason]`".format(self.bot.command_prefix[0]))
                        except Exception as e:
                            await ctx.send(":x: I can't kick someone equal to or higher than me.")
                    else:
                        await ctx.send(":x: You can't kick someone equal to or higher than yourself.")
            else:
                await ctx.send(":x: You cannot kick members.")
        else:
            await ctx.send(":x: I cannot kick members.")
            

    @commands.command(pass_context=True)
    async def ban(self, ctx):
        """Ban a user from the server.

        **Usage:** `g_ban <user> [days] [reason]`

        **Permission:** BAN_MEMBERS"""
        if ctx.message.guild.me.guild_permissions.ban_members == True:
            if ctx.message.author.guild_permissions.ban_members == True:
                if len(ctx.message.mentions) == 0:
                    umsg = ctx.message.content
                    args = umsg.split(' ')
                    try:
                        uid = int(args[1])
                        try:
                            member = await self.bot.get_user_info(uid)
                        except discord.NotFound:
                            await ctx.send(":x: That user doesn't exist.")
                        else:
                            reason = umsg.replace(args[0]+" "+args[1], "")
                            if reason == "":
                                await ctx.message.guild.ban(uid, delete_message_days=1, reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.id)+")"))
                                await ctx.send(":white_check_mark: Banned **"+str(member)+"** with reason: Undefined")
                            else:
                                await ctx.message.guild.ban(uid, delete_message_days=1, reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.id)+")")+" Reason:"+str(reason[1:]))
                                await ctx.send(":white_check_mark: Banned **"+str(member)+"** with reason: "+str(reason[1:]))
                    except ValueError:
                        await ctx.send(":x: That is not an ID.")
                    except IndexError:
                        await ctx.send("Usage: `{}ban <@user/id> [reason]`".format(bot.command_prefix))
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
                                await ctx.message.guild.ban(ctx.message.mentions[0], delete_message_days=days, reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.id)+")")+" Reason:"+str(args))
                                await ctx.send(":white_check_mark: Banned **"+str(member)+"** with reason: "+str(reason))
                            except discord.Forbidden:
                                await bot.say("I can't ban someone higher or equal to myself.")
                        else:
                            try:
                                await ctx.message.guild.ban(ctx.message.mentions[0], delete_message_days=days, reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.id)+")")+" Reason:"+str(args))
                                await ctx.send(":white_check_mark: Banned **"+str(member)+"** with reason: Undefined")
                            except discord.Forbidden:
                                await ctx.send(":x: I can't ban someone higher or equal to myself.")
                    else:
                        await ctx.send(":x: You can't ban someone higher or equal to yourself.")
            else:
                await ctx.send(":x: You don't have the permission to do that.")
        else:
            await ctx.send(":x: I don't have the permission to do that.")
            

    @commands.command(pass_context=True)
    async def softban(self, ctx):
        """Ban a user from the server then unban them, essentially clearing their messages.

        **Usage:** `g_softban <user> [reason]`

        **Permission:** BAN_MEMBERS"""
        if ctx.message.guild.me.guild_permissions.ban_members == True:
            if ctx.message.author.guild_permissions.ban_members == True:
                if len(ctx.message.mentions) == 0:
                    await ctx.send(":x: Tell me who to softban.")
                else:
                    if ctx.message.author.top_role.position > ctx.message.mentions[0].top_role.position:
                        try:
                            args = ctx.message.content
                            args = args.replace(self.bot.command_prefix[0]+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[0]+"softban <@!"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"softban <@"+ctx.message.mentions[0].id+">", "")
                            args = args.replace(self.bot.command_prefix[1]+"softban <@!"+ctx.message.mentions[0].id+">", "")
                            if args == "":
                                await ctx.message.guild.ban(ctx.message.mentions[0], delete_message_days=1, reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.id)+")"))
                                await ctx.message.guild.unban(ctx.message.mentions[0])
                                await ctx.send(":white_check_mark: Softbanned **"+str(ctx.message.mentions[0])+"** with reason: Undefined.")
                            else:
                                await ctx.message.guild.ban(ctx.message.mentions[0], delete_message_days=1, reason="Moderator: {}".format(str(ctx.message.author)+" ("+str(ctx.message.author.id)+")")+" Reason:"+str(args))
                                await ctx.message.guild.unban(ctx.message.mentions[0])
                                await ctx.send(":white_check_mark: Softbanned **"+str(ctx.message.mentions[0])+"** with reason:"+str(args))
                        except Exception as e:
                            await ctx.send(":x: I can't softban someone equal to or higher than me.")
                    else:
                        await ctx.send(":x: You can't softban someone equal to or higher than yourself.")
            else:
                await ctx.send(":x: You cannot ban members.")
        else:
            await ctx.send(":x: I cannot ban members.")
            

    @commands.command(pass_context=True, aliases=["purge", "clean"])
    async def prune(self, ctx):
        """Prune x amount of messages.

        **Usage:** `g_prune <number>`

        **Permission:** MANAGE_MESSAGES"""
        args = ctx.message.content
        args = args.split(' ')
        if ctx.message.guild.me.guild_permissions.manage_messages == True:
            if ctx.message.author.guild_permissions.manage_messages == True:
                try:
                    if args[1] != "":
                        try:
                            mgs = [] 
                            number = int(str(args[1]))
                            async for x in ctx.message.channel.history(limit=number):
                                mgs.append(x)
                            await ctx.message.channel.delete_messages(mgs)
                            prunemsg = await ctx.send(":white_check_mark: Deleted **{}** messages!".format(number))
                            await asyncio.sleep(5)
                            await prunemsg.delete()
                        except ValueError:
                            await ctx.send(":x: That's not a valid number.")
                except IndexError:
                    await ctx.send(":x: Specify messages to prune.")
            else:
                await ctx.send(":x: You cannot manage messages.")
        else:
            await ctx.send(":x: I cannot manage messages.")
            

    @commands.command(pass_context=True)
    async def unban(self, ctx):
        """Unban a user by their ID.

        **Usage:** `g_unban <user>`

        **Permission:** BAN_MEMBERS"""
        if ctx.message.guild.me.guild_permissions.ban_members == True:
            if ctx.message.author.guild_permissions.ban_members == True:
                try:
                    umsg = ctx.message.content
                    args = umsg.split(' ')
                    uid = int(args[1])
                    try:
                        member = await self.bot.get_user_info(uid)
                    except discord.NotFound:
                        await ctx.send("I didn't find that user.")
                    else:
                        await self.bot.unban(ctx.message.guild, member)
                        await ctx.send(":white_check_mark: unbanned "+str(member))
                except ValueError:
                    await ctx.send("That is not an ID.")
                except IndexError:
                    await ctx.send("Usage: `{}unban <user id>`".format(self.bot.command_prefix))
            else:
                await ctx.send("You can't manage bans.")
        else:
            await ctx.send("I can't manage bans.")
        
def setup(bot):
    bot.add_cog(Mod(bot))
