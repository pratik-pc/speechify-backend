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

voice_channel_list = {}

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

      # Retrieve userid from the message
      user_id = json_message['user_id']

      # Get the voice channel to which audio streaming is to be done
      channel_id = voice_channel_list[user_id]
      voice.save_to_file(json_message['message'])
      voice_channel = bot.get_channel(channel_id)

      # Get the voice client object
      voice_client = discord.utils.get(bot.voice_clients, channel=voice_channel)
      voice_client.play(discord.FFmpegPCMAudio('src\discord\output.wav'))
  
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel

    # Store user details to list of active voice clients
    channel = await channel.connect()
    user_id = ctx.author.id
    channel_id = channel.channel.id
    voice_channel_list[user_id] = channel_id


@bot.command()
async def leave(ctx):
  await ctx.voice_client.disconnect()

  # Remove user details from list of active voice clients
  del voice_channel_list[ctx.author.id]


bot.run(token)