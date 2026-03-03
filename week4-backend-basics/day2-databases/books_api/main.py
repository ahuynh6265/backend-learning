from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Book
from schemas import BookCreate, BookResponse 

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal() #open database connection
  try: yield db #hand the connection to route
  finally: db.close() #always close when route is done 

@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)): 
  return db.query(Book).all() 

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
  book = db.query(Book).filter(Book.id == book_id).first() 
  if not book:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")
  return book 

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate, db: Session = Depends(get_db)): 
  new_book = Book(title = book_data.title, author = book_data.author, year = book_data.year)
  db.add(new_book)
  db.commit()
  db.refresh(new_book)
  return new_book 

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
  book = db.query(Book).filter(Book.id == book_id).first()
  if not book:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")
  db.delete(book)
  db.commit() 
  return 

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookCreate, db: Session = Depends(get_db)):
  book = db.query(Book).filter(Book.id == book_id).first()
  if not book: 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book ID not found")
  
  book.title = book_data.title
  book.author = book_data.author
  book.year = book_data.year

  db.commit()
  db.refresh(book)
  return book 

  





