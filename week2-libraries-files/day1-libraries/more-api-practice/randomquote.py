#random quote api
#11/14/25
#time spent: 60 min 


import requests
#import json - for testing
import random

try:
  def print_error(e, error_type="Error"): 
    print(f"{error_type}: {e}")
    print("Please try again.")


  def get_quote():
    try:
      response = requests.get("https://dummyjson.com/quotes/random", timeout=5)
      response.raise_for_status()
      quote_data = response.json() 
      
      print(f"\"{quote_data['quote']}\"")
      print(f"- {quote_data['author']}")
    except requests.RequestException as e:
      print_error(e, "API Error")

  def quote_from_author(author):
    try:
      response = requests.get("https://dummyjson.com/quotes", timeout=5)
      response.raise_for_status()
      quote_data = response.json()
      quotes = quote_data['quotes']
    

      matches = [q for q in quotes if author.lower() in q['author'].lower()]

      if matches:  # If list has items
        quote = random.choice(matches)
        print(f"\"{quote['quote']}\"")
        print(f"— {quote['author']}")
      else:
          print(f"No quotes found for {author}")

    except requests.RequestException as e:
      print_error(e, "API Error")
    
  def main():
    while True:
        print("1. Get Quote\n2. Quote By Author\n3. Exit")

        while True: 
          try:
            choice = int(input("What would you like to do?: "))
            if choice < 1 or choice > 3:
              raise ValueError("Input has to be between 1 and 3")
          except ValueError as e:
            print_error(e)
          else: break

        if choice == 1:
          get_quote()
        elif choice == 2:
          author = input("Enter the author name: ")
          quote_from_author(author)
        else: break

  main()
except KeyboardInterrupt:
  print("Program interrupted.")