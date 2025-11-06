#family household todo list where each family member has designated tasks maybe?? 

#create data that holds outside of loop
tasksList = {}
family = {}
completedFam = {}

print("Family To-do List Organizer")

#input for number of people in family 
n = int(input("How many people are in your family?: "))

#create loop for n amount of members
for i in range(n):
  name = input("Who are you assiging these tasks to?: ")
  name =  name.strip().title()
  print(f"Hello {name}, what would you like to do?: ")

  #initialize everything
  tasksList[name] = {"high": [], "medium": [], "low": []}
  family[name] = []
  completedFam[name] = []

  while True:
    #create selection menu and input
    print("\n1. Add Task.\n2. View Tasks.\n3. Complete Task.\n4. Clear Tasks.\n5. Exit.")
    choice = int(input("What would you like to do?: "))

    # add another while loop for repeat task
    if choice == 1: 
      while True:
        task = input("What is the task?: ")
        task = task.strip().capitalize()

        #goes into dictionary and inserts into which list based on priority chose
        #another loop incase they make a mistake choosing priority
        while True:
          priority = input("What is the priority?(high/medium/low): ")
          priority = priority.lower()
          if priority in tasksList[name]:
            tasksList[name][priority].append(task)
            #assign the family memeber and the task
            family[name].append(task)
            print(f"{task} has been inserted into {priority} priority!")
            break
          else:
            print(f"Sorry, {priority} does not exist. Please try again.")
            continue
      
        #allows user to enter another task without resetting menu
        another = input("Would you like to add another task?(y/n): ")
        another = another.lower() 
        if another == 'y': continue
        else: break 

    elif choice == 2:
      print(f"{name}'s tasks: ")
      #initilize total task number
      total = 0
      #check to see how many tasks fall into each priority
      for priority in ["high", "medium", "low"]:
        if tasksList[name][priority]:
          print(f"\n{priority.upper()}: ")
          for i, task in enumerate(tasksList[name][priority], 1):
            print(f"{i}: {task}")
            #counts the task 
            total += 1
      if total == 0:
        print("No tasks to be completed.")
    
    elif choice == 3:
      #create loop for possibility user completed task in different priority
      while True:
        priority = input("Which priority is the task located in?(high/medium/low): ")
        priority = priority.lower() 

        #while loop for easier input
        while True:

          #checks to see if the priority selected is in the list
          #this only shows all the tasks in said priority and not the entire list
          if priority in tasksList[name] and tasksList[name][priority]:
            print(f"\n{priority.upper()}: ")
            for i, task in enumerate(tasksList[name][priority], 1):
              print(f"{i}: {task}")
            
            #create while loop to safeguard incase user error
            while True:
              #input for deletion
              # subtract 1 to be in line with index 
              taskNumber = int(input("Select the number of the task that you have completed.: ")) - 1
              if 0 <= taskNumber < len(tasksList[name][priority]):
                #name and delete the task
                completed = tasksList[name][priority].pop(taskNumber)
                # adds the completed task to different list
                completedFam[name].append(completed)
                print(f"{completed} has been completed!")
                break
              else: 
                print("Invalid choice. Please try again.")
                continue
              
          #allows user to complete another task without resetting menu
          another = input("Have you completed another task in this priority?(y/n): ")
          another = another.lower() 
          if another == 'y': continue
          else: break 
        #for different priority
        another = input("Have you completed another task in a different priority?(y/n): ")
        another = another.lower() 
        if another == 'y': continue
        else: break 
    
    elif choice == 4:  
      confirm = input("Are you sure you want to CLEAR the list?(y/n): ")  
      if confirm == 'y':
        #resets list
        tasksList[name] = {"high": [], "medium": [], "low": []}
        family[name] = []
        completedFam[name] = []
        print("Task list is cleared!")
  
    elif choice == 5:
      break
    else: 
      print(f"{choice} is not a valid option. Please try again.")
      continue

print("\nREMAINING TASKS:")
#.keys takes only the names 
for name in family.keys():
    print(f"\n{name}:")
    total = 0
    for priority in ["high", "medium", "low"]:
        if tasksList[name][priority]:
            print(f"  {priority.upper()}:")
            for task in tasksList[name][priority]:
                print(f"    - {task}")
                total += 1
    if total == 0:
        print("All done!")

print("\nCOMPLETED TASKS:")
for name, completed in completedFam.items():
    print(f"\n{name}:")
    if completed:
        for task in completed:
            print(f"  - {task}")
    else:
        print("None yet")


    




