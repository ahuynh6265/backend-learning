#program that reads text file and calculates statistics
#time spent: 50 min

'''
read a text file
count total lines
count total words
count total characters 
count average words per line
display results nicely
'''

'''
v1: 
had some problems with filenotfoundexception, was using the wrong return types 
had keyboard interruption outside the main function, started moving the keyboard interruption inside the loop for cleaner code
'''


def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")

def another_line():
  while True:
    try:
      another = input("Would you like to add another line?(y/n): ")
      if another != 'y' and another != 'n':
        raise ValueError("Input has to be 'y' or 'n'." )
    except ValueError as e:
      print_error(e)
    else: break
  if another == 'y': return True
  else: return False

def write_line():
  line = input("Write a line: ").capitalize().strip()
  with open('files_statistics.txt', 'a') as file:
    file.write(f"{line}\n")
  

def reset_txt():
  with open('files_statistics.txt', 'w') as file:
    file.write("")   
  

def read_line():
  linetotal = 0
  wordtotal = 0
  characterstotal = 0 
  try:
    with open('files_statistics.txt') as file: 
      for line in file:
        linetotal += 1

        words = len(line.split())
        wordtotal += words

        characters = len(line.rstrip().replace(" ", ""))
        characterstotal += characters
  except FileNotFoundError: pass
  
  return linetotal, wordtotal, characterstotal

  

def main():
  try:
    while True:
      print("1. Add Line\n2. Read Line\n3. Clear Text\n4. Quit")
      while True:
        try:
          choice = int(input("What would you like to do?: "))
          if choice < 1 or choice > 4:
            raise ValueError("Input has to be between 1 and 4")
        except ValueError as e:
          print_error(e)
        else: break

      if choice == 1: 
        while True:
          write_line() 
          if another_line() == True: continue
          else: break 
      
      elif choice == 2:
        linetotal, wordtotal, characterstotal = read_line() 
        if linetotal != 0:
          print(f"Line total: {linetotal}")
          print(f"Word total: {wordtotal}")
          print(f"Character total: {characterstotal}")
          print(f"Average word per line: {wordtotal/linetotal:.1f}")
        else: 
          print("Text file is empty.")

      elif choice == 3:
        reset_txt()
        print("File reset.")  
      
      else: 
        break
  except KeyboardInterrupt:
    print("\nProgram interrupted.")

if __name__ == "__main__":
  main()