from discord.ext import commands
import discord
import traceback
from cogs.utils import checks
from cogs.utils.tools import generate_id, resolve_emoji

class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.__sendable_exceptions = (
            checks.ChannelNotNSFW,
            commands.BadArgument,
            commands.UserInputError,
        )

    async def on_command(self, ctx):
        self.bot.executed_commands += 1

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(resolve_emoji('ERROR', ctx) + f' You seem to be missing the `{", ".join(error.missing_perms)}` permission(s).')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(resolve_emoji('ERROR', ctx) + f" I need the permission(s) `{', '.join(error.missing_perms)}` to run this command.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(resolve_emoji('ERROR', ctx) + " You are not authorized to use this command.")
        elif isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            await ctx.send(resolve_emoji('ERROR', ctx)
                + f' You can use this command again in {"%d hours, %02d minutes and %02d seconds" % (h, m, s)}'
                + (" (about now)." if error.retry_after == 0 else "."))
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(resolve_emoji('ERROR', ctx) + f" Missing required argument `{error.param.name}`, check `{ctx.prefix}help {ctx.command}`")
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, self.__sendable_exceptions):
            await ctx.send(resolve_emoji('ERROR', ctx) + ' ' + str(error))
            ctx.command.reset_cooldown(ctx)
        else:
            errid = generate_id()
            await ctx.send(resolve_emoji('ERROR', ctx)
                           + f" Unhandled exception. Report this on my support guild (<https://discord.gg/ewvvKHM>) with the ID **{errid}**")
            err_msg = f"Unhandled exception on command `{ctx.command}`\n**Error ID:** {errid}\n**Content:** {ctx.message.clean_content}\n**Author:** {ctx.author} ({ctx.author.id})\n**Guild:** {ctx.guild} ({ctx.guild.id})\n"
            trace = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
            print(err_msg + f"**Traceback:** ```py\n{trace}\n```")
            try:
                self.bot.webhook.send(err_msg + f"**Traceback:** ```py\n{trace}\n```")
            except discord.HTTPException:
                self.bot.webhook.send(err_msg + '**Traceback:** ' + await self.bot.post_to_haste(trace))

def setup(bot):
    bot.add_cog(CommandHandler(bot))