import re 

def extract_url(text):
  pattern = r'https?://[^\s]+|www\.[^\s]+'
  urls = re.findall(pattern, text)
  return urls 

def main(): 
  all_urls = []
  try:
    while True: 
      text = input("Enter text('quit' to exit): ")
      if text == 'quit': break
      result = extract_url(text)
      if result:
        clean_results = [url.rstrip('.,:;!?)') for url in result]
        all_urls.extend(clean_results)
        print(f"{len(result)} URL(s) have been added.")
      else: print("Text does not include any URLs.")

    if all_urls:
      print("Websites listed: ")
      for i, url in enumerate(all_urls, 1):
        print(f"{i}: {url}")
    else:
      print("No websites found.")
  except KeyboardInterrupt: 
    print("")
    print("Program interrupted ")
    if all_urls:
      print("Websites before interruption: ")
      for i, url in enumerate(all_urls, 1):
        print(f"{i}: {url}")
    else:
      print("No websites found.")

if __name__ == "__main__":
  main()
