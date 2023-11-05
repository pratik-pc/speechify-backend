import websockets
import asyncio

async def handle_connection(websocket, path):
  print(f'New connection from {websocket.remote_address}')
  try:
    async for message in websocket:
      print(message)

  except websockets.exceptions.ConnectionClosed:
    print('websocket is closed')




server = websockets.serve(
    handle_connection,
    "127.0.0.1",
    8000,
  )

if __name__ == "__main__":
  asyncio.get_event_loop().run_until_complete(server)
  asyncio.get_event_loop().run_forever()