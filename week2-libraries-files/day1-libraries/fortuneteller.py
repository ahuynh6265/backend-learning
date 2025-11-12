#basic fortune teller with shuffle
#11/12/25
#time spent: 20min
import random

fortunes = [
    "You will have a great day!",
    "Good fortune is coming your way.",
    "A surprise awaits you soon.",
    "Your hard work will pay off.",
    "An exciting opportunity approaches.",
    "You will learn something valuable today.",
    "Success is in your near future.",
    "A new friendship will form soon."
]

try:
  def print_error(e): 
      print(f"Error: {e}")
      print("Please try again.")

  def another_fortune():
      while True:
        try:
          another = input("Would you like another fortune?(y/n): ")
          if another != 'y' and another != 'n':
            raise ValueError("Input has to be 'y' or 'n'." )
        except ValueError as e:
          print_error(e)
        else: break
      if another == 'y': return True
      else: return False

  def add_name():
    while True:
      try: 
        name = input("What is your name?: ").strip().title()
        if len(name) == 0:
          raise ValueError("Name can't be left empty.")
        if not name.replace(" ","").isalpha():
          raise ValueError("Name can only contain characters.")
      except ValueError as e:
        print_error(e)
      else: 
        return name 

  def main():
    while True:
      name = add_name()
      while True: 
        fortune = random.choice(fortunes)
        print(f"{name}, your fortune is: {fortune}")
        if another_fortune() == True: continue
        else: break 
      break

  main() 
except KeyboardInterrupt:
  print("\nFortune teller interrupted.")

