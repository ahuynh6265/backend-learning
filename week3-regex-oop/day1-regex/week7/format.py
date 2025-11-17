import re 
name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
  last = matches.group(1)
  first = matches.group(2)
  name = f"{first} {last}"
print(f"hello, {name}")