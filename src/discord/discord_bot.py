import discord
from discord.ext import commands
import websockets
import os
import json
from dotenv import load_dotenv
from src.voice_service.voice_service import Voice

load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('discord_token')

voice = Voice()

@bot.event
async def on_ready(): 
  print(f'Logged in as {bot.user.name}')
  url = "ws://127.0.0.1:8000"

  async with websockets.connect(url) as websocket:
    print(f'Connected to {url}')
    while True:
      message = await websocket.recv()
      print(message)
      json_message = json.loads(message)
      voice.save_to_file(json_message['message'])
      voice_clients = bot.voice_clients
      voice_client = voice_clients[0]
      voice_client.play(discord.FFmpegPCMAudio('output.wav'))
  
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


bot.run(token)