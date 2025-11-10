#temperature conversion program
#11/9/25
#time spent: 20min 
def c_to_f(c):
  return (c * 9/5) + 32

def f_to_c(f):
  return (f - 32) * 5/9

print("Temperature Converter")
try:
  while True:
    print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celcius\n3. Quit ")
    while True:
      try:
        choice = int(input("What would you like to do?: "))
        if choice < 1 or choice > 3:
          raise ValueError("Input has to be between 1 and 3!")
      except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.")
      else: break

    if choice == 1:
      while True:
        try:
          celcius = float(input("What's the temperature?(in celcius): "))
          if celcius < -273.15:
            raise ValueError("Temperature is below zero!")
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again")
        else: break
      tempChange = c_to_f(celcius)
      print(f"The temperature {celcius:.2f} in Fahrenheit is {tempChange:.2f}")
    
    elif choice == 2:
      while True:
        try:
          fahrenheit = float(input("What's the temperature?(in fahrenheit): "))
          if fahrenheit < -459.67:
            raise ValueError("Temperature is below zero!")
        except ValueError as e:
          print(f"Error: {e}")
          print("Please try again")
        else: break
      tempChange = c_to_f(fahrenheit)
      print(f"The temperature {fahrenheit:.2f} in celcius is {tempChange:.2f}")

    else: 
      print("Thank you for using the temperature converter!")
      break
except KeyboardInterrupt:
  print("\nTemperature Conversion program interrupted.")