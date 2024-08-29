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

def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(f"[ ] {description}")
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """View all pending tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nPending Tasks:")
    for idx, task in enumerate(tasks, start=1):
        if task.startswith("[ ]"):
            print(f"{idx}. {task[4:]}")
    print()

def complete_task(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        if task.startswith("[ ]"):
            tasks[task_number - 1] = task.replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            print(f"Task completed: {task[4:]}")
        else:
            print("Task is already completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete a task from the list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task deleted: {task[4:]}")
    else:
        print("Invalid task number.")

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command> [options]")
        print("Commands:")
        print("  add <task_description>  - Add a new task")
        print("  list                    - View all pending tasks")
        print("  complete <task_number>  - Mark a task as completed")
        print("  delete <task_number>    - Delete a task")
        return

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: Task description is required.")
        else:
            description = " ".join(sys.argv[2:])
            add_task(description)
    elif command == 'list':
        list_tasks()
    elif command == 'complete':
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Error: Task number is required.")
        else:
            task_number = int(sys.argv[2])
            complete_task(task_number)
    elif command == 'delete':
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Error: Task number is required.")
        else:
            task_number = int(sys.argv[2])
            delete_task(task_number)
    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, list, complete, delete")

if __name__ == "__main__":
    main()
