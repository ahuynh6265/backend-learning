#want to take multiple grades 

#set total to 0 
total = 0

n = int(input("How many grades?: "))

#loop to add up grades
for i in range(n): 
  grade = float(input("Grade?: "))
  total += grade
  i += 1

#calc grade
total = total/n

#grade
print(f"Your grade average is{total: .2f}%")
if total >= 90:
  print("Great job!")
elif total >= 80:
  print("Nice work!")
elif total >= 70:
  print("Average")
elif total >= 60:
  print("You will need to retake the class")
else:
  print("You will need to retake the class")
