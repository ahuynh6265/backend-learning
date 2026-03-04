from pydantic import BaseModel, ConfigDict, computed_field 
from datetime import datetime

class UserCreate(BaseModel):
  name: str
  email: str 

class ExpenseCreate(BaseModel):
  description: str 
  amount: float 
  category: str

class ExpenseResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int 
  description: str 
  amount: float 
  category: str 
  created_time: datetime
  updated_time: datetime
  user_id: int 

  @computed_field
  @property
  def created_display(self) -> str:
    return self.created_time.strftime("%B %d, %Y %I:%M %p")
  
  @computed_field
  @property
  def updated_display(self) -> str:
    return self.updated_time.strftime("%B %d, %Y %I:%M %p")
  
class UserResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  name: str
  email: str 
  created_time: datetime
  updated_time: datetime
  expense: list[ExpenseResponse]

  @computed_field
  @property
  def created_display(self) -> str:
    return self.created_time.strftime("%B %d, %Y %I:%M %p")
  
  @computed_field
  @property
  def updated_display(self) -> str:
    return self.updated_time.strftime("%B %d, %Y %I:%M %p")
