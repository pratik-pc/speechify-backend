import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
from src.voice_service.voice_service import Voice
from aiokafka import AIOKafkaConsumer

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
  consumer = AIOKafkaConsumer(
    'pc',
    bootstrap_servers='localhost:9092',
    group_id='p',
    auto_offset_reset='none'
  )
  await consumer.start()

  try:
    async for message in consumer:
      json_message = json.loads(message.value.decode("utf-8"))
      # Get the voice channel to which audio streaming is to be done
      channel_id = voice_channel_list[json_message['user_id']]
      voice.save_to_file(json_message['message'])
      voice_channel = bot.get_channel(channel_id)

      # Get the voice client object
      voice_client = discord.utils.get(bot.voice_clients, channel=voice_channel)
      voice_client.play(discord.FFmpegPCMAudio('src\discord\output.wav'))
      
  finally:
    await consumer.stop()
  
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