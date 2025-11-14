#basic calculator with pytest 
#11/14/25 
#time spent: 30min

def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  if y == 0:
    raise ValueError("Can't divide by zero")
  return x / y
def exponent(n):
  return n*n

def x_y():
  x = int(input("What is x?: "))
  y = int(input("What is y?: "))
  return x, y

def main():
  print("Calculator")
  while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n6. Quit")
    choice = int(input("What would you like to do?: "))
    if choice == 1:
      x, y = x_y()
      print(f"{x} + {y} = {add(x, y)}")
    elif choice == 2:
      x, y = x_y()
      print(f"{x} - {y} = {subtract(x, y)}")
    elif choice == 3:
      x, y = x_y()
      print(f"{x} * {y} = {multiply(x, y)}")
    elif choice == 4:
      x, y = x_y()
      print(f"{x} / {y} = {divide(x, y):.2f}")
    elif choice == 5:
      n = int(input("What is n?: "))
      print(f"{n} squared is {exponent(n)}")
    else: break


if __name__ == "__main__":
  main()