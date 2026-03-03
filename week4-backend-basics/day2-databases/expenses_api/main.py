from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session 
from database import engine, SessionLocal, Base
from models import Expense 
from schemas import ExpenseCreate, ExpenseResponse
from typing import Optional

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal() 
  try: yield db
  finally: db.close() 

@app.get("/expenses", response_model=list[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db), limit: int = 10, offset: int = 0):
  return db.query(Expense).offset(offset).limit(limit).all()

@app.get("/expenses/search", response_model=list[ExpenseResponse])
def search_expenses( 
  min_amount: Optional[float] = None,
  max_amount: Optional[float] = None, 
  category: Optional[str] = None,
  db: Session = Depends(get_db)):
  query = db.query(Expense)

  if min_amount:
    query = query.filter(Expense.amount >= min_amount)

  if max_amount:
    query = query.filter(Expense.amount <= max_amount)

  if category:
    query = query.filter(Expense.category.ilike(f"%{category}%"))
  
  return query.all() 

  

@app.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
  expense =  db.query(Expense).filter(Expense.id == expense_id).first() 

  if not expense: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense ID not found")
  
  return expense

@app.post("/expenses", response_model=list[ExpenseResponse], status_code=status.HTTP_201_CREATED)
def create_expenses(expenses_data: list[ExpenseCreate], db: Session = Depends(get_db)):
  new_expenses = [Expense(description = e.description, amount = e.amount, category = e.category) for e in expenses_data]
  db.add_all(new_expenses)
  db.commit()
  for expense in new_expenses:
    db.refresh(expense)
  return new_expenses

@app.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expenses(expense_id: int, db: Session = Depends(get_db)):
  expense = db.query(Expense).filter(Expense.id == expense_id).first() 

  if not expense: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense ID not found")
  
  db.delete(expense)
  db.commit() 
  return
  
@app.put("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense_data: ExpenseCreate, db: Session = Depends(get_db)):
  expense = db.query(Expense).filter(Expense.id == expense_id).first() 

  if not expense: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense ID not found")
  
  expense.description = expense_data.description
  expense.amount = expense_data.amount
  expense.category = expense_data.category

  db.commit()
  db.refresh(expense)
  return expense

