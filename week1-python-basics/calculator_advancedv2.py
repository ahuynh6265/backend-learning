#new calculator with exceptions to stop program from crashing on error 

#maybe create a calcualtor with history? 
#list will contain numbers used and operator and show result 

showHistory = []

#intros 
print("Advanced Calculator V2")
print("Operators: +, -, *, /, **(power)")
print("Type 'quit' to close the calculator.\n")

while True: 

  try: 
    x_input = input("What is x?(or quit): ")
    if x_input.lower() == 'quit':
      break
    x = float(x_input)
    y_input = (input("What is y?: "))
    y = float(y_input)
  
    choice = input("Select your operation(+, -, *, /, **): ")
    choice = choice.strip()

    if choice == '+': 
      answer = x+y
    elif choice == "-":
      answer = x-y
    elif choice == "*":
      answer = x*y 
    elif choice == '/':
      if y == 0:
        raise ZeroDivisionError("Can't be divided by 0")
      answer = x/y
    elif choice == "**":
      answer = x**y
    else:
      raise ValueError(f"{choice} is not a valid operator")
    
    print(f"{x:.2f} {choice} {y:.2f} = {answer:.2f}")
    history = (f"{x:.2f} {choice} {y:.2f} = {answer:.2f}")
    showHistory.append(history)


  except ValueError as e:
    #catches any errors from int(input) and operator raise
    print(f"Error: {e}")
    print("Please enter valid numbers and operations.\n")

  except ZeroDivisionError as e:
      #catches the raise for zero division
      print(f"Math Error: {e}\n")

  except KeyboardInterrupt:
      print("\n\nInterrupted! Goodbye!")
      break

  except Exception as e:
      #catches any unforseen errors
      print(f"Unexpected error: {e}\n")
  
  
print("\nCalculator closed.")
print("History: ")
    
for i, history in enumerate(showHistory, 1):
  print(f"{i}: {history}")
  