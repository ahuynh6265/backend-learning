import json
import requests 
import sys

if len(sys.argv) != 2:
  sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=25&term=" + sys.argv[1])

o = response.json()

for i, result in enumerate(o["results"], 1):
  print(f"{i}. {result["trackName"]}")
