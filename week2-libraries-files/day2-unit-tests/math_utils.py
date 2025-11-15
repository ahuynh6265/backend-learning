#tdd practice
#write tests first then main code after
#11/15/25
#time spent: 60min
import math

try:
  def print_error(e):
    print(f"Error: {e}")
    print("Please try again.")

  def another_number():
    while True:
      try:
        another = input("Would you like to enter another number?(y/n): ")
        if another != 'y' and another != 'n':
          raise ValueError("Input has to be 'y' or 'n'." )
      except ValueError as e:
        print_error(e)
      else: break
    if another == 'y': return True
    else: return False

  def is_even(n):
    return n%2 == 0

  def factorial(n):
    if n < 0:
      raise ValueError("Can't be a negative number")
    
    if n == 0 or n == 1:
      return 1
    else:
      result = 1
      for i in range(2, n + 1):
        result *= i
      return result

  def find_max(numbers):
    if not numbers:
      raise ValueError("List is empty")
    else:
      current_number = numbers[0]
      for number in numbers: 
        if number > current_number:
          current_number = number
      return current_number

  def is_prime(n):
    if n < 0:
      raise ValueError("Number can't be negative")
    if n < 2: return False

    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0: return False
    return True

    


  def main():
    print("Math Utils")
    while True:
      print("1. Is Even\n2. Factorial\n3. Find Max\n4. Is Prime\n5. Quit")
      while True:
        try:
          choice = int(input("What would you like to do?: "))
          if choice < 1 or choice > 5:
            raise ValueError("Input has to be between 1 and 5.")
        except ValueError as e:
          print_error(e)
        else: break

      if choice == 1:
        n = int(input("Enter a number: "))
        if is_even(n) == True: print(f"{n} is even.")
        else: print(f"{n} is odd.")
      
      elif choice == 2:
        n = int(input("Enter a number: "))
        print(f"The factorial of {n} is {factorial(n)}.")

      elif choice == 3:
        numbers = []
        while True:
          number = int(input("Enter a number: "))
          numbers.append(number)
          if another_number() == False: break
        print(numbers)
        print(find_max(numbers))

      elif choice == 4:
        n = int(input("Enter a number: "))
        if is_prime(n) == True: print(f"{n} is prime.")
        else: print(f"{n} is nonprime.")
    
      else: 
        print("Math Utils closed.")
        break



  if __name__ == "__main__":
    main()

except KeyboardInterrupt:
  print("\nProgram interrupted.")

