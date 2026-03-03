from pydantic import BaseModel, ConfigDict, computed_field
from datetime import datetime

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
  created_at: datetime 
  updated_at: datetime 

  @computed_field
  @property
  def created_display(self) -> str:
    return self.created_at.strftime("%B %d, %Y %I:%M %p")
  
  @computed_field
  @property
  def updated_display(self) -> str:
    return self.updated_at.strftime("%B %d, %Y %I:%M %p")
  
