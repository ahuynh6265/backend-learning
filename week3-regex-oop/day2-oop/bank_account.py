class BankAccount: 
  def __init__(self, name, balance=0):
    self.name = name
    self.balance = balance
  
  def deposit(self, amount):
    if amount < 1:
      raise ValueError("Please enter a valid number.")
    self.balance += amount
  
  def withdraw(self, amount):
    if amount < 1: 
      raise ValueError("Please enter a valid number.")
    if amount > self.balance:
      raise ValueError("Can't withdraw more than account balance.")
    self.balance -= amount
  
  def __str__(self):
    return f"{self.name} has a balance of: ${self.balance}"
  
  @classmethod
  def get(cls):
    name = input("Name: ")
    balance = int(input("Balance: "))

    return cls(name, balance)

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")  

def main():
  bank_details = BankAccount.get() 
  print(bank_details)

  while True: 
    try: 
      answer = input("Bank Menu:\n1. Deposit\n2. Withdraw\n3. Get Balance\n4. Quit\n")
      if not answer: 
        raise ValueError("Answer can not be left empty.")
      choice = int(answer)
      if choice < 1 or choice > 4: 
        raise ValueError("Please pick between 1 and 4.")
    except ValueError as e:
      print_error(e)
      continue

    if choice == 1: 
      try:
        amount = int(input("How much money would you like to add to your bank?: "))
        bank_details.deposit(amount)
        print(f"${amount} has been added into your account.")
      except ValueError as e:
        print_error(e)

    elif choice == 2:
      try: 
        amount = int(input("How much would you like to withdraw?: "))
        bank_details.withdraw(amount)
        print(f"You have withdrawn ${amount} from your account.")
      except ValueError as e:
        print_error(e)
        
    elif choice == 3:
      print(bank_details)
    elif choice == 4: break

if __name__ == "__main__":
  main() 



