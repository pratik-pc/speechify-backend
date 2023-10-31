import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('discord_token')

@bot.event
async def on_ready(): 
  print(f'Logged in as {bot.user.name}')

if __name__ == '__main__':
    bot.run(token)