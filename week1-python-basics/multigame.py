#create a multi game system that you play randomly based on how many games you want to play

import random 
import time #allows me to control how fast outputs show

#initial choices for games 
rps = ['rock', 'paper', 'scissors']
ht = ['heads', 'tails']
blackjack = random.randint(1,11)

#create dict to hold data of user and computer 
#key:(user/computer) value(wins of rps/blackjack/guessinggame)
gameTracker = {}
gamecount = 0
gameplayed = 0
userwin = 0
computerwin = 0

#lets make it so that if the winner wins the game they get to choose the next game 
#intros
 

def main(): 
  global userwin, computerwin, gamecount, gameplayed 
  print("Welcome to the multi-game tournament!")
  user = input("What is your name?: ").strip().title() 
  n = int(input(f"Welcome {user}! How many games do you want to play?: "))


  print("Let's see who gets to choose which game to play first!") 

  gamecount = n

  htchoice = input("Heads or tails?: ").strip()
  htrandom = random.choice(ht)
  current_chooser = ''
  if htchoice.lower() == htrandom:
    print(f"Nice! {user} gets to choose the first game!")
    current_chooser = 'user'
  else: 
    print("The computer will select the first game.")
    current_chooser = 'computer'
  
  if current_chooser == 'user':
    print("\nSelection Menu")
    print("1. Rock Paper Scissors\n2. Guessing Game\n3. Blackjack")
    choice = int(input("What game will you choose?: "))

  while gamecount > 0: 
    if current_chooser == 'user':
      if choice == 1: 
        print(f"{user} has chosen to play Rock, Paper, Scissors! Get Ready!")
        user_won = rps_game(user)
      elif choice == 2: 
        print(f"{user} has chosen Guessing Game! Get Ready!")
        user_won = gg_game(user)
      elif choice == 3:
        print(f"{user} has chosen Blackjack! Get ready")
        user_won = bj_game(user)
    else: 
      computerchoose = random.randint(1,3)
      if computerchoose == 1: 
        print("Computer has chosen to play Rock, Paper, Scissors! Get Ready!")
        user_won = rps_game(user)
        
      elif computerchoose == 2:
        print("Computer has chosen to play Guessing Game! Get Ready!")
        user_won = gg_game(user)
  
      elif computerchoose == 3:
        print("Computer has chosen to play Blackjack Get Ready!")
        user_won = bj_game(user)
      
    gamecount -= 1
    gameplayed += 1

    if user_won: 
      userwin += 1
      current_chooser = 'user'
      if gamecount > 0: 
        print("\nSelection Menu")
        print("1. Rock Paper Scissors\n2. Guessing Game\n3. Blackjack")
        choice = int(input("What game will you choose?: "))
    else:
      computerwin += 1
      current_chooser = 'computer'
      
  print("\n--- Tournament Over ---")
  # ... Add your final results print statements here
  print(f"Total Games Played: {gameplayed}")
  print(f"{user} wins: {userwin} | Computer wins: {computerwin}")

    
      


def rps_game(user): 
  while True: 
    rpsrandom = random.choice(rps)
    rpschoice = input("Rock, Paper, Scissors?: ").strip().lower()
    if rpschoice == rpsrandom: 
      print(f"{user} and the computer have both picked {rpschoice}! No ties allowed play again!")
      continue
    elif rpschoice == 'rock' and rpsrandom == 'scissors' or rpschoice == 'scissors' and rpsrandom == 'paper' or rpschoice == 'paper' and rpsrandom == 'rock': 
      print(f"{user} has won by choosing {rpschoice}! On to the next!")
      return True
    else:
      print(f"The computer has won by choosing {rpsrandom}! Computer will choose the next game!")
      return False
    
def gg_game(user): 
  attempts = 5
  ggrandom = random.randint(1,20)
  underattempts = 0
  for i in range(attempts):
    n = attempts - (i + 1)
    tries = i + 1
    ggchoice = int(input("Pick a number 1 - 20: "))
    if ggchoice == ggrandom: 
      print(f"{user} has guessed the correct number {ggchoice} in {tries} attempts! On to the next!")
      underattempts = 1
      return True
    elif ggchoice < ggrandom and i < attempts:
      print(f"{ggchoice} is too low! Guess higher!")
      print(f"You have {n} attempts left")
    elif ggchoice > ggrandom and i < attempts: 
      print(f"{ggchoice} is too high! Guess lower!")
      print(f"You have {n} attempts left.")

  if (i + 1) == attempts and underattempts == 0: 
    print(f"{user} has run out of attempts! The answer was {ggrandom}. Computer will choose the next game!")
    return False 

def bj_game(user): 
  while True:
    bjchoice = random.randint(1, 11) + random.randint(1, 11)
    bjrandom = random.randint(1, 11) + random.randint(1, 11)
    if bjchoice > 21:
      #on the rare chance we get 22 on draw
      bjchoice = random.randint(1, 11) + random.randint(1, 11)
    elif bjrandom > 21: 
      bjrandom = random.randint(1, 11) + random.randint(1, 11)

    #if user has 21 and computer doesnt
    elif bjchoice == 21 and bjrandom < 21: 
      print(f"BLACKJACK! {user} wins!")
      return True
    #if comuter has 21 and user doesnt
    elif bjrandom == 21 and bjchoice < 21:
      print(f"BLACKJACK! Computer wins! Computer will choose the next game!")
      return False
    #tie on draw
    elif bjchoice == 21 and bjrandom == 21:
      print(f"{user} and computer both have 21! RUN IT BACK!")

    else: 
      #show hand
      print(f"{user} Your hand is {bjchoice}")

      while True:
        hitorstay = input("Hit or stay?: ").lower().strip() 
        if hitorstay == 'hit':  
          bjchoice += random.randint(1, 11)
          print(f"Your hand is now {bjchoice}")
          if bjchoice > 21: 
            print(f"{user} has busted with {bjchoice}! Computer wins! Computer will choose the next game!")
            return False
          else: continue 
        elif hitorstay == 'stay': 
          if bjchoice > bjrandom and bjrandom > 16:
            print(f"The computer has {bjrandom}. {user} has won with {bjchoice}!")
            return True
          elif bjchoice > bjrandom and bjrandom <= 16:
            print(f"{user} has {bjchoice}!")
            
            print(f"The computer has {bjrandom}.")
            time.sleep(2)
            print("... The computer hits")

            while True: 
              bjrandom += random.randint(1, 11)
              if bjrandom <= 16: 
                print(f"The computer has {bjrandom} it will hit again")
                time.sleep(1)
                print("...")
                if bjrandom > 21: break
              else: break
            time.sleep(1)
            if bjrandom > bjchoice and bjrandom <= 21: 
              print(f"The computer has won with {bjrandom}! Computer will choose the next game!")
              return False
            elif bjrandom > 21:
              print(f"The computer has busted with {bjrandom}!")
              return True 
            elif bjchoice > bjrandom:
              print(f"The computer has {bjrandom}. {user} has won with {bjchoice}!")
              return True
            else: 
              print(f"{user} and computer both have {bjchoice}! RUN IT BACK!")
          else: 
            print(f"The computer has {bjrandom}. {user} has lost with {bjchoice}!")
            return False
          

main()