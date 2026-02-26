class ShoppingCart:
  def __init__ (self):
    self.shopping_list = { 
    }
    

  def add_item(self, item, price): 
    if item == "":
      raise ValueError("Can not be left empty.")
    if price > 0:
      self.shopping_list[item] = price
      print(f"{item} has been added to shopping list.")
    else: 
      raise ValueError("Price is invalid.")
  
  def remove_item(self, item):
    if item in self.shopping_list:
      del self.shopping_list[item]
      print(f"{item} has been removed.")
    else:
      raise KeyError("Item does not exist in shopping list.")
  
  def check_total(self):
    if self.shopping_list:
      total = sum(self.shopping_list.values())
      return total
    else:
      return 0
  
  def check_list(self):
    print("Items List: ")
    if self.shopping_list:
      for i, (key, value) in enumerate(self.shopping_list.items(), 1):
        print(f"{i}. {key}: ${value:.2f}")
    else:
      print("No items in cart.")
        
  
  def apply_discount(self, total): 
    if total > 100:
      total = total * .80
      return total
    else: return total
  
  def __str__(self):
    return f"{self.shopping_list}"
  
def print_error(e):
  print(f"Error: {e}")
  print("Please try again.") 

def another_input(word):
    while True:
      try:
        another = input(f"Would you like to {word} another item?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input has to be 'y' or 'n'." )
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if another == 'y': return True
    else: return False

def reciept(total, finaltotal):
  if finaltotal > 0 and finaltotal == total: 
    print(f"You did not qualify for this discount. Your final total: ${finaltotal:.2f}")
  elif finaltotal > 0: 
    print(f"You qualified for the discount! Your total is now 20% off!: ${finaltotal:.2f}")
  else:
    print("You didn't buy anything today :(") 


def main():
  items = ShoppingCart()
  print("="*50)
  print("\nShopping Cart\n")
  print("="*50,"\n")

  while True: 
    print("Menu:\n1. Add Item\n2. Remove Item\n3. Check Total\n4. Check List\n5. Quit\n")
    try:
      choice = int(input("Enter choice: "))
      if choice < 1 or choice > 5:
        raise ValueError("Choice must be between 1 and 5")
    except ValueError as e:
      print_error(e)
      continue

    if choice == 1: 
      word = "add"
      while True:
        item = input("Name of item: ").strip().title().strip() 
        price = float(input("Price of item: "))
        price_rounded = round(price, 2)
        items.add_item(item, price_rounded)
        if not another_input(word): break 
    
    elif choice == 2: 
      word = "remove"
      while True:
        item = input("Name of item to delete: ").title().strip()
        items.remove_item(item)
        if not another_input(word): break 
    
    elif choice == 3: 
      total = items.check_total()
      print(f"Your current total: ${total}")
    
    elif choice == 4:
      items.check_list()

    elif choice == 5: break
  
  total = items.check_total()
  finaltotal = total
  discount = input("Would you like to see if you qualify for the discount?(y/n): ").lower().strip() 
  if discount == 'y': 
    finaltotal = items.apply_discount(total)
  
  reciept(total, finaltotal)


if __name__ == "__main__":
  main()
      
