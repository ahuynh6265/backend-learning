class Dog: 
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    
  def dog_years(self):
    return self.age * 7
  
  def birthday(self):
    self.age += 1
    return self.age
  
  def __str__(self):
    return f"""{self.name}: 
      Breed: {self.breed} 
      Age(dog years): {self.dog_years()}"""

def print_error(e):
  print(e)

def dog_info():
  while True: 
    try:
      name = input("Name: ").title().strip()
      if name == '':
        raise ValueError("Name can't be left empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: break 
  while True: 
    try:
      breed = input("Breed: ").title().strip()
      if breed == '':
        raise ValueError("Breed can't be left empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: break 
  while True: 
    try:
      age = int(input("Age: "))
      if age < 0:
        raise ValueError("Can't have a negative number.")
    except ValueError as e:
      print_error(e)
      continue
    else: break 
  
  return name, breed, age

def main():
  dogs = []

  while True: 
    while True:
      try:
        choice = int(input("\nDog Menu:\n1. Add dog\n2. Dog's birthday\n3. Show all info\n4. Show specific dog info\n5. Quit\n"))
        if choice < 1 or choice > 5:
          raise ValueError("Please select between 1 and 5.")
      except ValueError as e:
        print_error(e)
        continue
      else: break
      
    if choice == 1: 
      name, breed, age = dog_info()
      dog = Dog(name, breed, age)
      dogs.append(dog)
      
    elif choice == 2:
      if not dogs:
        print("No dogs yet! Add a dog first.")
        continue
      
      else:
        print("\nWhose birthday is it?:")
        for i, dog in enumerate(dogs, 1):
          print(f"{i}. {dog.name}")

        while True:
          try:  
            choice = int(input(("Select corresponding number: ")))
            if not 1 <= choice <= len(dogs):
              raise ValueError("Please select a valid number.")
          except ValueError as e:
            print_error(e)
            continue
          else: break
    
      dogs[choice - 1].birthday()
      print(f"Happy Birthday {dogs[choice - 1].name}! {dogs[choice - 1].name} is now {dogs[choice - 1].age} years old(in human years)!")
    
    elif choice == 3: 
      if not dogs:
        print("No dogs yet! Add a dog first.")

      else:
        print("\nDog List:")
        for i, dog in enumerate(dogs, 1):
          print(f"{i}. {dog}")
          print("-"*50)
    
    elif choice ==  4: 
      if not dogs:
        print("No dogs yet! Add a dog first.")
      
      else:
        print("\nWhich dog's info would you like to see?:")
        for i, dog in enumerate(dogs, 1):
          print(f"{i}. {dog.name}")
        
        while True:
          try:  
            choice = int(input(("Select corresponding number: ")))
            if not 1 <= choice <= len(dogs):
              raise ValueError("Please select a valid number.")
          except ValueError as e:
            print_error(e)
            continue
          else: break
        
        print(dogs[choice - 1])

    elif choice == 5: break 
        

if __name__ == "__main__":
  main()
   