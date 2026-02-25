class Student_Tracker:
  def __init__(self, name, id, gpa=0):
    self.name = name 
    self.id = id 
    self.gpa = gpa
    self.grades = []

  def add_grade(self, grade):
    letter_grades = ['A', 'B', 'C', 'D', 'F']
    if not grade in letter_grades:
      raise ValueError("Please enter a valid grade.")
    self.grades.append(grade)
  
  def get_gpa(self): 
    if self.grades:
      self.gpa = 0
      for grade in self.grades: 
        if grade == 'A': self.gpa += 4.0
        elif grade == 'B': self.gpa += 3.0
        elif grade == 'C': self.gpa += 2.0
        elif grade == 'D': self.gpa += 1.0
        else: self.gpa += 0
      
      self.gpa = self.gpa/len(self.grades)
    
  def __str__(self):
    if self.grades: 
      return f"Name: {self.name}\nID: {self.id}\nGPA: {self.gpa:.2f}"
    else:
      return f"Name: {self.name}\nID: {self.id}\nNo Grades Yet"
  
  @classmethod
  def get(cls):   
    name = input("Name: ").capitalize().strip() 
    if not name:
      raise ValueError("Can't be left empty.")
    id = input("ID: ")
    if not id:
      raise ValueError("Can't be left empty.")

    return cls(name, id)

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.") 

def another_input():
    while True:
      try:
        another = input("Would you like to add another student?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input has to be 'y' or 'n'." )
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if another == 'y': return True
    else: return False

def print_students(student_list):
  print("Student Info:")
  for i, student in enumerate(student_list, 1):
    print(f"{i}. {student}\n")


def main(): 
  student_list = []
  while True: 
    try:
      student_info = Student_Tracker.get() 
    except ValueError as e:
      print_error(e)
      continue

    while True: 
      try: 
        add_grade = input("Add grade (A/B/C/D/F/'q to quit'): ").capitalize()
        if add_grade.lower() == 'q': break
        student_info.add_grade(add_grade) 
      except ValueError as e:
        print_error(e)
        continue

    student_info.get_gpa()
    print(student_info)
    student_list.append(student_info)
    if not another_input(): break
  
  print_students(student_list)

if __name__ == "__main__":
  main()

