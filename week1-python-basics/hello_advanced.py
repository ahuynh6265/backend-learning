#ask for inputs
print("Hello! Welcome to my program!"); 
name = input("What is your name?: ");
name = name.title().strip(); 
first, last = name.split();
age = int(input("How old are you?: ")); 



#say hello 
print(f"Hello, {name}"); 
print(f"Next year you will be, {1+ age}"); 
print(f"Your first name is {first} and your last name is {last}"); 
print(f"So you are {age} years old and your name is {name}"); 

#if statement 

if age <= 18: 
  print("You are still young!"); 
else:
  print("You are an adult!"); 


