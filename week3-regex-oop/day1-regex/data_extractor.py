import re 

def date_extractor(text): 
  dates_pattern = r"(\d{1,2})/(\d{1,2})/(\d{4})"
  return re.findall(dates_pattern, text)

def phone_extractor(text):
  phone_pattern = r"\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})"
  return re.findall(phone_pattern, text)

def email_extractor(text):
  email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
  return re.findall(email_pattern, text)

def money_extractor(text):
  money_pattern = r"\$[\d,]+\.?\d{0,2}"
  return re.findall(money_pattern, text)

def date_format(month, day, year):
  return (f"{month}/{day}/{year}")

def number_format(area_code, first_three, last_four):
  return (f"({area_code}) {first_three}-{last_four}")

def get_all(text): 
  data = {
    'emails': email_extractor(text),
    'phones': phone_extractor(text),
    'dates': date_extractor(text),
    'money': money_extractor(text)
  }
  return data 

def main():

  text = input("Enter text: ")
  data = get_all(text) 

  if data['emails']:
    print(f"{len(data['emails'])} Email(s):")
    for email in data['emails']: 
      print(email)
  
  if data['dates']:
    print(f"{len(data['dates'])} Date(s):")
    for (month, day, year) in data['dates']:
      dates_formatted = date_format(month, day, year)
      print(dates_formatted)
  
  if data['phones']:
    print(f"{len(data['phones'])} Phone(s):")
    for (area_code, first_three, last_four) in data['phones']:
      phone_formatted = number_format(area_code, first_three, last_four)
      print(phone_formatted) 
  
  if data['money']: 
    print(f"{len(data['money'])} Dollar Amount(s):")
    for dollar in data['money']:
      print(dollar)
      
    


if __name__ == "__main__":
  main()
