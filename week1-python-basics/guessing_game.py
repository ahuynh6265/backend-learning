import random 

#give value range of random numbers 

n1 = int(input("Give me a starting number: "))
n2 = int(input("Give me last number in range: "))

randNum = random.randint(n1, n2)
attempts = int(input("How many attempts do you want?: "))

print(f"You will get {attempts} attempts.")

#create loop for attemps
for i in range(attempts):
  #set to 1 that way attempts is equal to loop
  n = i + 1
  guess = int(input("What is your guess?: "))
  if guess == randNum:
    print(f"You got it! The number was {guess}")
    print(f"Congrats! You got the answer in {n} attempts!")
    break
  elif guess < randNum:
    print("Sorry, try again. Too low! Guess higher!")
    print(f"You have {attempts - n} attempts left")
  elif guess > randNum:
    print("Sorry, try again. Too high! Guess lower!")
    print(f"You have {attempts - n} attempts left")
  else:
    print(f"Sorry! The number was {randNum}")
