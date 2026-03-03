from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///books.db")

SessionLocal = sessionmaker(
  autocommit=False, 
  autoflush=False, 
  bind=engine
)

class Base(DeclarativeBase):
  pass