#dice roller
#11/9/25
#time spent: 20min 

import random

print("Dice Roller Simulator")
rollsHistory = []
try:
  while True: 
    print("1. Roll Dice\n2. View stats\n3. Clear history\n4. Quit")
    while True:
      try:
        choice = int(input("What would you like to do?: "))
        if choice < 1 or choice > 4:
          raise ValueError("Number has to be between 1 and 4.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break

    if choice == 1:
      while True:
        try:
          numDice = int(input("How many dice do you want to roll?(1 - 10): "))
          if numDice < 1 or numDice > 10:
            raise ValueError("Number has to be between 1 and 10.")
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again.")
        else: break

      while True: 
        try:
          sides = int(input("How many sides?(1 - 6): "))
          if sides < 1 or sides > 6:
            raise ValueError("Number has to be between 1 and 6.")
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again.")
        else: break

      rolls = [random.randint(1, sides) for i in range(numDice)]
      total = sum(rolls)

      print(f"\nRolled {numDice}d{sides}: {rolls}")
      print(f"Total: {total}")
      rollsHistory.append(total)
    
    elif choice == 2:
      if rollsHistory: 
        print(f"\n📊 Statistics:")
        print(f"Total rolls: {len(rollsHistory)}")
        print(f"Average: {sum(rollsHistory)/len(rollsHistory):.2f}")
        print(f"Highest: {max(rollsHistory)}")
        print(f"Lowest: {min(rollsHistory)}\n")
      else:
        print("No rolls yet!\n")
    
    elif choice == 3:
      rollsHistory.clear()
      print("History cleared!")
    else: 
      print("Dice Simulator ended! Thank you!")
      break

except KeyboardInterrupt:
  print("\nDice Roller interrutped")
  if rollsHistory: 
    print("Dice stats before interruption:")
    print(f"\n📊 Statistics:")
    print(f"Total rolls: {len(rollsHistory)}")
    print(f"Average: {sum(rollsHistory)/len(rollsHistory):.2f}")
    print(f"Highest: {max(rollsHistory)}")
    print(f"Lowest: {min(rollsHistory)}\n")
  else:
    print("No rolls yet!\n")

  