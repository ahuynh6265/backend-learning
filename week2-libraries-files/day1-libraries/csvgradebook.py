#gradebook with csv import
#11/11/25
#time spent: 40min

import csv 

#create dict to hold grade for each student and their grades 
grades = {}

print("CSV Gradebook")

def add_another(name):
  while True:
    try:
      another = input(f"Would you like to enter another grade for {name}?(y/n): ")
      if another != 'y' and another != 'n':
        raise ValueError("Input has to be 'y' or 'n'." )
    except ValueError as e:
      print(f"Error: {e}")
      print("Please try again.")
    else: break
  if another == 'y': return True
  else: return False

def add_student():
  while True:
    try:
      another = input("Would you like to enter another student?(y/n): ")
      if another != 'y' and another != 'n':
        raise ValueError("Input has to be 'y' or 'n'." )
    except ValueError as e:
      print(f"Error: {e}")
      print("Please try again.")
    else: break
  if another == 'y': return True
  else: return False
    

try: 
  while True:
    while True:
      try:
        name = input("What is the name of the student?: ").strip().title()
        if len(name) == 0: 
          raise ValueError("Input can't be empty.")
        if not name.replace(" ","").isalpha():
          raise ValueError("Name can only include characters.")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break

    #selection menu 
    while True: 
      print("1. Add Grade\n2. View Grades\n3. Export to CSV\n4. Quit")
      while True:
        try:
          choice = int(input("What would you like to do?: "))
          if choice < 1 or choice > 4:
            raise ValueError("Number has to be between 1 and 4.")
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again.")
        else: break
      
      if choice == 1: 
        while True: 
          while True:
            try: 
              grade = int(input(f"What grade would you like to add for {name}?(0-100): "))
              if grade < 0 or grade > 100:
                raise ValueError("Please enter a grade between 0 and 100.")
            except ValueError as e:
              print(f"Error: {e}")
              print("Please try again.")
            else: break

          #if student doesn't exist in gradebook create a list in dictionary for the student
          if name not in grades: 
            grades[name] = []
          
          grades[name].append(grade)
          
          print(f"{grade} has been added for {name}.")

          if add_another(name) == True: continue
          else: break
      
      elif choice == 2:

        if grades:
          for i, (name, grade) in enumerate(grades.items(),1):
            avg = sum(grade) / len(grade)
            print(f"{i}. {name}, GPA: {avg:.1f}%, {len(grade)} grades.")
        else:
          print(f"No grades added.")

      
      elif choice == 3:
        if grades:
          #open file for writing csv
          #'w' = write newline='' prevents blanklines
          with open('gradebook.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Student', 'Average', 'Total Grades'])

            for name, grade in grades.items():
              avg = sum(grade) / len(grade)
              writer.writerow([name, f"{avg:.1f}%", len(grade)])
          print("Exported to CSV.")
        else:
          print("Nothing to export.") 

      else:
        break 
    if add_student() == True: continue
    else: break
except KeyboardInterrupt:
  print("\nGradebook interrupted.")

    
        

