import asyncio, websockets

async def notification():
  name = input("Your name: ")

  async with websockets.connect("ws://localhost:8765") as websocket:
    await websocket.send(name)
    print(f"{name}, you have subscribed to the notification feed.")

    async def recieve():
      
      async for notif in websocket:
        print(f"\n{notif}")
      
    await recieve()

asyncio.run(notification())
