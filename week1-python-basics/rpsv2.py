#make basic rock paper scissors with exceptions
#11/9/2025
#time to make: 30 mins
import random

rps = ['rock', 'paper', 'scissors']
userwin = 0
computerwin = 0

print("Rock, Paper, Scissors v2")
try:
  while True:
    while True:
      try:
        rpschoice = input("Rock, Paper, or Scissors?: ").strip().lower() 
        if len(rpschoice) == 0:
          raise ValueError("Input can not be empty!")
        if rpschoice != 'rock' and rpschoice !='paper' and rpschoice != 'scissors':
          raise ValueError("Input must be rock, paper, or scissors!")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again")
      else: break

    rpsrandom = random.choice(rps)

    if rpschoice == rpsrandom:
      print(f"You and the computer have both picked {rpschoice}. Run it back!")
      continue
    elif rpschoice == 'rock' and rpsrandom == 'scissors' or rpschoice == 'scissors' and rpsrandom == 'paper' or rpschoice == 'paper' and rpsrandom == 'rock':
      print("You win!")
      userwin += 1
    else:
      print("The computer wins.")
      computerwin += 1
    while True:
      try:
        another = input("Would you like to play another game?(y/n): ")
        another = another.lower().strip()
        if another != 'y' and another != 'n':
          raise ValueError("Invalid option!")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again")
      else: break
    if another == 'n': break
    else: continue
    

      

  print("\nFinal Results!")

  if userwin == computerwin:
    print(f"You and the computer have both won {userwin} games!")
  elif userwin > computerwin:
    print(f"Congrats! You won more games than the computer!\nYou: {userwin}\nComputer: {computerwin}")
  else:
    print(f"Nice Try! The computer won more games than you.\nYou: {userwin}\nComputer: {computerwin}")

except KeyboardInterrupt:
  print("\nGame interrupted.")
  if userwin != 0 or computerwin != 0:
    print(f"Score before game closure:\nYou: {userwin}\nComputer: {computerwin}")
  else:
    print("No games recorded.")