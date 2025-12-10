#12/09
#basic phone formatter wwith regex findall

import re 

def extract_number(phone):
  pattern = r"\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})"
  matches = re.findall(pattern, phone)
  if matches: 
    return matches
  else: return False 

def format_number(area_code, first_three, last_four):
  return (f"({area_code}) {first_three}-{last_four}")

  

def main():
  all_numbers = []
  try: 
    while True: 
      text = input("Enter phone number('quit' to exit): ").strip()
      if text == 'quit': break
      phone_numbers = extract_number(text)
      if phone_numbers:
        for (area_code, first_three, last_four) in phone_numbers:
          formatted = format_number(area_code, first_three, last_four)
          all_numbers.append(formatted)
          print(f"{formatted} has been saved.")
      else:
        print("There is not a valid number in the text please try again.")
    
    if all_numbers:
      print(f"Number of contacts: {len(all_numbers)}")
      for i, numbers in enumerate(all_numbers, 1):
        print(f"{i}: {numbers}")
    else:
      print("No numbers saved")
  except KeyboardInterrupt:
    print("")
    if all_numbers:
      print(f"Number of contacts before interruption:{len(all_numbers)}")
      for i, numbers in enumerate(all_numbers, 1):
        print(f"{i}: {numbers}")
    else:
      print("No numbers saved")

main() 