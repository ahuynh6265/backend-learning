from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel, Field 
from typing import Optional 

app = FastAPI() 

#data model - what the book looks like 
class Book(BaseModel): 
  id: int = Field(gt=0, description="Must be a positive number")
  title: str = Field(min_length=1, max_length=200, description="Title is required.")
  author: str = Field(min_length=1, max_length=100, description="Author name is required.")
  year: int = Field(ge=1000, le=2026, description="Year must be between 1000 and 2026" )

#memory database 
books = [
    Book(id=1, title="1984", author="George Orwell", year=1949),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)
    ]

#GET all books
@app.get("/books")
def get_books(): return books

#SEARCH/FILTER 
@app.get("/books/search")
def search_books(
  author: Optional[str] = None,
  year: Optional[int] = None,
  min_year: Optional[int] = None, 
  max_year: Optional[int] = None, 
):
  '''
  search books by:
  author (partial match): case insensitive 
  year: exact match 
  min_year: published on or after this year
  max_year: publised on or before this year 
  '''
  results = books

  if author: 
    results = [b for b in results if author.lower() in b.author.lower()]
  
  if year:
    results = [b for b in results if b.year == year]
  
  if min_year:
    results = [b for b in results if min_year <= b.year]
  
  if max_year:
    results = [b for b in results if b.year <= max_year]
  
  return{ 
    "count": len(results),
    "books": results
  }


#GET by specific id
@app.get("/books/{book_id}")
def get_book(book_id: int):
  for book in books:
    if book.id == book_id:
      return book 
  raise HTTPException(status_code=404, detail="Book not found")
  
#POST - create new book
@app.post("/books")
def create_book(book: Book):
  books.append(book)
  return {"message": "Book created", "book": book}

#DELETE - delete existing book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
  for i, book in enumerate(books):
    if book.id == book_id:
      books.pop(i)
      return {"message": "Book deleted"}
  raise HTTPException(status_code=404, detail="Book not found")

#UPDATE - update existing book
@app.put("/books/{book_id}")
def update_book(book_id: int, book_updated: Book):
  for i, book in enumerate(books):
    if book.id == book_id: 
      books[i] = book_updated 
      return {"message": "Book updated", "book": book_updated}
  raise HTTPException(status_code=404, detail="Book not found")



