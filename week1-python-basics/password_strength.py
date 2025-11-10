#password strength checker 


data = {}

def check_password_strength(password):
  score = 0 

  if len(password) >= 8: 
    score += 1
  if len(password) >= 12:
    score += 1 
  if any(c.isupper() for c in password):
    score += 1
  if any(c.islower() for c in password):
    score += 1
  if any(c.isdigit() for c in password):
    score += 1 
  if any(c in "!@#$%&*" for c in password):
    score += 1
  
  return score 

print("Password Strength Checker")
print("Let's make your username and password!")
try: 
  while True:
    while True:
      user = input("Create your username: ").strip() 
      try:
        if user in data:
          raise ValueError("Username already exists!")
        if len(user) == 0: 
          raise ValueError("Username cannot be left empty!")
        if len(user) > 30:
          raise ValueError("Username is too long!")
        if ' ' in user:
          raise ValueError("Can't have spaces in name!")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    
    while True:
      password = input(f"Hello {user}, please create your password: ")
      try:
        if len(password) == 0:
          raise ValueError("Password cannot be left empty!")
        if len(password) > 30:
          raise ValueError("Password is too long!")
        if ' ' in password:
          raise ValueError("Can't have spaces in password!")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: 
        print("Password has been created!")
        score = check_password_strength(password)
        if score <= 2:
          print("Password is weak. Make a new one.")
          continue
        elif score <= 4: 
          print("Password is decent. Could be stronger")
        else:
          print("Password is strong!")
        data[user] = password
        break
    while True:
      try:
        another = input("Would you like to create another user?(y/n): ")
        if another.lower() != 'y' and another.lower() != 'n':
          raise ValueError("Not a valid choice.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if another == 'y': continue
    else: break

  print("All the users: ")

  for i, (user, password) in enumerate(data.items(), 1):
    print(f"{i}. {user}: {password}")

except KeyboardInterrupt:
  print("Program cancelled.")
 





