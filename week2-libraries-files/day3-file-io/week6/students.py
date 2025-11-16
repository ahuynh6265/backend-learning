import csv

'''
students = []

with open('students.csv') as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name": row['name'], "home": row['home'], "age": row['age']})

def get_name(student):
  return student['name']


for student in sorted(students, key=lambda student: student['name']):
  print(f"{student['name']} is from {student['home']} and is {student['age']} years old.")
'''

name = input("What's your name?: ")
home = input("Where's your home?: ")

with open('students.csv', 'a') as file:
  writer = csv.DictWriter(file, fieldnames=['name', 'home'])
  writer.writerow({'name': name, 'home': home})

