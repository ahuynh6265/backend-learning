#asyncio is a single thread that can handle and switch between tasks while waiting for other tasks to update
import asyncio, websockets

#all currently connected clients
connected_clients = {}

async def handle_connection(websocket): 
  #add this client to the set when they connect 
  username = await websocket.recv() 
  connected_clients[websocket] = username
  print(f"{username} connected. Total clients: {len(connected_clients)}")

  #broadcast to everyone but the sender that they have entered
  for client in connected_clients.keys():
    if client != websocket:
      await client.send(f"{username} has connected to the chat.")
  
  try:
    #keep listening for messages from this client 
    #pauses here waiting for a message
    async for message in websocket: 
      print(f"Recieved: {message}")

      #broadcast to everyone except the sender
      for client in connected_clients.keys(): 
        if client != websocket:
          #pauses here waiting for send to finish 
          await client.send(message)
  
  except websockets.exceptions.ConnectionClosed:
    pass #client disconnected 
  
  finally: 
    #broadcast to everyone but the sender that they have disconnected
    for client in connected_clients.keys():
      if client != websocket:
        await client.send(f"{username} has disconected from the chat.")

    #ALWAYS remove them from the set when they leave
    connected_clients.pop(websocket)
    print(f"{username} has disconnected. Total: {len(connected_clients)}")

async def main():
  #8765 default websocket port
  async with websockets.serve(handle_connection, "localhost", 8765):
    print("Websocket server running on ws://localhost:8765")
    #run forever
    await asyncio.Future() 

asyncio.run(main())