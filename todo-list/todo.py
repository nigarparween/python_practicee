tasks = []

def save_tasks():
    with open("tasks.txt", "w" ) as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip()) 

    except FileNotFoundError:
        pass                   


#Function to add a task 
def add_task():
    task = input("Enter your task: ")
    if task == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")

#Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")

        for index, task in enumerate(tasks, start=1):
            print(index, ".",task)


#Function to delete a task
def delete_task():
    if len(tasks) == 0:
        print("No tasks available to delete.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(index, ".", task)
        try:
            task_number = int(input("Enter the task number to delete: "))


            if task_number >= 1 and task_number <= len(tasks):
                tasks.pop(task_number - 1)
                save_tasks()
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number.")


#Function to clear all tasks 
def clear_tasks():
    tasks.clear()
    save_tasks()
    print("All tasks cleared successfully!")      


#Function to update a task           
def update_task():
    if len(tasks) == 0:
        print("No tasks available to update.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(index, ".", task)

        try:
            task_number = int(input("Enter the task number to update: "))

            if task_number >= 1 and task_number <= len(tasks):
                new_task = input("Enter the new task: ")
                if new_task == "":
                    print("Task cannot be empty!")
                else:
                    tasks[task_number - 1] = new_task
                    save_tasks()
                    print("Task updated successfully!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!") 

load_tasks()

# menu code
while True:
    print("\n---- TO-DO LIST ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Update Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        add_task()

    # View Tasks
    elif choice == "2":
        view_tasks()

    # Delete Task
    elif choice == "3":
        delete_task()
         

    #Clear All Tasks
    elif choice == "4":
        clear_tasks()

    #Update Task
    elif choice == "5":
        update_task()

    #Exit 
    elif choice == "6":
        print("Thank you for using the To-Do List!")
        break         

    else:
        print("Invalid choice. Please try again.")