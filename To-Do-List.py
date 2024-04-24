import datetime

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False
        self.time = datetime.datetime.now()

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f'''{self.description} ({status})
                Priority of this task is {self.priority}
                Created at: {self.time}'''

    def complete(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"This task \"{task}\" has been removed")
        else:
            print("Task not found!")

    def complete_task(self, task):
        if task in self.tasks:
            task.complete()
            print("Task has been completed")
        else:
            print("Task not found!")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(f"\n{task}")
        else:
            print("No tasks found. Add some tasks and try again.")

    def sort_tasks_by_priority(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        print("Tasks sorted by priority.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMy To-Do List :)")
        print("1 for Add task")
        print("2 for Remove task")
        print("3 for Complete task")
        print("4 for Display tasks")
        print("5 for Sort tasks by priority")
        print("6 for Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task_description = input("Enter your task description: ")
            task_priority = input("Enter the task priority (low, medium, high): ")
            task = Task(task_description, task_priority)
            todo_list.add_task(task)

        elif choice == "2":
            task_description = input("Enter a task description to remove: ")
            task = next((t for t in todo_list.tasks if t.description == task_description), None)

            if task:
                todo_list.remove_task(task)
            else:
                print("Task not found.")

        elif choice == "3":
            task_description = input("Enter the description to complete: ")
            task = next((t for t in todo_list.tasks if t.description == task_description), None)

            if task:
                todo_list.complete_task(task)
            else:
                print("Task not found.")

        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            todo_list.sort_tasks_by_priority()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a choice from 1-6.")
            continue

try:
    main()

except Exception as e:
    print(f"An error occurred: {e}")
