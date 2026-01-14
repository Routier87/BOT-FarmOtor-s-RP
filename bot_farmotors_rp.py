import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=config.PREFIX,
    intents=intents
)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} est connecté !")
    await bot.change_presence(
        activity=discord.Game(name="GTA RP | FarmOtor's RP")
    )

# Chargement des modules (cogs)
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.announcements")

bot.run(config.TOKEN)
