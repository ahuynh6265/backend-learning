from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session 
from database import engine, SessionLocal, Base
from models import User, Expense 
from schemas import UserCreate, UserResponse, ExpenseCreate, ExpenseResponse
from typing import Optional 

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal() 
  try: yield db
  finally: db.close() 

#user routes
@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), limit: int = 10, offeset: int = 0):
  return db.query(User).limit(limit).offset(offeset).all()

@app.get("/users/search", response_model=list[UserResponse])
def search_user(
  name: Optional[str] = None,
  db: Session = Depends(get_db)
):
  query = db.query(User)
  if name:
    query = query.filter(User.name.ilike(f"%{name}%"))
  return query.all() 

  
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first()
  if not user: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found.")
  return user 

@app.post("/users", response_model=list[UserResponse], status_code=status.HTTP_201_CREATED)
def create_users(users_data: list[UserCreate], db: Session = Depends(get_db)): 
  new_users = [User(name = u.name, email = u.email)for u in users_data]
  db.add_all(new_users)
  db.commit() 
  for user in new_users:
    db.refresh(user)
  return new_users

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_users(user_id: int, db: Session = Depends(get_db)): 
  user = db.query(User).filter(User.id == user_id).first() 

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found")
  
  db.delete(user)
  db.commit() 
  return 

#expense routes 
@app.get("/users/{user_id}/expenses", response_model=list[ExpenseResponse])
def get_user_expenses(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first() 

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found") 
  
  return user.expense 

@app.get("/users/{user_id}/expenses/search", response_model=list[ExpenseResponse])
def search_user(
  user_id: int, 
  min_amount: Optional[int] = None,
  max_amount: Optional[int] = None, 
  category: Optional[str] = None, 
  db: Session = Depends(get_db)
):
  user = db.query(User).filter(User.id == user_id).first() 

  if not user: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found") 

  query = db.query(Expense).filter(Expense.user_id == user_id)
  if min_amount:
    query = query.filter(Expense.amount >= min_amount)

  if max_amount:
    query = query.filter(Expense.amount <= max_amount)

  if category:
    query = query.filter(Expense.category.ilike(f"%{category}%"))
  return query.all() 

@app.post("/users/{user_id}/expenses", response_model=list[ExpenseResponse], status_code=status.HTTP_201_CREATED)
def create_user_expenses(user_id: int, expenses_data: list[ExpenseCreate], db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first() 

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found")
  
  new_expenses = [Expense(user_id=user_id, description = e.description, amount = e.amount, category = e.category) for e in expenses_data]
  db.add_all(new_expenses)
  db.commit() 
  for expense in new_expenses:
    db.refresh(expense)
  return new_expenses

@app.delete("/users/{user_id}/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_expense(user_id: int, expense_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first() 
  expense = db.query(Expense).filter(Expense.id == expense_id).first() 

  if not user: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found")
  
  elif not expense:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense ID not found")
  
  if expense.user_id != user_id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Expense ID {expense.id} does not belong to {user.name}.") 
  
  db.delete(expense)
  db.commit()
  return

@app.put("/users/{user_id}/expenses/{expense_id}", response_model=ExpenseResponse)
def update_user_expense(user_id: int, expense_id: int, expense_data: ExpenseCreate, db: Session = Depends(get_db)): 
  user = db.query(User).filter(User.id == user_id).first()
  expense = db.query(Expense).filter(Expense.id == expense_id).first() 

  if not user: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID not found")
  
  elif not expense:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense ID not found")
  
  if expense.user_id != user_id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Expense ID {expense.id} does not belong to {user.name}.") 
  
  expense.description = expense_data.description
  expense.amount = expense_data.amount
  expense.category = expense_data.category
  db.commit()
  db.refresh(expense)
  return expense 


