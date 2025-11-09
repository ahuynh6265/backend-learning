#input validator v2 
#ask for name, age, occupation, and address 

#create a list that holds a key:(name) and three values for each key:(age, occupation, address)

info = {}

print("User Registration")

#make code first then refactor into function then add exceptions 

def main():  
  while True: 
    name = get_name()
    age = get_age()
    occupation = get_occupation()
    address = get_address()
    create_info(name, age, occupation, address)

    #get choice using validating function
    user_choice = get_choice() 
    if user_choice == 'n':
      break
        
  print_info() 
  

def get_name():
  while True:
    try:
      name_input = input("What is your name?: ")
      name_input = name_input.strip().title()

      if len(name_input) == 0: 
        raise ValueError("Name cannot be empty.")
      if not name_input.replace(" ","").isalpha():
        raise ValueError("Name can only contain letters.")
      return name_input
      
    except ValueError as e:
      print_errors(e)

def get_age(): 
  while True:
    try:
      age_input = input("How old are you?: ")
      age = int(age_input)
      if age < 18 or age > 150:
        raise ValueError("Please enter an appropriate age.")
      return age
    except ValueError as e: 
      print_errors(e)

def get_occupation(): 
  while True:
    try: 
      occupation = input("What is your occupation?(leave empty if unemployed): ")
      occupation = occupation.strip().capitalize() 

      if len(occupation) == 0:
        occupation = ("Unemployed")
      elif not occupation.replace(" ", "").isalpha():
        raise ValueError("Occupation is not valid.")
      return occupation 
    except ValueError as e: 
      print_errors(e)

def get_address():
  while True: 
    try: 
      address = input("Where do you live?: ")
      address = address.strip().title()
      if len(address) == 0:
        raise ValueError("Please enter an address.")
      return address
    except ValueError as e:
      print_errors(e)

def create_info(name, age, occupation, address):
  info[name] = age, occupation, address 
  return info

def get_choice(): 
  while True:
    choice = input("Would you like to register another user?(y/n)")
    try:
      if choice.lower() == 'n':
        return 'n'
      elif choice.lower() == 'y':
        return 'y'
      else: 
        raise ValueError("Please enter y/n")
    except ValueError as e:
      print_errors(e) 

def print_info():
  for i, (name, details) in enumerate(info.items(), 1):
    print(f"{i}: {name}: ")
    for detail in details:
      print(f"  - {detail}")
  

def print_errors(e):
  print(f"Invalid input: {e}")
  print("Please try again. \n")



main() 

  



