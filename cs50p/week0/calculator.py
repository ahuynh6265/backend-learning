'''
#you can nest variables
x = float(input("What is x?: ")); 
y = float(input("What is y?: "));

z = (x/y); 

print(f"{z:.3f}"); 
'''

def main():
  x = int(input("What's x?: "));
  print("x squared is", square(x)); 

def square(n):
  return n*n; 
main()