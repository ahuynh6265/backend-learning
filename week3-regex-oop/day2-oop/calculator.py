class Calculator:
  def __init__(self):
    self.calculator_history = []
    
  def add(self, a, b):
    c_add = a + b
    rounded = f"{round(c_add, 1):g}"
    self.calculator_history.append([(f"{a:g} + {b:g}"), (f"{rounded}")])
    print(f"{a:g} + {b:g} = {rounded}")
    return c_add

  def subtract(self, a, b):
    c_sub = a - b
    rounded = f"{round(c_sub, 1):g}"
    self.calculator_history.append([(f"{a:g} - {b:g}"), (f"{rounded}")])
    print(f"{a:g} - {b:g} = {rounded}")
    return c_sub

  def multiply(self, a, b):
    c_mul = a * b
    rounded = f"{round(c_mul, 1):g}"
    self.calculator_history.append([(f"{a:g} * {b:g}"), (f"{rounded}")])
    print(f"{a:g} * {b:g} = {rounded}")
    return c_mul

  def divide(self, a, b):
    try:
      c_div = a / b
      rounded = f"{round(c_div, 1):g}"
      self.calculator_history.append([(f"{a:g} ÷ {b:g}"), (f"{rounded}")])
      print(f"{a:g} ÷ {b:g} = {rounded}")
      return c_div

    except ZeroDivisionError:
      print("Error: Cannot divide by zero.")
      return

  def get_history(self):
    if not self.calculator_history: 
      print("\nNo History.")
    
    else: 
      print("\nCalculator History: ")
      for i, problem in enumerate(self.calculator_history, 1):
        print(f"{i}. {problem[0]} = {problem[1]}")
    
  def clear_history(self): 
    if not self.calculator_history:
      print("\nNo history to clear.")
    
    else: 
      self.calculator_history = []
      print("\nHistory has been cleared.")

def print_error(e):
  print(f"Error: {e}") 

def get_choice(): 
  while True: 
    try:
      choice = int(input("\nCalculator Menu:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Clear History\n7. Quit\n"))
      if choice < 1 or choice > 7: 
        raise ValueError("Please select between 1 and 7")
    except ValueError as e:
      print_error(e)
      continue
    else: break
  
  return choice    

def get_numbers(): 
  while True: 
    try:
      a = float(input("Enter first number: "))
    except ValueError as e:
      print_error(e)
      continue
    else: break

  while True: 
    try:
      b = float(input("Enter second number: "))
    except ValueError as e:
      print_error(e)
      continue
    else: break  

  return a, b

def main():
  calculator = Calculator() 

  while True:
    choice = get_choice() 

    if choice == 1: 
      a, b = get_numbers() 
      calculator.add(a,b)
    
    elif choice == 2:
      a, b = get_numbers()
      calculator.subtract(a, b)
    
    elif choice == 3:
      a, b = get_numbers()
      calculator.multiply(a, b)
    
    elif choice == 4: 
      a, b = get_numbers()
      calculator.divide(a, b)
      
    elif choice == 5:
      calculator.get_history() 
    
    elif choice == 6: 
      calculator.clear_history() 
    
    elif choice == 7: break 


if __name__ == "__main__":
  main() 