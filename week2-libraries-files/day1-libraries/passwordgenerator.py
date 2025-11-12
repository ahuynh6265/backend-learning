import random
#random password generator for a user
#give option for user to regenerate if password is not to standards
#time to make: 45min

#review: don't use global variables harder to maintain

#create list to hold data and user 
try:
  while True: 
    try:
      user = input("What is your username?: ")
      if len(user) == 0:
        raise ValueError("Username can't be left empty.")
      if len(user) > 32:
        raise ValueError("Username is too long.")
    except ValueError as e:
      print(f"Error: {e}")
      print("Please try again.")
    else: break

  user_and_pass= {user: []}

  def generate_password(user, length):
    lowercase =  "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper() 
    numbers = "0123456789"
    special = "!@#$%&*"

    #combine into one string
    allchars = lowercase + uppercase + numbers + special

    #generate a random letter from each case and add to password list(total 4)
    user_and_pass[user].append(random.choice(lowercase))
    user_and_pass[user].append(random.choice(uppercase))
    user_and_pass[user].append(random.choice(numbers))
    user_and_pass[user].append(random.choice(special))

    #generate range and minus 4 from range since we already have 4 chose from earlier
    for i in range(length - 4):
      user_and_pass[user].append(random.choice(allchars))
    
    #join each string generated and return 
    user_and_pass[user] = ''.join(user_and_pass[user])
    return user_and_pass

  def regen_password():
    while True:
      try:
        regenerate = input("Would you like to generate a new password?(y/n): ")
        if regenerate != 'y' and regenerate != 'n':
          raise ValueError("Input has to be 'y' or 'n'.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if regenerate == 'y': return True
    else: return False

  def print_password():
    print("User and Password:")
    for user, password in user_and_pass.items():
      print(f"{user}: {password}")

  def main():
    global user_and_pass
    while True: 
      while True:
        try: 
          pass_length = int(input(f"Hello {user}, what length would you like your password to be?(8-32): "))
          if pass_length < 8 or pass_length > 32:
            raise ValueError("Input must be between 8 and 32 digits.")
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again.")
        else: break 
      generate_password(user, pass_length)
      print(f"Password has been generated: {user_and_pass[user]}!")

      if regen_password() == True: 
        print(f"{user_and_pass[user]} has been deleted. Generating new password.")
        user_and_pass = {user: []}
        continue
      else: break
  
    print_password()

  main() 
except KeyboardInterrupt:
  print("\nPassword generator interrupted.")