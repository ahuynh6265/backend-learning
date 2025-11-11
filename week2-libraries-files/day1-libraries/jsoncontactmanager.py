#json contact manager 
#11/10/25
#time: 40min
import json

FILENAME = "contacts.json"

try:
  def load_contacts():
    try:
      with open(FILENAME, 'r') as f:
        return json.load(f)
    except FileNotFoundError:
      return {}
    
  def save_contacts(contacts):
    with open(FILENAME, 'w') as f:
      json.dump(contacts, f, indent=2)

  def another_input(term):
    while True:
      try:
        another = input(f"Would you like to {term} another contact?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input has to be 'y' or 'n'." )
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if another == 'y': return True
    else: return False
      

  contacts = load_contacts()
  print(f"Contact Manager Loaded {len(contacts)} contacts.\n")

  while True:
    print("1. Add\n2. View\n3. Delete\n4. Quit")
    while True:
      try:
        choice = int(input("What would you like to?: "))
        if choice < 1 or choice > 4:
          raise ValueError("Input must be between 1 and 4.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again")
      else: break
    
    if choice == 1: 
      while True:
        while True:
          try:
            name = input("What is the name of the contact?: ").strip().title()
            if len(name) == 0:
              raise ValueError("Name can't be empty.")
            if not name.replace(" ", "").isalpha():
              raise ValueError("Name can only contain characters.")
            if name in contacts:
              raise ValueError("Name already has a number.")
          except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
          else: break


        while True:  
          try: 
            number = input("What is their number?: ").strip()
            if len(number) == 0:
              raise ValueError("Number can't be empty.")
            if not number.isdigit():
              raise ValueError("Number can only be digits")
          except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
          else: break
        contacts[name] = number
        save_contacts(contacts)
        print(f"{name} has been saved!")

        if another_input("enter") == False: break
        else: continue

    elif choice == 2:
      if contacts: 
        for i, (name, number) in enumerate(contacts.items(), 1):
          print(f"{i}. {name}: {number}")
      else:
        print("Contact list is empty.")
    
    elif choice == 3: 
      while True:
        while True:
          try:
            name = input("What is the name of the contact?: ").strip().title()
            if len(name) == 0:
              raise ValueError("Name can't be empty.")
            if not name.replace(" ", "").isalpha():
              raise ValueError("Name can only contain characters.")
          except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
          else: break
        if name in contacts:
          del contacts[name]
          save_contacts(contacts)
          print(f"{name}'s contact has been deleted!")
        else: 
          print(f"{name} does not exist in contact list.")
        
        if another_input("delete") == False: break
        else: 
          if not contacts:
            print("No more contacts to delete.")
            break
          continue
    
    else:
      print("Contact List Manager closed!")
      break
except KeyboardInterrupt:
  print("\nContact Manager interrupted.")
  if contacts:
    print("Contacts currently saved:")
    for i, (name, number) in enumerate(contacts.items(), 1):
      print(f"{i}. {name}: {number}")
  else:
    print("Contact list is empty.")
  

