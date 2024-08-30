# KEYSIGHT Project

# Task Manager CLI

This is a simple command-line interface (CLI) tool for managing tasks. The tool allows users to add, view, complete, and delete tasks. Tasks are stored in a text file (`tasks.txt`), ensuring they persist between sessions.

## Features

- **Add a Task**: Enter a task name and description interactively.
- **View Tasks**: Display all pending tasks.
- **Complete a Task**: Mark a task as completed.
- **Delete a Task**: Remove a task from the list.
- **Persistence**: All tasks are stored in a text file (`tasks.txt`), allowing them to persist between program runs.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AnshumaliSuri/keysight_anshumali.git
   cd keysight_anshumali

2. **Run the script**:
   ```bash
   python task_manager.py

3. **Example usage**:
   --- Task Manager ---
    1. Add a Task
    2. List Tasks
    3. Complete a Task
    4. Delete a Task
    5. Exit

    Enter your choice (1-5): 1
    Enter task name: Buy groceries
    Enter task description: Purchase milk, eggs, and bread.

    Task added successfully.

    Enter your choice (1-5): 2

    Pending Tasks:
    1. Buy groceries: Purchase milk, eggs, and bread.

    Enter your choice (1-5): 3
    Enter the number of the task to complete: 1

    Task completed successfully.
