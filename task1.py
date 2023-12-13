import os
import json
from datetime import datetime
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['date']}")
def add_task(tasks, title):
    new_task = {"title": title, "date": str(datetime.now())}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")
def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully!")
    else:
        print("Invalid task index.")
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the task number to remove: "))
            remove_task(tasks, index)
        elif choice == "4":
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
