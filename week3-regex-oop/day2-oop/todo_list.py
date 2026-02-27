class ToDoList:
  def __init__(self):
    self.list = []
  
  def complete_task(self, task_number):
    status = "Completed"
    if not 1 <= task_number <= len(self.list):
      raise ValueError("Please select a valid number.")
    index = task_number - 1
    self.list[index][1] = status 

  def add_task(self, task):
    status = "Incomplete"
    task_name = [t[0] for t in self.list]
    if task not in task_name:
      self.list.append([task, status])
    else:
      print("Task already in list.")
  
  def delete_task(self, task_number):
    if not 1 <= task_number <= len(self.list):
      raise ValueError("Please select a valid number.")
    index = task_number - 1
    self.list.pop(index)
  
  def task_list(self):
    print("\nFull Task List:")
    if self.list:
      for i, task in enumerate(self.list, 1):
        print(f"{i}. {task[0]}: {task[1]}")
    else:
      print("List is empty.")
  
  def pending_task(self):
    if self.list:  
      print("\nPending Task List:")
      pending = []
      for i, status in enumerate(self.list, 1): 
        if status[1] == "Incomplete":
          pending.append((i, status[0]))
          print(f"{len(pending)}. {status[0]}")
      return pending 
    return []

def print_error(e):
  print(f"Error: {e}")
  print("Please try again.")

def main():
  todo = ToDoList() 

  while True:
    try:
      choice = int(input("\nTask Menu:\n1. Add task\n2. Complete task\n3. Delete task\n4. View All\n5. Need to complete\n6. Exit\n"))
      if choice < 1 or choice > 6:
        raise ValueError("Please select between 1 and 6.")
    except ValueError as e:
      print_error(e)
      continue

    if choice == 1: 
      while True:
        try:
          task = input("Add task: ").capitalize().strip() 
          if task == '':
            raise ValueError("Task can't be left empty.")
        except ValueError as e:
          print_error(e)
          continue
        else: break
      todo.add_task(task)
    
    elif choice == 2: 
      if not any(task[1] == "Incomplete" for task in todo.list): 
        print("No task to complete.")
      else:
        pending = todo.pending_task()
        if pending:
          try:
            select = int(input("Select task to complete: "))
            if 1 <= select <= len(pending):
              real_position = pending[select - 1][0]
              todo.complete_task(real_position)
              print("Task completed.")
            else: 
              raise ValueError("Please select one of the numbers listed.")
          except ValueError as e:
            print_error(e)
            continue
    
    elif choice == 3:
      if not todo.list: 
        print("No tasks in list.")
      else: 
        todo.task_list() 
        select = int(input("Select task to delete: "))
        try:
          todo.delete_task(select)
        except ValueError as e:
          print_error(e)
          continue
      
    elif choice == 4:
      todo.task_list()
    
    elif choice ==  5:
      no_pending = not any(task[1] == "Incomplete" for task in todo.list)
      if no_pending:
        print("All tasks completed.")
      else:
        todo.pending_task() 

    elif choice == 6: break


if __name__ == "__main__":
  main()