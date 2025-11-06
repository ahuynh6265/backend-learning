'''
i = 3
while i!= 0:
  print("meow")
  i -= 1 
  '''

'''
while True:
  n = int(input("What is n?: "))
  if n > 0: break

for i in range(n):
  print("meow") 
'''

def main():
  number = get_number()
  meow(3)

def get_number():
  while True:
    n = int(input("What's n?: "))
    if n > 0: break
  return n

def meow(n):
  for i in range(n):
    print("meow")

main()