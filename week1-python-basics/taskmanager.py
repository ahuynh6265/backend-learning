#basic task manager menu with exceptions
# 11/9/2025 - day 6
# 45 mins

taskList = []
completedList = []

print("Task Manager Menu: ")



try:
  while True: 
    print("1. Add Task\n2. View Tasks\n3. Complete Tasks\n4. Exit")
    try:
      choice = int(input("What would you like to do?: "))
      if choice == 1:
        while True:
          try:
            task = input("What task would you like to add?: ")
            task = task.strip().capitalize()
            if len(task) == 0:
              raise ValueError("Task should not be left empty.")
            if task in taskList:
              raise ValueError("Task has already been added!")
          except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
          else: break

        taskList.append(task)
        print(f"{task} has been added!")

      elif choice == 2:
        if taskList: 
          for i, task in enumerate(taskList, 1):
            print(f"{i}: {task}")
        else:
          print("Nothing to do!")

      elif choice == 3:
        while True:
          try:
            task = input("What task would you like to complete?: ")
            task = task.strip().capitalize()
            if len(task) == 0:
              raise ValueError("Task should not be left empty.")
          except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
          if task in taskList:
            taskList.remove(task)
            completedList.append(task)
            print(f"{task} has been completed!")
            break
          else:
            print(f"{task} does not exist in the list.")
            break
      elif choice == 4:
        print("Thank you for using the task manager menu!")
        break
      else:
        raise ValueError("Number selected is not 1 - 4")
    except ValueError as e:
      print(f"Error: {e}")
      print("Please try again")

  print("\nFinal Task List:")
  for i, task in enumerate(taskList, 1):
    print(f"{i}: {task}")
  
  print("\n Completed List:")
  for i, task in enumerate(completedList, 1):
    print(f"{i}: {task}")


except KeyboardInterrupt:
  print("\nTask Manager interrupted")
  if taskList: 
    print("Tasks added before interruption:")
    for i, task in enumerate(taskList, 1):
      print(f"{i}: {task}")

