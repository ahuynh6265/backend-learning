class Rectangle:
  def __init__(self, height, width):
    if height < 1 or width < 1: 
      raise ValueError("Dimensions must be positive.")
    
    self.height = height
    self.width = width 
 

  def area(self):
    area = self.height * self.width
    return area 
  
  def perimeter(self):
    perimeter = 2 * (self.height + self.width)
    return perimeter
  
  def is_square(self):
    return self.height == self.width

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")  

 
    
def main():
  while True:
    try: 
      height = int(input("Height: "))
      width = int(input("Width: "))
   
      rectangle_lengths = Rectangle(height, width) 
    except ValueError as e:
      print_error(e)
      continue
    else: break

  while True: 
    try:   
      choice = int(input("Menu:\n1. Area\n2. Perimeter\n3. Check if square\n4. Quit\n"))
      if choice < 1 or choice > 4:
        raise ValueError("Please select between 1 and 4.")
    except ValueError as e:
      print_error(e)
      continue
    
    if choice == 1:
      area = rectangle_lengths.area()
      print(f"\nArea: {area}\n")

    elif choice == 2:
      perimeter = rectangle_lengths.perimeter()
      print(f"\nPerimeter: {perimeter}\n")

    elif choice == 3:
      square = rectangle_lengths.is_square()
      if square: print("\nRectangle is square\n")
      else: print("\nNot square\n")
    
    elif choice == 4: break



if __name__ == "__main__":
  main() 
