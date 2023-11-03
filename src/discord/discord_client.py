from discord_bot import bot
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('discord_token')



@bot.event
async def on_ready():
  print(bot.get_all_channels)
  guilds = bot.guilds
  for guild in guilds:
    print(guild.name)

bot.run(token)


