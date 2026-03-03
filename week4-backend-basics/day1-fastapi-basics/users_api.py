from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional 

app = FastAPI() 

class Users(BaseModel): 
  id: int = Field(gt=0, description="Must be a positive value")
  name: str = Field(min_length=1, max_length=100, description="Name is required")
  email: str = Field(min_length=5, max_length=100, description="Email is required")
  age: int = Field(ge=13, le=120)

users = [
   Users(id=1, name="Jon Jones",email="jjones@email.com", age=37),
   Users(id=2, name="Dak Prescott",email="dprescott@email.com", age=26),
   Users(id=3, name="LeBron James",email="lbj@email.com", age=41),
   Users(id=4, name="Tom Brady",email="tb12@email.com", age=47),
   Users(id=5, name="Jeremy Lin",email="jlin7@email.com", age=32),
]

@app.get("/users")
def get_users(): return users 

@app.get("/users/search")
def search_users(
  name: Optional[str] = None,
  min_age: Optional[int] = None, 
  max_age: Optional[int] = None
): 
  
  results = users 

  if name: 
    results = [n for n in results if name.lower() in n.name.lower()]
  
  if min_age:
    results = [n for n in results if min_age <= n.age]
  
  if max_age:
    results = [n for n in results if n.age <= max_age]
  
  return{
    "count": len(results),
    "users": results
  
  }


@app.get("/users/{user_id}")
def get_user(user_id: int):
  for user in users: 
    if user_id == user.id: return user 
  raise HTTPException(status_code=status.
  HTTP_404_NOT_FOUND, detail="User ID not found")

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(new_user: Users):
  for user in users: 
    if new_user.id == user.id:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User ID {new_user.id} already assigned.")
  users.append(new_user)
  return {"message": "User created", "user": new_user}

@app.put("/users/{user_id}")
def update_user(user_id: int, new_user: Users):
  if user_id != new_user.id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"URL ID {user_id} and body ID {new_user.id} do not match.")
  
  for i, user in enumerate(users):
    if user_id == user.id:
      users[i] = new_user 
      return {"message": "User updated", "user": new_user}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found")

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
  for i, user in enumerate(users):
    if user_id == user.id:
      users.pop(i) 
      return 
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found")



