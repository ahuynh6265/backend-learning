import asyncio, websockets, sys 

async def chat():
  name = input("Your name: ")

  async with websockets.connect("ws://localhost:8765") as websocket:
    await websocket.send(name)
    print("Connected! Type messages below")

    #two tasks running at the same time 
    #one listens for incoming, one sends outgoing
    async def recieve():
      async for message in websocket:
        print(f"\n{message}")

    async def send():
      while True:
        msg = await asyncio.get_event_loop().run_in_executor(None, input, "")
        await websocket.send(f"{name}: {msg}")

    await asyncio.gather(recieve(), send())

asyncio.run(chat())
