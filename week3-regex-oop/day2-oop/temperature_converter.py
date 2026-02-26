class Temperature:
  def __init__(self, degrees, unit):
    if not unit in ['F', 'C', 'K']:
      raise ValueError("Please select a valid unit.")
    self.degrees = degrees
    self.unit = unit
  
  def to_celsius(self):
    if self.unit == 'F':
      temp = (self.degrees - 32) * 5/9
      return temp
    elif self.unit == 'K':
      temp = self.degrees - 273.15
      return temp
    else: 
      return self.degrees
  
  def to_fahrenheit(self):
    if self.unit == 'C':
      temp = (self.degrees * (9/5)) + 32
      return temp
    elif self.unit == 'K': 
      temp = (self.degrees - 273.15) * (9/5) + 32
      return temp
    else: 
      return self.degrees
  
  def to_kelvin(self):
    if self.unit == 'F':
      temp = (self.degrees - 32) * (5/9) + 273.15
      return temp
    elif self.unit == 'C':
      temp = self.degrees + 273.15
      return temp
    else:
      return self.degrees

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")
  
def main():
  while True: 
    try:
      number = float(input("Enter a number: "))
      unit = input("Enter unit(F/C/K): ").strip().capitalize()

      convert_temp = Temperature(number, unit)  
    except ValueError as e :
      print_error(e)
      continue
    else: break 
  
  while True: 
    try: 
      choice = int(input("Temp Converter Menu:\n1. To Celsius\n2. To Fahrenheit\n3. To Kelvin\n4. Quit\n"))
      if choice < 1 or choice > 4:
        raise ValueError("Please select a number between 1 and 4.")
    except ValueError as e:
      print_error(e)
      continue

   
    if choice == 1: 
      temp = convert_temp.to_celsius()
      if temp != convert_temp.degrees:
        print(f"{convert_temp.degrees}{convert_temp.unit} converted to Celsius is: {temp:.3f}°C")
      else:
        print(f"Temperature is already in Celsius: {convert_temp.degrees}°C")
    
    elif choice == 2:    
      temp = convert_temp.to_fahrenheit()
      if temp != convert_temp.degrees:
        print(f"{convert_temp.degrees}{convert_temp.unit} converted to Fahrenheit is: {temp:.3f}°F")
      else:
        print(f"Temperature is already in Fahrenheit: {convert_temp.degrees}°F")
      
    
    elif choice == 3: 
      temp = convert_temp.to_kelvin()
      if temp != convert_temp.degrees:
        print(f"{convert_temp.degrees}{convert_temp.unit} converted to Kelvin is: {temp:.3f}K")
      else:
        print(f"Temperature is already in Kelvin: {convert_temp.degrees}K")
    
    elif choice == 4: break


if __name__ == "__main__":
  main() 
  
