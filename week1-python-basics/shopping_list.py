#create a shopping list and create a total cost for each item 

shoppingList = []

#keeps check of what prices go with item
dataList = {}

#initialize cost 
total = 0
tax = 1.06

#intro
print("Welcome to Publix!")
print("Your Shopping List: ")

while True:
  #selection
  print("\n1. Add Item\n2. View List\n3. Remove Item\n4. Current Total\n5. Done Shopping")

  #input 
  choice = int(input("What would you like to do?: "))

  #safeguard 
  if choice > 5 or choice < 1:
    print("Please choose a valid action.")
    continue

  #create actions
  
  if choice == 1:
    #create another while loop so it takes us back to here instead of main menu when asked
    while True:
      item = input("What would you like to add?: ")
      item = item.strip().capitalize()
      price = float(input(f"How much does a {item} cost?: "))
      shoppingList.append(item)
      print(f'{item} has been added!')
      total += price
      dataList[item] = price

      #allow user to add another item without having to go back to main menu
      another = input("Would you like to add another item?(y/n): ")
      another = another.lower()
      if another == 'y': continue
      else: break

  elif choice == 2:
    for i, item in enumerate(shoppingList, 1):
      print(f"{i}. {item}")
 
  elif choice == 3:
    #create another while loop that allows us to remove without asking
    while True:
      item = input("Which item would you like to remove?: ")
      item = item.strip().capitalize()
      if item in shoppingList:
        shoppingList.remove(item)
        print(f"{item} has been removed!")
      else:
        print(f"{item} is not on list!")
      
      #deletes data and subtracts price from total
      if item in dataList:
        total -= dataList[item]
        del dataList[item]
        
      #allow user to remove another item without having to go back to main menu
      another = input("Would you like to remove another item?(y/n): ")
      another = another.lower()
      if another == 'y': continue
      else: break
    
  elif choice == 4:
    print(f"Your current total on the shopping list is ${total:.2f}")

  elif choice == 5:
    break

#show shopping list and prices 
print("\nHere is your list and cost for each item: ")
for item, price in dataList.items():
  print(f"{item}: ${price:.2f}")

finaltotal = total * tax
print(f"Your total pre tax comes out to: ${total}")
print(f"Your total after tax is: ${finaltotal:.2f}")
print("Thank you for shopping with us today!")



