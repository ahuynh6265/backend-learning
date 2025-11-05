def main():
  x = float(input("What is x?: "));
  y = float(input("What is y?: "));
  print("Adding these numbers =",add(x,y))
  print("Subtracting these numbers =",subtract(x,y))
  print("Multiplying these numbers =",multiply(x,y))
  print("Diving these numbers =", round(divide(x,y), 2))
  print("The exponent of each number is=", exponent(x, y))
  print(f"The exponent of {x} to the {y} power is=",together(x,y))

def add(n1, n2): 
  return n1+n2; 
def subtract(n1,n2):
  return n1-n2; 
def multiply(n1,n2):
  return n1*n2; 
def divide(n1,n2):
  return n1/n2; 
def exponent(n1,n2):
  return n1**n1, n2**n2; 
def together(n1,n2):
  return n1**n2; 

main(); 