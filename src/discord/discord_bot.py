import discord
from discord.ext import commands
import websockets
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
  url = "ws://127.0.0.1:8000"

  async with websockets.connect(url) as websocket:
    print(f'Connected to {url}')
    while True:
      message = await websocket.recv()
      print(message)
  
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


bot.run(token)