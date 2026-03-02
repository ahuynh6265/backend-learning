from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI() 

class ToDo(BaseModel):
  id: int = Field(gt=0, description="Must be a postive value")
  task: str = Field(min_length=1, max_length=200, description="Task is required.")
  completed: bool = Field(default=False)

todo_list = [
  ToDo(id=1, task="Read book",completed=True),
  ToDo(id=2, task="Drink water", completed=True),
  ToDo(id=3, task="Sleep")
]

@app.get("/todos")
def get_todo_list(): return todo_list 

@app.get("/todos/{todo_id}")
def get_task(todo_id: int):
  for task in todo_list:
    if task.id == todo_id:
      return task 
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_task(task: ToDo):
  for existing_task in todo_list:
    if existing_task.id == task.id:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Task with ID {task.id} already exists")
  todo_list.append(task)
  return {"message": "Task created", "task": task}

@app.put("/todos/{todo_id}")
def update_task(todo_id: int, task_updated: ToDo):
  if todo_id != task_updated.id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"ID mismatch: URL has {todo_id}, but body has {task_updated.id}")
  
  for i, task in enumerate(todo_list):
    if task.id == todo_id:
      todo_list[i] = task_updated
      return {"message": "Task Updated", "task": task_updated}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(todo_id: int):
  for i, task in enumerate(todo_list):
    if task.id == todo_id:
      todo_list.pop(i)
      return 
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")




