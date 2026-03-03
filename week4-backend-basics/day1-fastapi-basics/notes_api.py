from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, computed_field
from typing import Optional 
from datetime import datetime

app = FastAPI() 

class CreateNote(BaseModel):
  id: int = Field(gt=0)
  title: str = Field(min_length=1, max_length=100)
  content: str = Field(min_length=1, max_length=1000)

class Note(BaseModel):
  id: int = Field(gt=0)
  title: str = Field(min_length=1, max_length=100)
  content: str = Field(min_length=1, max_length=1000)
  created_at: datetime 
  updated_at: datetime 

  @computed_field
  @property
  def display_created(self) -> str:
    return self.created_at.strftime("%B %d, %Y %I:%M %p:")
  
  @computed_field
  @property
  def display_updated(self) -> str:
    return self.updated_at.strftime("%B %d, %Y %I:%M %p:")

startup_time = datetime.now()
  
notes = [
  Note(id=1, title="Grocery List",content="Get banana, apples, water, paper towels", created_at=startup_time, updated_at=startup_time),
  Note(id=2, title="Study Notes",content="Math, reading, writing, homework", created_at=startup_time, updated_at=startup_time),
  Note(id=3, title="Spotify Artists",content="Bad bunny, horsegirl, jaydayoungan, nba youngboy", created_at=startup_time, updated_at=startup_time),
  Note(id=4, title="NBA players",content="Lebron, KD, Jabari Smith, Anthony Edwards", created_at=startup_time, updated_at=startup_time),
]
  
@app.get("/notes")
def get_notes(): return notes 

@app.get("/notes/{note_id}")
def get_note(note_id: int):
  for note in notes:
    if note_id == note.id: return note
  raise HTTPException(status_code=status.
  HTTP_404_NOT_FOUND, detail="Note ID not found")

@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note_data: CreateNote): 
  for note in notes:
    if note.id == note_data.id:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Note ID {note_data.id} has already been assigned.")
    
  now = datetime.now() 
  new_note = Note(
    id = note_data.id, 
    title = note_data.title,
    content = note_data.content, 
    created_at = now, 
    updated_at = now
  )
  notes.append(new_note)
  return{"message": "Note created", "note": new_note}

@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
  for i, note in enumerate(notes):
    if note.id == note_id: 
      notes.pop(i)
      return
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note ID not found")

@app.put("/notes/{note_id}")
def update_note(note_id: int, note_data: CreateNote):
  if note_id != note_data.id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"URL ID {note_id} does not match body ID {note_data.id}")
  
  for i, note in enumerate(notes):
    if note.id == note_data.id:
      now = datetime.now() 
      new_note = Note(
        id = note_data.id, 
        title = note_data.title,
        content = note_data.content, 
        created_at = note.created_at, 
        updated_at = now
      )
      notes[i] = new_note 
      return {"message": "Note updated", "note": new_note}
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note ID not found")


  
  

 