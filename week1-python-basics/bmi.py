#bmi calculator 

#lets create a loop so we can add however many people and their name to it as well

people = int(input("How many people?: "))

for i in range(people):
  #ask for inputs
  name = input("What is your name?: ")
  name = name.strip().title()
  weight = float(input("What is your weight in Kg?: "))
  height = float(input("What is your height in Meters?: "))

  #calculate bmi 
  bmi = weight / (height ** 2)

  #show your bmi
  print(f"Your BMI is {bmi:.2f}")

  #tailored statements 
  if bmi < 18.5:
    category = "You are underweight."
    advice = "Consider eating more."
  elif bmi < 25:
    category = "You are normal weight."
    advice = "Stay consistent."
  elif bmi < 30: 
    category = "You are overweight."
    advice = "Eat healthier."
  else:
    category = "You are obese."
    advice = "Start excercising and eating heathier."
  print(f"{name}: {category} {advice}")

