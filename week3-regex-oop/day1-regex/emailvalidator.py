#12/9/25
#first program after exams 
#email validator, save emails and print out all emails and number of them

import re

emails = []

def validate_email(email):
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  if re.match(pattern, email):
    return True
  else: return False

def another_email():
  while True:
    try:
      another = input("Would you like to add another email?(y/n): ")
      if another != 'y' and another != 'n':
        raise ValueError("Input has to be 'y' or 'n'." )
    except ValueError as e:
      print_error(e)
    else: break
  if another == 'y': return True
  else: return False

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")

def main():
  try:
    while True: 
      email = input("Enter email: ")
      if validate_email(email): 
        print(f"{email} validated.")
        emails.append(email)
        if not another_email(): break
      else:
        print("Invalid email, please try again")
    
    print(f"Total number of emails: {len(emails)}")
    for i, email in enumerate(emails, 1):
      print(f"{i}. {email}")
  except KeyboardInterrupt:
    print("")
    if emails:
      print(f"Total number of emails before cancellation: {len(emails)}")
      for i, email in enumerate(emails, 1):
        print(f"{i}. {email}")
    else:
      print("No emails saved.")

main()

