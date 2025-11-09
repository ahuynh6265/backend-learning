import random 
import time

#create guessing game with exceptions 
#maybe score tracker and user input for difficulty 



def get_attempts():
  while True:
    try:
      attempts = int(input("How many attempts would you like?: "))
      if not attempts.is_integer():
        raise ValueError("Please enter an integer")
      else: return attempts
    except ValueError as e:
      print(f"Error: {e}")
      print("Please try again")

def gg_games(attempts, name): 
    time.sleep(1)
    print("Let me think of a number")
    time.sleep(1)
    print("I'm thinking of a number 1 - 20!")
    randNum = random.randint(1,20)

    for j in range(attempts):
      count = attempts - (j + 1)
      while True:
        try:
          userGuess = int(input("Guess a number!: "))
          if userGuess > 20 or userGuess < 1: 
            raise ValueError(f"{userGuess} is out of range!")
          elif not userGuess.is_integer():
            raise ValueError("Please enter an integer")
          else: break
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again")

      if userGuess == randNum: 
        print(f"{name} has guessed {userGuess} in {j + 1} attempts! {name} wins!")
        return True
      elif userGuess < randNum and j < attempts:
        print(f"{userGuess} is too low. Guess higher!")
        print(f"You have {count} attempts remaining")
      elif userGuess > randNum and j < attempts: 
        print(f"{userGuess} is too high. Guess lower!")
        print(f"You have {count} attempts remaining")
      
      if userGuess != randNum and (j + 1) >= attempts:
        print(f"{name} has failed to guess the number {randNum} and is out of attempts. Computer wins!")
        return False


def main(): 

  #intros
  print("Guessing Game V2")

  while True: 
    name = input("What is your name?: ").strip().title() 
    try:
      if not name.isalpha():
        raise ValueError("Your name must only contain characters.")
      else: break
    except ValueError as e:
      print(f"Error: {e}")
      print("Please try again")

  attempts = get_attempts()
  gg_games(attempts, name)




main() 

'''
bugs to note:

.is_integer() doesn't work on int
Missing KeyboardInterrupt
Name validation too strict


'''



