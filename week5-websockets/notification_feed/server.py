import asyncio, websockets, random 

notifications =[
  "Stock prices have gone down",
  "Stock prices have gone up", 
  "Weather will be rainy today",
  "Weather will be rainy tomorrow",
  "Weather will be sunny today",
  "Lebron has been traded to the Heat",
  "Lebron has retired",
  "Lebron is the greatest player of all time"
]

connected_clients = {}

async def handle_connection(websocket):
  username = await websocket.recv()
  try:
    connected_clients[websocket] = username
    print(f"{username} has subscribed to the feed. Total clients: {len(connected_clients)}")

    #used to keep the server alive while broadcast is happening
    async for _ in websocket:
      pass
  
  except websockets.exceptions.ConnectionClosed:
    pass

  finally:
    connected_clients.pop(websocket)
    print(f"{username} has unsubscribed. Total: {len(connected_clients)}")

async def broadcast_loop():
  while True: 
    for client in connected_clients.keys():
      notification = random.choice(notifications) 
      await client.send(f"Notification: {notification}")
    await asyncio.sleep(5)

async def main():
  async with websockets.serve(handle_connection, "localhost", 8765):
    print("Websocket server running on ws://localhost:8765")
    await asyncio.gather(asyncio.Future(), broadcast_loop())
    
  
asyncio.run(main())