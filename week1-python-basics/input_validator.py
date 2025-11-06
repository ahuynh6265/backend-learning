#create a system where you ask for someones name and age must be valid inputs 

#create and hold data of user
user_data = {}

n = int(input("How many people?: "))

#create loop for input 
for i in range(n):
  while True: 
    name = input("What is your name?: ")
    name = name.strip().title()
    if not name.isalpha(): 
      print("This is not a valid name. Please try again.")
      continue
    print(f"Hello, {name}!")
    break

  while True:  
    age = input("How old are you?: ")
    if not age.isdigit():
      print("This is not a number. Please try again!")
      continue

    age = int(age)

    if age < 18:
      print(f"You are {age}! You are too young!")
      continue
    elif age > 150:
      print(f"You can't be {age}! That is impossible!")
      continue
    else:
      print(f"Your name is {name} and you are {age} years old!")
      break
  user_data[name] = age

print("\nName and Age:")
for name, age in user_data.items():
  print(f"{name}: {age}")




