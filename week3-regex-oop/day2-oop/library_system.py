class Book: 
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author 
    self.isbn = isbn
    self.checked_out = False

  def checkout(self):
    if self.checked_out: 
      print(f"{self.title} is already checked out.")
    else:
      self.checked_out = True
      print(f"You have checked out: {self.title}")
      return self.checked_out 
  
  def returned(self):
    if not self.checked_out:
      print(f"{self.title} isn't checked out. Can not be returned.")
    else:
      self.checked_out = False
      print(f"You have returned: {self.title}")
      return self.checked_out
  
  def __str__(self):
    if not self.checked_out:
      return f"{self.title}:\n  Author: {self.author}\n  ISBN: {self.isbn}\n  Status: Available for checkout" 
    else:    
      return f"{self.title}:\n  Author: {self.author}\n  ISBN: {self.isbn}\n  Status: Currently checked out"

class Library:
  def __init__(self, name):
    self.name = name 
    self.books = []
  
  def add_book(self, book): 
    self.books.append(book)
    print(f"{book.title} has been added into {self.name}")
  
  def remove_book(self, book):
    print(f"{book.title} by {book.author} has been removed.")
    self.books.remove(book)
  
  def checkout_book(self, book):
    book.checkout()
  
  def return_book(self, book):
    book.returned() 
  
  def show_available(self):
    if self.books: 
      available = False

      for book in self.books:
        if not book.checked_out: 
          print(f"Title: {book.title}\nISBN: {book.isbn}")
          print("-"*50)
          available = True
      
      if available: return available

      if not available: 
        print("No books available currently.")
        return available
  
  def show_checked_out(self):
    if self.books:
      current_checked = False

      for book in self.books:
        if book.checked_out: 
          print(f"Title: {book.title}\nISBN: {book.isbn}")
          print("-"*50)
          current_checked = True
      
      if current_checked: return current_checked

      elif not current_checked: 
        print("No books checked out currently.")
        return current_checked
    
  
  def show_all(self):
    print(f"All books at {self.name}")
    for i, book in enumerate(self.books, 1):
      if not book.checked_out:
        status = "Available for checkout"
      else:
        status = "Currently checked out"
      print(f"{i}.\nTitle: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}\nStatus: {status}")
      print("-"*50)
  
  def find_book(self, isbn):
    for book in self.books:
      if book.isbn == isbn:
        return book
    else: 
      return None 
  
def print_error(e):
  print(f"Error: {e}") 

def get_choice(): 
  while True: 
    try:
      choice = int(input("Menu:\n1. Add Book\n2. Checkout Book\n3. Return Book\n4. Remove Book\n5. Find Specific Book\n6. Show All Books\n7. Quit\n"))
      if choice < 1 or choice > 7: 
        raise ValueError("Please select between 1 and 7")
    except ValueError as e:
      print_error(e)
      continue
    else: return choice

def book_info():
  while True:
    try:
      title = input("Book title: ").title().strip()
      if title == '':
        raise ValueError("Book title can not be empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: break 
  
  while True:
    try:
      author = input("Author: ").title().strip()
      if author == '':
        raise ValueError("Author name can not be empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: break 
  
  while True:
    try:
      isbn = input("ISBN: ").strip() 
      if isbn == '':
        raise ValueError("ISBN can not be empty.")
      elif not isbn.isdigit():
        raise ValueError("Please only enter numerical values.")
    except ValueError as e:
      print_error(e)
      continue
    else: 
      isbn_number = int(isbn)
      break 
  
  return title, author, isbn_number

def get_isbn():
  while True:
    try:
      isbn = input("ISBN: ").strip() 
      if isbn == '':
        raise ValueError("ISBN can not be empty.")
      elif not isbn.isdigit():
        raise ValueError("Please only enter numerical values.")
    except ValueError as e:
      print_error(e)
      continue
    else: 
      isbn_number = int(isbn)
      break 
  
  return isbn_number
      
  
def main():
  library = Library("UCF Library")

  while True:
    book_found = False
    choice = get_choice()
    
    if choice == 1:
      title, author, isbn = book_info()
      current_book = Book(title, author, isbn)

      check_book = library.find_book(isbn)

      if check_book:
        print(f"{isbn} is already assigned to: {check_book.title}") 
        book_found =  True 

      if not book_found: 
        library.add_book(current_book)
    
    elif choice == 2:
      if not library.books: 
        print("No books in the system to show. Add some books!")
      else: 
        print("Currently Available: ")
        available = library.show_available()
        
        if available: 
          print("Which book would you like to checkout?")
          isbn = get_isbn() 
          find_book = library.find_book(isbn)

          if find_book:
            library.checkout_book(find_book)
            book_found = True
        
          if not book_found: 
            print(f"{isbn} not found inside system. No book has been checked out.")

    elif choice == 3:
      if not library.books: 
        print("No books in system to return. Add some books!")
      else: 
        print("Checked out books: ")
        check = library.show_checked_out() 

        if check: 
          print("Which book would you like to return?: ")
          isbn = get_isbn()
          find_book = library.find_book(isbn)

          if find_book:
            library.return_book(find_book)
            book_found = True
          
          if not book_found:
            print(f"{isbn} not found inside system. No book has been returned.")

    elif choice == 4: 
      if not library.books: 
        print("No books in system to remove. Add some books!")
      else: 
        library.show_all() 
        print("Which book would you like to remove?")
        isbn = get_isbn() 
        find_book = library.find_book(isbn) 
      
        if find_book:
          library.remove_book(find_book)
          book_found = True

        if not book_found:   
          print(f"{isbn} has not been assigned. No book is removed.")

    elif choice == 5: 
      if not library.books: 
        print("No books in system. Add some books!")
      else:
        isbn = get_isbn()
        find_book = library.find_book(isbn)

        if find_book:
          print("\n" , find_book)
          book_found = True
        
        if not book_found:
          print(f"{isbn} has not been assigned. No book found.")

    elif choice == 6: 
      if not library.books:
        print("No books to show. Add some books!")
      else:
        library.show_all() 
    
    elif choice == 7: break
    
    


if __name__ == "__main__":
  main() 

