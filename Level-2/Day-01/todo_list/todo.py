tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks avaialable.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{index + 1}. {task['task']}[{status}]")

def add_task():
    task_name = input("Enter task:")
    tasks.append({"task":task_name, "done":False})
    print("Task Added successfully!")

def remove_task():
    show_tasks()
    task_num = int(input("enter task number to remove:"))

    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Removed:{removed['task']}")

    else:
        print("Invalid task number!")

def mark_done():
    show_tasks
    task_num = int(input("Enter task number completed:"))

    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")


while True:
    print("\n========TO-Do LIST==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Removed Task")
    print("4. Mark Task Done")
    print("5. Exit")

    choice = input("Enter choice:")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("GoodBye!")
        break
    else:
        print("Invalid choice!")
