import discord
from discord.ext import commands
import config

class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="annonce")
    @commands.has_permissions(administrator=True)
    async def annonce(self, ctx, *, message: str):
        channel = self.bot.get_channel(config.ANNOUNCE_CHANNEL_ID)

        if channel is None:
            await ctx.send("❌ Salon d'annonces introuvable.")
            return

        embed = discord.Embed(
            title="📢 Annonce Officielle",
            description=message,
            color=discord.Color.blue()
        )
        embed.set_footer(text="BOT FarmOtor's RP")

        await channel.send(embed=embed)
        await ctx.send("✅ Annonce envoyée avec succès.")

async def setup(bot):
    await bot.add_cog(Announcements(bot))

