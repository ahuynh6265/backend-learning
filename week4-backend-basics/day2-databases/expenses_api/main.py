from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session 
from database import engine, SessionLocal, Base
from models import Expense 
from schemas import ExpenseCreate, ExpenseResponse

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal() 
  try: yield db
  finally: db.close() 

@app.get("/expenses", response_model=list[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
  return db.query(Expense).all() 

@app.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
  expense =  db.query(Expense).filter(Expense.id == expense_id).first() 

  if not expense: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense ID not found")
  
  return expense

@app.post("/expenses", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create_expenses(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
  new_expense = Expense(description = expense_data.description, amount = expense_data.amount, category = expense_data.category)
  db.add(new_expense)
  db.commit()
  db.refresh(new_expense)
  return new_expense

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

