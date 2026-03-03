from sqlalchemy import Column, Integer, Float, String 
from database import Base

class Expense(Base):
  __tablename__ = "expenses"
  id = Column(Integer, primary_key=True, autoincrement=True)
  description = Column(String, nullable=False)
  amount =  Column(Float, nullable=False)
  category = Column(String, nullable=False)


