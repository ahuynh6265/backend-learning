#create and validate password 

#create multiple users and confirm password for each user
users = int(input("How many users?: "))

#create loop ask each user for name and pass
for i in range(users):
  
  #create username and password
  username = input("Create username: ")
  username = username.strip()
  password = input("Create your password: ")

  while True: 
    attempt = input("Confirm your password: ")
    if attempt != password:
      print(f"Password for {username} does not match. Please try again.")
    else: 
      print(f"Password for {username} is confirmed. Thank you!")
      break 


