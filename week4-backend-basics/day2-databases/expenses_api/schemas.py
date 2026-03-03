from pydantic import BaseModel, ConfigDict

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
  