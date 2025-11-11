#random choice program 
#make a list of chores shuffle them and distribute each one to a family member 
#11/10/25
#time: 50 min
import random 

taskList = []
allNames = []

try:
  def another_input():
    while True:
      try:
        another = input("Would you like to enter another?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input has to be 'y' or 'n'." )
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if another == 'y': return True
    else: return False

  print("Random Chore Distributor")

  while True: 
    while True:
      try:
        name = input("Add a name: ").title().strip()
        if len(name) == 0:
          raise ValueError("Name can't be left empty.")
        if not name.replace(" ", "").isalpha():
          raise ValueError("Name can only contain characters.")
        if name in allNames:
          raise ValueError("Name has already been added.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    allNames.append(name)
    if another_input() == False: break
    else: continue



  while True:
    while True:
      try:
        chore = input("Add a chore: ").strip().capitalize()
        if len(chore) == 0:
          raise ValueError("CHore can't be left empty.")
        if chore in taskList:
          raise ValueError("Chore has already been added.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    taskList.append(chore)

    if (len(taskList) - 1) > len(allNames):
      print("Too many chores, not enough people!")
      break

    if another_input() == False: 
      if len(taskList) < len(allNames):
        nochore = "No chores for you!"
        taskList.append(nochore)
      break
    else: continue


  random.shuffle(taskList)

  #use zip to print one pair (name and chore) per iteration
  for name, chore in zip(allNames, taskList):
    print(f"{name}: {chore}")
except KeyboardInterrupt:
  print("\nProgram closed.")
  if allNames and taskList:
    print("Tasks assigned before interruption: ")
    for name, chore in zip(allNames, taskList):
      print(f"{name}: {chore}")
  else:
    print("Nothing assigned.")