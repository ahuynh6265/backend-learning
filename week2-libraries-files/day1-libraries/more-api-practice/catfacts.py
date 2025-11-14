#cat fact api
#11/14/25
#time spent: 30min

import requests 
#import json - used for testing

try:
  def print_error(e): 
        print(f"Error: {e}")
        print("Please try again.")

  def another_fact():
      while True:
        try:
          another = input("Would you like another cat fact?(y/n): ")
          if another != 'y' and another != 'n':
            raise ValueError("Input has to be 'y' or 'n'." )
        except ValueError as e:
          print_error(e)
        else: break
      if another == 'y': return True
      else: return False

  def cat_fact():
    try:
      response = requests.get("https://catfact.ninja/fact", timeout=5)
      response.raise_for_status()
      fact_list = response.json() 
      print(f"{fact_list['fact']}")
    except requests.RequestException as e:
      print(f"API Error: {e}")
      print("Could not fetch cat fact please try again.")
      
      
  def main():
    while True:
      print("\nCat fact: ")
      cat_fact()
      if another_fact() == True: continue
      else: break
    
  main()
except KeyboardInterrupt:
  print("Cat Fact program interrupted.")