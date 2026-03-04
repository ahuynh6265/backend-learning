from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timezone

class User(Base): 
  __tablename__ = "user"
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  created_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  updated_time = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)) 
  expense = relationship("Expense", back_populates="user", cascade="all, delete")

class Expense(Base):
  __tablename__ = "expense"
  id = Column(Integer, primary_key=True, autoincrement=True)
  description = Column(String, nullable=False)
  amount = Column(Float, nullable=False)
  category = Column(String, nullable=False)
  user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
  created_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  updated_time = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)) 
  user = relationship("User", back_populates="expense")

