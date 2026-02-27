class Movie:
  def __init__(self, title, director, year):
    self.title = title 
    self.director = director
    self.year = year 
    self.watched = False 
    self.rating = None
 

  def mark_watched(self):
    self.watched = True 
  
  def add_rating(self, rating):
    if rating < 0 or rating > 10:
      raise ValueError("Please enter a rating between 1 and 10 ")
    else: 
      self.rating = rating 

  def __str__(self):
    if self.watched: 
      status = 'Watched' 
    else:
      status = "Haven't watched"
    
    if self.rating:
      check_rating = self.rating
    else:
      check_rating = "No rating"

    return f"""{self.title} 
    Director: {self.director}   
    Year: {self.year}   
    Status: {status}    
    Rating: {check_rating}\n {'-'*50}""" 

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")  

def main(): 
  movie_list = []
  while True: 
    try: 
      choice = int(input("Movie List Menu:\n1. Add Movie\n2. See List \n3. Mark Movie \n4. Quit\n"))
      if choice < 1 or choice > 4:
        raise ValueError("Please select between 1 and 4")
    except ValueError as e:
      print_error(e)
      continue

    if choice == 1: 
      title = input("Movie Name: ")
      director = input("Director Name: ")
      year = int(input("Release Year: "))
      
      movie = Movie(title, director, year) 
      
      while True: 
        try:
          watched = input("Did you watch this movie(y/n)?: ")
          if watched != 'y' and watched != 'n':
            raise ValueError("Please enter 'y' or 'n'.")
        except ValueError as e:
          print_error(e)
          continue
        else: break

      if watched == 'y': 
        movie.mark_watched()

        while True:
          try:
            rating = float(input("Add Rating: "))
          except ValueError as e:
            print_error(e)
            continue
          else: break

        try:  
          movie.add_rating(rating)
        except ValueError as e:
          print_error(e)
      movie_list.append(movie)
      
    elif choice == 2: 
      if not movie_list:
        print("No movies in list.")
      else:
        for i, movie in enumerate(movie_list,1):
          print(f"{i}. {movie}")
    
    elif choice == 3: 
      if not movie_list:
        print("No movies in list.")
        continue  
      for i, movie in enumerate(movie_list,1):
        print(f"{i}. {movie}")

      while True: 
        try: 
          select = int(input("Please select a movie you would like to mark.: "))
          if not 1 <= select <= len(movie_list):
            raise ValueError("Please select a number from list.")
        except ValueError as e:
          print_error(e)
          continue
        else: break
      
      if not movie_list[select - 1].watched: 
        movie_list[select - 1].mark_watched()

        while True:
          try:
            rating = float(input("Add Rating: "))
          except ValueError as e:
            print_error(e)
            continue
          else: break
        movie_list[select - 1].add_rating(rating)
        print(f"Marked {movie_list[select - 1].title} as watched.")
      else:
        print(f"{movie_list[select - 1].title} is already marked as watched.")
    
    elif choice == 4: break 


    


if __name__ == "__main__":
  main() 
