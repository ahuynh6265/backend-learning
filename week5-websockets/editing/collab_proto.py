from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI() 
connected_clients = []
html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, inital-scale=1.0">
  <title>Basic Editor</title>
</head>
<body>


<label for = "edit"> Add Text: 
</label>
<textarea id = "edit" placeholder= "Message here"/> 
</textarea>

<button id = "connect">Connect</button>


<script>
  let websocket 
  
  document.getElementById("connect").addEventListener("click", function(){
    websocket = new WebSocket(`ws://localhost:8000/ws`)
    websocket.onopen = function() {
    }
    websocket.onmessage = function(event){
      console.log(event.data)
      const edits = document.getElementById("edit")
      edits.value = event.data
  }
  })
  
  document.getElementById("edit").addEventListener("keyup", function(){
  const editInput = document.getElementById("edit").value
  websocket.send(`${editInput}`)
  })
</script>
</body>


'''

@app.get("/")
def get_edits(): return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  print(f"Client connected, total: {len(connected_clients)}")
  connected_clients.append(websocket)
  while True:
    message = await websocket.receive_text()
    for client in connected_clients:
      if client != websocket:
        await client.send_text(message)
       
        