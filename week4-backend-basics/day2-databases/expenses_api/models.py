from sqlalchemy import Column, Integer, Float, String, DateTime
from database import Base
from datetime import datetime, timezone 

class Expense(Base):
  __tablename__ = "expenses"
  id = Column(Integer, primary_key=True, autoincrement=True)
  description = Column(String, nullable=False)
  amount =  Column(Float, nullable=False)
  category = Column(String, nullable=False) 
  created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

  


