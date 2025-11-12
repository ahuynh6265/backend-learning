#practing with apis 
# dad jokes 
#time spent: 25min
import requests 
#import json -- used for testing

try:
  def print_error(e): 
        print(f"Error: {e}")
        print("Please try again.")

  def another_joke():
      while True:
        try:
          another = input("Would you like another dad joke?(y/n): ")
          if another != 'y' and another != 'n':
            raise ValueError("Input has to be 'y' or 'n'." )
        except ValueError as e:
          print_error(e)
        else: break
      if another == 'y': return True
      else: return False

  def print_joke():
    while True:
      try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"},timeout=5)
        response.raise_for_status()
        joke_data = response.json()
        print(f"{joke_data['joke']}")
      except requests.RequestException as e:
        print(f"API Error: {e}")
        print("Could not fetch joke please try again.")
      
      if another_joke() ==  True: continue
      else: break
    


  print("=== Dad Joke Generator ===\n")

  input("Press Enter for a dad joke... ")
  
  try:
      print_joke()
      # ... get and show joke
  except requests.RequestException as e:
      print(f"Error: {e}")

    
    
except KeyboardInterrupt:
  print("Program interrupted.")
