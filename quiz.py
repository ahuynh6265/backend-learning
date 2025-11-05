#set score 
score = 0 

print("Week 0 Quiz Questions")
#create quiz questions 

#question 1
q1 = input("What is the function that allows you to print out what you write?: ")
if q1.lower() == "print":
  score += 1 
else:
  print("Incorrect, answer is print()")

#question 2
q2 = input("How do you ask for the user's input?: ")
if q2.lower() == "input":
  score += 1
else:
  print("Incorrect, answer is input()")

#question 3
q3 = input("What is one way to join multiple arguments into function?: ")
if q3 == "+":
  score += 1
elif q3 == ",":
  score += 1
else:
  print("Incorrect two ways you can join arguments together is + or ,")

#quiz total 
total = float(score/3)
total = round(total, 2)
print(total)
if total == 1:
  print("Congrats you got 100% on the test")
else:
  print("Sorry you failed, try again")
  
