from fastapi import FastAPI #import framework

app = FastAPI() #create api app

@app.get("/") #decorator: someone makes a GET request to '/' 
def read_root(): #handles request
  return {"message": "Hello World"} #return JSON automatically 

@app.get("/about")
def about(): 
  return {"app": "My First API", "version": "1.0"}

@app.get("/hello/{name}")
def greet(name: str):
  return {"message": f"Hello {name}"}

@app.get("/search")
def search(q: str, limit: int = 10):
  return {
    "query": q,
    "limit": limit,
    "results": f"Searching for '{q}' with limit {limit}"
  }

