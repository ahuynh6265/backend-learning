#create menu system that keeps track of users order and total 

#introductions 
print("Welcome to CAVA!")

#create and hold data for each user
user_data = {}

#how many people will order
user = int(input("How many people will be ordering?: "))




for i in range(user):
  #create cost variable
  total = 0
  tax = 1 + 0.06
  #create name
  name = input("What is the name for the order?: ")
  name = name.strip().title()

  #create loop for menu 
  while True:
    print("1. Start Order\n2. Show total\n3. End order")
    choice = int(input(f"Hello {name}! What would you like to do?: "))
    if choice == 1:
      print("1. Food\n2. Drink")
      itemChoice = int(input("What would you like to order?: "))
      if itemChoice == 1:
        print("1. Cava Bowl - $11.99\n2. Gyro - $10.99\n3. Kid's Meal - $6.99")
        foodchoice = int(input("What would you like?: "))
        if foodchoice == 1:
          total += 11.99
        elif foodchoice == 2:
          total += 10.99
        elif foodchoice == 3:
          total += 6.99
        else: 
          print("Input is wrong. Please try again.")
          continue
      elif itemChoice == 2:
        print("1. Water - $1.00\n2. Soda - $1.50")
        drinkchoice = int(input("What would you like to drink?: "))
        if drinkchoice == 1:
          total += 1
        elif drinkchoice == 2:
          total += 1.5
        else:
          print("Input is wrong. Please try again.")
          continue
      else:
        print("Invalid choice! Try again.")
        continue
    elif choice == 2:
      print(f"Your current total is currently ${total}")
    elif choice == 3:
      finaltotal = tax * total 
      user_data[name] = finaltotal
      print(f"Thank you for your purchase {name}! Your total comes out to ${finaltotal:.2f}.")
      break
    else:
      print("Input is wrong. Please try again.")
      continue
print("\n Today's Orders:")
for name, total in user_data.items():
    print(f"  {name}: ${total:.2f}")

