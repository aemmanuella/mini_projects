# A to do list where users can add, view and delete tasks
tasks = []

print("Welcome to the To-Do List CLI app")

while True:
    print("\nMenu: \n1. Add task \n2. View Tasks \n3. Delete Task \n4. Mark as Done \n5. Exit")
    question = input("\nEnter number from menu: ")

    if question == "1":
        add_task = input("Enter new task: ")
        tasks.append({"task": add_task, "done": False})
        print("Task Successfully added.")
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {task['task']} {status}")
    elif question == "2":
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {task['task']} {status}")
    elif question == "3":
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {task['task']} {status}")
        try:
            delete_task = int(input("Select the number of task you want to delete: "))
            tasks.pop(delete_task - 1)
            print("Task has been deleted")
        except (ValueError, IndexError):
            print("\nInvalid task number")

        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {task['task']} {status}")
    elif question == "4":
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {task['task']} {status}")
        try:
            task_done = int(input("Enter number of task you want to mark as done: "))
            tasks[task_done - 1]["done"] = True
        except (ValueError, IndexError):
            print("\nInvalid task number")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {task['task']} {status}")
    elif question == "5":
        break
    else:
        print("Incorrect input entered.")

