from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()
connected_clients = {}
message_history = {}

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, inital-scale=1.0">
  <title>Real Time Chat</title>
</head>

<body>

<form>
  <label for = "username"> Username: 
  </label>
  <input type = "text" id = "username" placeholder= "Username here"/> 
</form>

<form>
  <label for = "room"> Room:
  </label>
  <input type = "number" id = "room" placeholder = "Enter room number"/> 
</form> 

<form>
  <label for = "message"> Message: 
  </label>
  <input type = "text" id = "message" placeholder= "Message here"/> 
</form>

<button id = "send">Send</button>
<div id = "messages"></div>
<button id = "connect">Connect</button>

<script>
  let websocket 

  document.getElementById("connect").addEventListener("click", function(){
    const username = document.getElementById("username").value 
    const room = document.getElementById("room").value
    websocket = new WebSocket(`ws://localhost:8000/ws/${room}/${username}`)
    websocket.onopen = function() {
      websocket.send(username)
    }
    websocket.onmessage = function(event){
      console.log(event.data)
      const messages = document.getElementById("messages")
      messages.innerHTML += `<p>${event.data}</p>` 
    }

    websocket.onclose = function() {
      const messages = document.getElementById("messages")
      messages.innerHTML += `<p>Disconnected</p>` 
    }
  })

  document.getElementById("send").addEventListener("click", function(){
    const messageInput = document.getElementById("message").value
    const messageDiv = document.getElementById("messages")
    const username = document.getElementById("username").value
    messageDiv.innerHTML += `<p>You: ${messageInput}</p>`
    websocket.send(`${username}: ${messageInput}`)
    document.getElementById("messages").value = ""
  })
</script>

</body>

</html>
'''

class ConnectionManager:
  async def connect(self, websocket:WebSocket, room, username):
    await websocket.accept()
    connected_clients.setdefault(room, {})
    message_history.setdefault(room, [])
    connected_clients[room][websocket] = username
    if message_history[room]:
      await websocket.send_text("<br>".join(message_history[room]))
  
  async def disconnect(self, websocket:WebSocket, room): 
    del connected_clients[room][websocket]
    await websocket.close() 

  async def broadcast(self, websocket:WebSocket, room, message):
    for client in connected_clients[room].keys(): 
      if client != websocket:
        await client.send_text(message)

    

manager = ConnectionManager()

@app.get("/")
def get_chat(): return HTMLResponse(html)

@app.websocket("/ws/{room}/{username}")
async def websocket_endpoint(websocket: WebSocket, room: int, username: str):
  await manager.connect(websocket, room, username)
  await manager.broadcast(websocket, room, f"{username} has joined chat room {room}")

  try:
    while True:
      message = await websocket.receive_text() 
      await manager.broadcast(websocket, room, message)
      message_history[room].append(message)
  except WebSocketDisconnect:
    pass
  finally:
    await manager.broadcast(websocket, room, f"{username} has disconnected from room {room}")
    await manager.disconnect(websocket, room)