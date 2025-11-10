#BMI Calculator v2 with exceptions 
#basic bmi calculator with name and bmi assigned 
#time spent: 27 min

data = {}

print("BMI Calculator v2")

try:

  def calculate_bmi(weight, height):
    return weight/ height ** 2

  def bmi_response(bmi):
    print(f"{name}, your BMI is: {bmi:.2f}")
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
    return(print(category, advice))

  while True: 
    while True:
      try:
        name = input("What is your name?: ").strip().title()
        if len(name) == 0:
          raise ValueError("Name cannot be empty!")
        if not name.replace(" ", "").isalpha():
          raise ValueError("Name can only contain letters!")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break

    while True:
      try:
        weight = int(input(f"Hello {name}, what is your weight?(in kg): "))
        if weight <= 0 or weight > 500:
          raise ValueError("Weight must be between 0 and 500 kg")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break

    while True:
      try:
        height = float(input("What is your height?(in m): "))
        if height <= 1 or height > 3:
          raise ValueError("Height must be between 1 and 3 m")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    
    bmi = calculate_bmi(weight, height)
    data[name] = round(bmi, 2)
    bmi_response(bmi)

    while True:
      try:
        another = input("Would you like to add another user?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input is not 'y' or 'n'")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break
    if another == 'y': continue
    else: break

  print("\nAll user's BMI: ")
  for i, (name, bmi) in enumerate(data.items(), 1):
    print(f"{i}. {name}: {bmi}")

except KeyboardInterrupt:
  print("\nBMI Calculator interrutped")
  if data:
    print("Data logged before interruption:")
    for i, (name, bmi) in enumerate(data.items(), 1):
      print(f"{i}. {name}: {bmi}")
  else:
    print("No data logged.")




