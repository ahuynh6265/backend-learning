class LibraryBook: 
  def __init__(self, book_title, author, ISBN):
    self.book_title = book_title
    self.author = author
    self.ISBN = ISBN 
    self.checkout = False
    self.borrower = None 

  def check_out(self, borrower):
    if self.borrower == None: 
      self.borrower = borrower
      self.checkout = True
    else:
      raise ValueError(f"Book has already been checked out. Currently being borrowed by {self.borrower}")
  
  def return_book(self, ISBN):
    if ISBN != self.ISBN:
      raise ValueError("This book does not exist.")

    if ISBN == self.ISBN and self.checkout == True:
      returner = self.borrower
      self.checkout = False
      self.borrower = None
      print(f"{returner} has returned {self.book_title}.")
    else: 
      raise ValueError("This book has not been checked out.")
  
  def check_availability(self):
    if self.checkout == True:
      return f"{self.book_title} is currently checked out by {self.borrower}"
    else: return f"{self.book_title} is currently available."
    
  def __str__(self):
    return f"Book Title: {self.book_title}\nAuthor: {self.author}\nISBN: {self.ISBN}"
  
  @classmethod
  def get(cls):
    book_title = input("Book Title: ").title().strip() 
    author = input("Author: ").title().strip()
    ISBN = int(input("IBSN number: "))
    return cls(book_title, author, ISBN)

def print_error(e):
  print(f"Error: {e}\n")


def main():
  library = LibraryBook.get()

  while True:
    try: 
      choice = int(input("Library Book Menu: \n1. Check Out\n2. Return\n3. Check Availability\n4. Show Book Info\n5. Quit\n"))
      if choice < 1 or choice > 5:
        raise ValueError("Please select between 1 and 5")
    except ValueError as e:
      print_error(e)
      continue 

    if choice == 1:
      try: 
        borrower = input("Name of borrower: ").title()
        library.check_out(borrower)
      except ValueError as e:
        print_error(e)

    elif choice == 2:
      try: 
        ISBN = int(input("ISBN Number of book: "))
        library.return_book(ISBN)
      except ValueError as e:
        print_error(e)

    elif choice == 3: 
      result = library.check_availability() 
      print(result)
    
    elif choice == 4:
      print(library)

    elif choice == 5: break 
    
    
if __name__ == "__main__":
  main() 