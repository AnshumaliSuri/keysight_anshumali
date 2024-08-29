import sys
import os

# Path to the file where tasks will be stored
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the tasks.txt file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the tasks.txt file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task():
    """Add a new task to the list interactively."""
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty. Please try again.")
        return

    description = input("Enter task description: ").strip()
    tasks = load_tasks()
    tasks.append(f"[ ] {task_name}: {description}")
    save_tasks(tasks)
    print(f"\nTask added successfully: {task_name}")

def list_tasks():
    """View all tasks, separating pending and completed ones."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nPending Tasks:")
    pending_tasks = [task for task in tasks if task.startswith("[ ]")]
    if pending_tasks:
        for idx, task in enumerate(pending_tasks, start=1):
            print(f"{idx}. {task[4:]}")
    else:
        print("No pending tasks.")

    print("\nCompleted Tasks:")
    completed_tasks = [task for task in tasks if task.startswith("[x]")]
    if completed_tasks:
        for idx, task in enumerate(completed_tasks, start=1):
            print(f"{idx}. {task[4:]}")
    else:
        print("No completed tasks.")

def complete_task():
    """Mark a task as completed interactively."""
    tasks = load_tasks()
    pending_tasks = [task for task in tasks if task.startswith("[ ]")]

    if not pending_tasks:
        print("No pending tasks to complete.")
        return

    print("\nPending Tasks:")
    for idx, task in enumerate(pending_tasks, start=1):
        print(f"{idx}. {task[4:]}")

    try:
        task_number = int(input("\nEnter the number of the task to complete: "))
        if 1 <= task_number <= len(pending_tasks):
            task_idx = tasks.index(pending_tasks[task_number - 1])
            tasks[task_idx] = tasks[task_idx].replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            print(f"Task completed successfully: {pending_tasks[task_number - 1][4:]}")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    """Delete a task interactively."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks to delete.")
        return

    print("\nTasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task[4:]}")

    try:
        task_number = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task deleted successfully: {task[4:]}")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to handle command-line arguments."""
    print("\n--- Task Manager ---")
    print("1. Add a Task")
    print("2. List Tasks")
    print("3. Complete a Task")
    print("4. Delete a Task")
    print("5. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                list_tasks()
            elif choice == 3:
                complete_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
