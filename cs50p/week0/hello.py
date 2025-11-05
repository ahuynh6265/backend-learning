'''
#Ask user for name
name = input("What's your name?: ");

#remove whitespace from str and captilize name
name = name.strip().title(); 

#split user name into first and last
first, last = name.split(" "); 

#say hello to user 
#using mulitple arguments (,) automatically allocates a space compared to using + operator which makes one argument
print(f"Hello, {first}"); 
'''
def main():
  hello()
  name = input("What's your name?: ");
  hello(name); 

def hello(to="world"):
  print("hello", to); 

main(); 

