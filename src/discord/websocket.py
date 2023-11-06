import websockets
import asyncio


connected_clients = set()

async def handle_connection(websocket, path):
  print(f'New connection from {websocket.remote_address}')
  connected_clients.add(websocket)
  try:
    async for message in websocket:
      await websocket.send(message)
      for client in connected_clients:
        if client != websocket:
          await client.send(message)

  except websockets.exceptions.ConnectionClosed:
    print('websocket is closed')

  finally:
    connected_clients.remove(websocket)



server = websockets.serve(
    handle_connection,
    "127.0.0.1",
    8000,
  )

if __name__ == "__main__":
  asyncio.get_event_loop().run_until_complete(server)
  asyncio.get_event_loop().run_forever()