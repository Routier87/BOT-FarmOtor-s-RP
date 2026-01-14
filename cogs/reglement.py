import discord
from discord import app_commands
from discord.ext import commands

class Reglement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="reglement",
        description="Afficher le règlement officiel du serveur FarmOtor's RP"
    )
    async def reglement(self, interaction: discord.Interaction):

        embeds = []

        embeds.append(discord.Embed(
            title="📜 Règlement Joueurs – FarmOtor's RP",
            description=(
                "Le règlement est **obligatoire**.\n"
                "Sanctions possibles : avertissement → ban définitif.\n"
                "⚠️ Modifiable à tout moment."
            ),
            color=discord.Color.orange()
        ))

        embeds.append(discord.Embed(
            title="📘 HRP & Discord",
            description=(
                "**Discord :**\n"
                "• Respect obligatoire\n"
                "• Pas de spam / flood\n"
                "• Publicité interdite\n\n"
                "**HRP :** règlement à connaître"
            ),
            color=discord.Color.blue()
        ))

        embeds.append(discord.Embed(
            title="📚 Lexique RP",
            description=(
                "Zone Safe, NoFear, NoPain, PowerGaming,\n"
                "MetaGaming, RevengeKill, Freekill, ForceRP..."
            ),
            color=discord.Color.green()
        ))

        embeds.append(discord.Embed(
            title="🎭 Rôleplay",
            description=(
                "• Respect total\n"
                "• Propos discriminatoires interdits\n"
                "• /me obligatoire en coma"
            ),
            color=discord.Color.purple()
        ))

        embeds.append(discord.Embed(
            title="🚨 Illégal & Mort RP",
            description=(
                "• Sommations obligatoires\n"
                "• Braquages réglementés\n"
                "• Mort RP sous dossier staff"
            ),
            color=discord.Color.red()
        ))

        for e in embeds:
            e.set_footer(text="BOT FarmOtor's RP | GTA RP USA")

        await interaction.response.send_message(embeds=embeds, ephemeral=False)

async def setup(bot):
    await bot.add_cog(Reglement(bot))
