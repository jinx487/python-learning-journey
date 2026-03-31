# Python To_do_list_app 

tasks = []

def add_tasks():
    while True:
        task = input("Enter a task to_do: ")
        tasks.append({"task": task, "completed": False})

        again = input("Do you want to add another task? (Y/N): ").upper()

        if again != "Y":
            break

def view_tasks():
    if not tasks:
        print("No tasks available")
        return
    
    print("\nYour Task: ")

    for i, task in enumerate(tasks):
        status = "X" if task["completed"] else " "
        print(f"{i + 1}. {task['task']} [{status}]")

def mark_complete():
    if not tasks:
        print("No available tasks")
        return
    

    view_tasks()

    choice = input("Enter a choice to mark task as completed: ")

    if not choice.isdigit():
        print("Invalid input")
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return
    
    tasks[index]["completed"] = True
    print("Task marked as complete ✅")

def delete_tasks():
    if not tasks:
        print("No tasks available")
        return
    
    view_tasks()

    choice = input("Enter a task to delete: ")

    if not choice.isdigit():
        print("Invalid input")
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return
    
    removed = tasks.pop(index)
    print(f"Deleted tasks: {removed['task']}")

def main():

    is_running = True

    print("*****************")
    print("To_do list App")
    print("1.Add task")
    print("2.View task")
    print("3.Mark complete")
    print("4.Delete task")
    print("5.Exit")

    while is_running:

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_tasks()
        elif choice == "5":
            is_running = False
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()