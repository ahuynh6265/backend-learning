class Student: 
  def __init__(self, name, id):
    self.name = name 
    self.id =  id 
    self.grades = []
    self.average = None
  
  def add_grade(self, grade):
    self.grades.append(grade)
  
  def get_average(self):
    self.average = sum(self.grades) / len(self.grades)

    return self.average

  def __str__(self):
    return f"Student: {self.name}\nID: {self.id}"

class Course: 
  def __init__(self, course_name="CS101"):
    self.course_name = course_name
    self.students = []
  
  def enroll_student(self, student):
    self.students.append(student)
  
  def remove_student(self, student):
     self.students.remove(student)
  
  def find_student(self, student_id):
    for student in self.students:
      if student_id == student.id:
        return student 
      
  
  def show_all(self): 
    print("Student List: ")
    for student in self.students: 
      if student.average == None:
        average = "No Grades Yet"
        print(f"Name: {student.name}\nID: {student.id}\nGrade Average: {average} ")
      else:
        print(f"Name: {student.name}\nID: {student.id}\nGrade Average: {student.average:.1f}%")
      print("-"*50)
  
  def get_class_average(self):
    print(f"Student List ({len(self.students)} Students Total): ")
    self.show_all() 

    student_averages = []
    for student in self.students:
      if not student.average == None:
        student_averages.append(student.average)
    
    try:
      if len(student_averages) == 0:
        raise ZeroDivisionError("No class average currently.")
    except ZeroDivisionError as e:
      print(e)
      return None

    final_average = sum(student_averages) / len(student_averages)
    return final_average

def print_error(e):
  print(f"Error: {e}") 

def get_choice(): 
  while True: 
    try:
      choice = int(input("Menu:\n1. Enroll Student\n2. Add Grade to Student\n3. Remove Student\n4. All Students\n5. Class Average\n6. Student Info\n7. Quit\n"))
      if choice < 1 or choice > 7: 
        raise ValueError("Please select between 1 and 7")
    except ValueError as e:
      print_error(e)
      continue
    else: return choice

def student_intials(first, last):
  first_inital = first[0]
  last_inital = last[0]
  intials = f"{first_inital}{last_inital}"
  return intials

def student_info(id_holder): 
  while True: 
    try: 
      first_name = input("First name: ")
      if first_name == "":
        raise ValueError("Name can't be left empty.")
      if not first_name.isalpha():
        raise ValueError("Name can only contain characters.")
    except ValueError as e:
      print_error(e)
      continue
    else: break
  
  while True: 
    try: 
      last_name = input("Last name: ")
      if last_name == "":
        raise ValueError("Name can't be left empty.")
      if not last_name.isalpha():
        raise ValueError("Name can only contain characters.")
    except ValueError as e:
      print_error(e)
      continue
    else: break
  
  name = f"{first_name} {last_name}"
  name = name.title()

  while True:
    try:
      id_number = input(f"Create {name}'s ID number: ")
      if id_number == "":
        raise ValueError("ID can't be left empty.")
      if not id_number.isdecimal():
        raise ValueError("ID can only be numerical values.")
      if len(id_number) != 7: 
        raise ValueError("ID must have 7 digits.")
      if id_number in id_holder:
        raise ValueError(f"{id_number} is already being used! Can't have duplicate ID numbers.")
    except ValueError as e:
      print_error(e)
      continue
    else: break
  
  intials = student_intials(first_name, last_name).upper()
  student_id = f"{intials}{id_number}"
  
  return name, student_id, id_number

def get_grade(name):
  while True: 
    try:
      grade = int(input(f"Add grade for {name}: "))
      if grade < 0:
        raise ValueError("Grade can't be less than 0.")
      if grade > 100: 
        raise ValueError("Grade can't be greater than 100")
    except ValueError as e:
      print_error(e)
      continue
    else: return grade

def get_id(): 
  while True: 
    try: 
      student_id = input("Enter ID: ")
      if student_id == "":
        raise ValueError("ID can't be left empty.")
    except ValueError as e:
      print_error(e)
      continue
    else: return student_id

def another_grade(name):
  while True: 
    try:
      another = input(f"Would you like to add another grade for {name}(y/n)?: ")
      if another != 'y' and another != 'n':
        raise ValueError("Please pick 'y' or 'n'.")
    except ValueError as e:
      print_error(e)
      continue
    else: 
      if another == 'y': return True
      else: return False

def main():
  course = Course()
  #holds numbers to check for dupes
  id_holder = []

  while True: 
    choice = get_choice()

    if choice == 1: 
      name, student_id, id_number = student_info(id_holder) 
      id_holder.append(id_number)
      student = Student(name, student_id)
      course.enroll_student(student)

      print("Student enrolled.")
      print(student) 
    
    elif choice == 2:
      if not course.students:
        print(f"No students in {course.course_name}")
      else:
        course.show_all() 
        print("Which student do you want to add a grade to?")
        student_id = get_id() 
        student = course.find_student(student_id)

        if student:
          while True: 
            grade = get_grade(student.name)
            student.add_grade(grade)
            student.get_average() 
            print(f"{grade} has been added to {student.name}'s gradebook.")
            if not another_grade(student.name): break
        else:
          print(f"No student with ID: {student_id} exists in {course.course_name}.")
    
    elif choice == 3:
      if not course.students:
        print(f"No students in {course.course_name}")
      else:
        student_id = get_id() 
        student = course.find_student(student_id)
        if student:
          print(f"{student.name} has been removed from {course.course_name}.")
          course.remove_student(student)
        else: 
          print(f"No student with ID: {student_id} exists in {course.course_name}.")
    
    elif choice == 4: 
      if not course.students:
        print(f"No students in {course.course_name}")
      else:
        course.show_all()

    elif choice == 5:
      if not course.students:
        print(f"No students in {course.course_name}")
      else:
        average = course.get_class_average() 
        if not average == None:
          print(f"Class Average: {average:.1f}%")
    
    elif choice == 6: 
      if not course.students: 
        print(f"No students in {course.course_name}")
      else:
        print("All Students:")
        course.show_all() 

        print("Which student's info would you like to view?")
        student_id = get_id() 
        student = course.find_student(student_id)

        if student:
          print("Student Info:")
          if student.grades: 
            print(f"Name: {student.name}\nID: {student.id}\nGrade Average: {student.average:.1f}%")
 
            print(f"Total Grades ({len(student.grades)}):")
            for i, grade in enumerate(student.grades,1): 
              print(f"{i}. {grade}%")
          
          else:
            print(f"Name: {student.name}\nID: {student.id}\nGrade Average: No Grades Yet")
          
        else: 
          print(f"No student with ID: {student_id} exists in {course.course_name}.")
    
    elif choice == 7: break 




if __name__ == "__main__":
  main()