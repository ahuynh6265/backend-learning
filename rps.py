#rock paper scissors
import random 

#create choices for rps
choices = ["rock", "paper", "scissors"]

#initialize variables 
player = 0
computer = 0
tie = 0

#however many games
games = int(input("How many games do you want to play?: "))
for i in range(games):
  n = i + 1
  #generate randomly
  randChoice = random.choice(choices)
  playerChoice = input("Rock, Paper, or Scissors?: ")

  if playerChoice.lower() == randChoice:
    print(f"We both picked {playerChoice} it's a tie for Game {n}!")
    tie += 1
  elif (playerChoice.lower() == "rock" and randChoice == "scissors") or (playerChoice.lower() == "paper" and randChoice == "rock") or (playerChoice.lower() == "scissors" and randChoice == "paper"):
    print(f"Nice! You won Game {n} by picking {playerChoice}")
    player += 1
  else:
    print(f"That's too bad! I won Game {n} by picking {randChoice}")
    computer += 1

#determine victor
if player == computer:
  print(f"We both won {tie} games! It's a tie!")
elif player > computer: 
  print(f"You won {player} out of {games} games! We tied {tie} games. Congrats!")
else:
  print(f"Looks like I won {computer} out of {games} games! We tied {tie} games. Better luck next time.")

