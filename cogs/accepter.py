import discord
from discord.ext import commands

ROLE_ID = 1459644755246977207  # Rôle Citoyen RP

class Accepter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="accepter")
    async def accepter(self, ctx):
        role = ctx.guild.get_role(ROLE_ID)

        if role is None:
            await ctx.send("❌ Erreur : rôle introuvable. Contacte le staff.")
            return

        if role in ctx.author.roles:
            await ctx.send("✅ Tu as déjà accepté le règlement.")
            return

        await ctx.author.add_roles(role, reason="Règlement accepté")
        await ctx.send(
            f"🎉 {ctx.author.mention}, tu as **accepté le règlement** !\n"
            "Bon RP sur **FarmOtor's RP** 🚓🚑"
        )

        # Optionnel : supprimer le message de commande
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Accepter(bot))
