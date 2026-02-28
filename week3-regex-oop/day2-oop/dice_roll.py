import random

class Dice: 
  def __init__(self, sides=6):
    self.sides = sides
  
  def roll(self):
    return random.randint(1, self.sides)
  
  def roll_multiple(self, n):
    dice_list = []
    for i in range(n):
      dice_roll = random.randint(1,self.sides)
      dice_list.append(dice_roll)
      i += 1
    
    return dice_list 
      
  def __str__(self):
    return f"The dice is d{self.sides}:"

def print_error(e):
  print(f"Error: {e}") 

def get_choice(): 
  while True: 
    try:
      choice = int(input("\nDice Menu:\n1. Roll Once\n2. Roll Multiple\n3. Change Number of Sides\n4. Quit\n"))
      if choice < 1 or choice > 4: 
        raise ValueError("Please select between 1 and 4")
    except ValueError as e:
      print_error(e)
      continue
    else: return choice

def get_number():
  while True:
    try:
      number = int(input("How many die would you like to roll?: "))
      if number < 1:
        raise ValueError("Can't roll a zero or a negative number!")
    except ValueError as e:
      print_error(e)
      continue
    else: return number

def roll_another():
  while True: 
    try:
      another = input("Would you like to roll again(y/n)?: ")
      if another != 'y' and another != 'n':
        raise ValueError("Please pick 'y' or 'n'.")
    except ValueError as e:
      print_error(e)
      continue
    else: 
      if another == 'y': return True
      else: return False

def num_sides():
  while True:
    try:
      sides = int(input("How many sides is the dice?: "))
      if sides < 1:
        raise ValueError("Sides can't be zero or negative!")
    except ValueError as e:
      print_error(e)
      continue
    else:
      return sides

def main():
  sides = num_sides() 
  dice = Dice(sides)
  print(dice) 

  while True:
    choice = get_choice() 

    if choice == 1:
      while True: 
        roll = dice.roll()
        print(f"You rolled a {roll}!")

        if not roll_another(): break

    elif choice == 2:
      while True:
        number = get_number() 
        dice_list = dice.roll_multiple(number)
        print(f"You rolled {number}d{sides}: ")
        for i, roll in enumerate(dice_list, 1):
          print(f"{i}. {roll}")
        
        total = sum(dice_list)
        print(f"You rolled a total of {total}!")

        if not roll_another(): break
    
    elif choice == 3: 
      sides = num_sides() 
      dice = Dice(sides)
      print(dice)
    
    elif choice == 4: break
      


if __name__ == "__main__":
  main()

