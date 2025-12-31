# To-Do List Application
# Oasis Infobyte Internship - Python Programming
# Author: Cudos

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
