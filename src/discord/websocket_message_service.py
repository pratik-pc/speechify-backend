import websockets
import asyncio
import json


async def send_message(url):
  async with websockets.connect(url) as websocket:
    await websocket.send(json.dumps({"message": 'message from client'}))
    print('published message')


websocket_url = "ws://127.0.0.1:8000"

asyncio.get_event_loop().run_until_complete(send_message(websocket_url))