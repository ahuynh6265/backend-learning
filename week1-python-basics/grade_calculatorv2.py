#grade calculator v2 
#keep it simple just practice adding exceptions

print("Grading Calculator v2")

#keeps total count
total = 0
try:
  while True:
    try:
      numGrades = int(input("How many grades would you like to enter?: "))
      if numGrades == 0: 
        raise ValueError("You must enter at least one grade")
    except ValueError as e:
      print(f"Error: {e}")
      print("Please enter a number.")
    else: break

  for i in range(numGrades):
    while True:
      try:
        grade = int(input("Please enter a grade (0 - 100): "))
        if grade < 0 or grade > 100:
          raise ValueError("Number is not between 0 and 100")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    total += grade 
    print(f"{grade} has been entered.")


  finaltotal =  total/numGrades
  print(f"Your final is a grade {finaltotal:.1f}%.")

  if finaltotal >= 90: 
    print("You finish the semester with an A! Great job!")
  elif finaltotal >= 80:
    print("You finish the semester with an B! Good work!")
  elif finaltotal >= 70:
    print("You finish the semester with an C. You made it!")
  elif finaltotal >= 60:
    print("You finish the semester with a D. You will have to retake the class!")
  else:
    print("You finish the semester with an F. You will have to retake the class.")

except KeyboardInterrupt:
  print("\nGrade calculator interrupted.")

#time spent: 25mins 





