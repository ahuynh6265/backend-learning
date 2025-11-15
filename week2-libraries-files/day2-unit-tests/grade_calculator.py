#grade calculator with pytest 



def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")

def another_grade():
  while True:
    try:
      another = input("Would you like another grade?(y/n): ")
      if another != 'y' and another != 'n':
        raise ValueError("Input has to be 'y' or 'n'." )
    except ValueError as e:
      print_error(e)
    else: break
  if another == 'y': return True
  else: return False

def calculate_grade(score):
  if score < 0:
    raise ValueError("Grade can't be less than zero")
  if score > 100: 
    raise ValueError("Grade can't be more than 100")


  if score > 89: 
    return 'A'
  elif score > 79:
    return 'B'
  elif score > 69:
    return 'C'
  elif score > 59:
    return 'D'
  else:
    return 'F'

def get_gpa(grade):
  if grade == 'A':
    gpa = 4.0
  elif grade == 'B':
    gpa = 3.0
  elif grade == 'C':
    gpa = 2.0
  elif grade == 'D':
    gpa = 1.0
  else:
    gpa = 0

  return gpa 

def calculate_gpa(grades):
  if not grades: 
    raise ValueError("Empty list can't calculate GPA.")
  else: 
    totalgpa = 0
    for grade in grades: 
      gpa = get_gpa(grade)
      totalgpa += gpa
    return totalgpa / len(grades)



def main(): 
  #create list to hold grades 
  grades = []
  print("Grade Calculator")
  while True: 
    print("1. Add Grade\n2. Calculate GPA\n3. Quit")
    while True:
      try:
        choice = int(input("What would you like to do?: "))
        if choice < 1 or choice > 3:
          raise ValueError("Input has to be between 1 and 3.")
      except ValueError as e:
        print_error(e)
      else: break

    if choice == 1:
      while True: 
        score = int(input("Enter grade: "))
        letter = calculate_grade(score)
        grades.append(letter)
        if another_grade() == True: continue
        else: break

    elif choice == 2:  
      if grades:
        try:   
          gpa = calculate_gpa(grades)
          print(f"Classes taken: {len(grades)}")
          print(f"GPA: {gpa:.2f}")
        except ValueError as e:
          print_error(e)
      else:
        print("No grades added yet.")
 
    else: 
      break

if __name__ == "__main__":
  main()



    