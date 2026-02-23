#basic username validator 

import re

def validate_user(username):
  pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,15}$'
  
  if not re.match(pattern, username): return False
  if '__' in username: return False
  return True

def main(): 
  while True: 
    username = input("Enter username ('quit' to exit): ").strip()
    if username.lower() == 'quit': break 

    if validate_user(username):
      print(f"{username} approved.")
    else:
      print(f"{username} not allowed.")

if __name__ == "__main__":
  main() 
