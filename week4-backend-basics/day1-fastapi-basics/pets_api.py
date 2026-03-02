from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI() 

class Pets(BaseModel):
  id: int = Field(gt=0, description="Must be a positive value")
  name: str = Field(min_length=1, max_length=50, description="Name is required")
  species: str = Field(min_length=1, max_length=30, description="Species is required")
  age: int = Field(ge=0, le=30, description="Must be a postive value")

pets = [
  Pets(id=1, name="Wally",species="dog", age=2),
  Pets(id=2, name="Appa",species="bison", age=12),
  Pets(id=3, name="Jerry",species="cat", age=17),
]

@app.get("/pets")
def get_pets():
  return pets

@app.get("/pets/{pet_id}")
def get_pet(pet_id: int):
  for pet in pets:
    if pet.id == pet_id:
      return pet
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")

@app.post("/pets", status_code=status.HTTP_201_CREATED)
def create_pet(new_pet: Pets):
  for pet in pets:
    if new_pet.id == pet.id:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{new_pet.id} has already been assigned")
    
  pets.append(new_pet)
  return {"message": "Pet has been added", "pet": new_pet}

@app.put("/pets/{pet_id}")
def update_pet(pet_id: int, new_pet: Pets):
  if pet_id != new_pet.id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"URL ID is {pet_id} but body ID is {new_pet.id}")

  for i, pet in enumerate(pets): 
    if pet.id == pet_id:
      pets[i] = new_pet 
      return {"message": "Pet updated", "pet": new_pet}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")

@app.delete("/pets/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pet(pet_id: int):
  for i, pet in enumerate(pets):
    if pet.id == pet_id:
      pets.pop(i)
      return 
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")

