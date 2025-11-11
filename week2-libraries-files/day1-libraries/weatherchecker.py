#basic weather checker with free api

import requests 
import sys

def get_weather(city):
  try:
    url = (f"https://wttr.in/{city}?format=3")
    response = requests.get(url, timeout=5)
    response.raise_for_status() 
    return response.text.strip() 
  except requests.RequestException as e:
    return f"Error: {e}"

print("=== Weather Checker ===\n")

#if more than 1 argument is called in terminal
if len(sys.argv) > 1:
    city = ' '.join(sys.argv[1:]) #join into one string
else:
    #user has to input
    city = input("Enter city: ").strip().title()

if city:
    weather = get_weather(city)
    print(f"\n{weather}")
else:
    #if no argument is given
    print("City name required.")
