#to do list that saves to json file 
#11/16/25
#time spent: 75 min
import json 
'''
add todo list 
view todo list
clear list
mark todo list task as done 
print list neatly 
'''


def write_json(todo_list):
  with open("todolist.json", 'w') as file:
    json.dump(todo_list, file, indent=2)

def clear_json():
  write_json([])

def read_json(): 
  try: 
    with open("todolist.json", 'r') as file:
      data = json.load(file)
      return data if isinstance(data, list) else []
  except (FileNotFoundError, json.JSONDecodeError):
    write_json([])
    return []

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")

def another_task():
  while True:
    try:
      another = input("Would you like to add another task?(y/n): ")
      if another != 'y' and another != 'n':
        raise ValueError("Input has to be 'y' or 'n'." )
    except ValueError as e:
      print_error(e)
    else: break
  if another == 'y': return True
  else: return False

def add_list(todo_list):
  task = input("Add a task: ").strip().capitalize()
  todo_list.append(task)
  print(f"{task} has been added.")

def view_list(todo_list):
  if not todo_list:
    print("No task in todo list.")
  else:
    for i, task in enumerate(todo_list, 1):
      print(f"{i}. {task}")

def complete_task(todo_list):
  if not todo_list:
    print("No task in list to complete.")
    return
  
  view_list(todo_list)
  while True:
    try:
      choice = int(input("What task would you like to complete?(enter number): "))
      if choice < 1 or choice > len(todo_list):
        raise ValueError("Select a valid number.")
    except ValueError as e:
      print_error(e)
    else: break
  
  task = todo_list.pop(choice - 1)
  print(f"{task} has been completed.")


def main():
  try:
    #load file once
    todo_list = read_json()
    while True:
      print(f"\nCurrent number of tasks: {len(todo_list)}")

      print("1. Add Task\n2. View List\n3. Complete Task\n4. Clear List\n5. Quit")
      while True:
        try:
          choice = int(input("What would you like to do?: "))
          if choice < 1 or choice > 5:
            raise ValueError("Input has to be between 1 and 5")
        except ValueError as e:
          print_error(e)
        else: break

      if choice == 1:
        while True:
          add_list(todo_list)
          write_json(todo_list)
          if another_task() == False: break
      
      elif choice == 2:
        view_list(todo_list)

      elif choice == 3:
        complete_task(todo_list)
        write_json(todo_list)
      
      elif choice == 4:
        #update file without having the file inside while loop
        todo_list.clear() 
        clear_json() 
      
      else: 
        print("Todo List closed.")
        break
  except KeyboardInterrupt:
    print("\nTo do list interrupted.")
    
    if not todo_list:
      print("To do list is empty.")
    else:
      print("Tasks before interruption: ")
      view_list(todo_list)


if __name__ == "__main__":
  main()
