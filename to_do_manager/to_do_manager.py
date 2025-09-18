import json

import sys

import os


def show_menu():    # The ability to change status will be added.
    print("""
===== TO-DO LIST MENU =====
1. Add Task
2. View Task
3. Delete Task
4. Exit
""")


def get_non_emtpy_input(prompt: str) -> str:
    """Keep asking until user enter non-empty string."""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.\n")

        except (KeyboardInterrupt, EOFError):   # try-except for built-in exceptions. Exit the program.
            print("\nThank you for using TO-DO MANAGER by BelacEr!")
            sys.exit()  # Exit the program.


def load_json_data() -> dict:
    """Load JSON data from file, return emtpy dict if file doesn't exist or is corrupted."""
    try:
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return {}   # File is emtpy or corrupted.
        return {}   # File doesn't exist.
    except IOError as e:
        print(f"Error reading file 'tasks.json': {e}.")
        return {}


def save_json_data(data: dict) -> bool:
    """Save data into JSON file, return True if successful."""
    try:
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    except IOError as e:
        print(f"Error writing to file 'tasks.json': {e}.")
        return False


def add_task():
    """Add a task to the JSON file that includes a try-except statement for built-in exceptions."""
    task = get_non_emtpy_input("\nEnter the task: ")
    status = "Not completed"

    new_data = {task: status}

    data = load_json_data()

    if not task in data:
        # Update dictionary with new data.
        data.update(new_data)

        # Write back to file (overwrite with updated data)
        save_json_data(data)    # Update the JSON data.
        print(f"\n{task} has been added.")

    else:
        print(f"\n{task} already exists.")


def read_tasks():
    """Display the tasks and their statuses from the JSON file."""
    data = load_json_data()

    if data:    # Make sure the file contains data.
        for task, status in data.items():
            print(f"- {task}:  {status}")
    else:
        print("\nThere are no tasks.")


def delete_task():
    """Delete a specific task by searching for its name."""
    tasks = read_tasks()
    data = load_json_data()

    if data:
        # If there are tasks, you will be prompted to select the one you want to delete.
        task = get_non_emtpy_input("\nEnter the name of the task you want to delete: ")
    else:
        # If there are no tasks, you will be redirected back to the menu.
        return

    if task in data:
        # Delete the task by its name.
        del data[task]
        print(f"The task '{task}' was deleted.")

         # Update the JSON file with new data.
        save_json_data(data)
    else:
        print(f"The task {task} was not found in tasks.json")


def exit_program():
    """Gracefully exit the pogram."""
    print("\nThank you for using TO-DO MANAGER by BelacEr!")
    sys.exit()

def main():
    """The main function of the program."""
    menu_options = {
        1: add_task,
        2: read_tasks,
        3: delete_task,
        4: exit_program,
    }
    while True:
        show_menu() # Show the menu of the program.
        try:
            choice = int(input("Choose the option: "))

            selected_function = menu_options.get(choice)

            if selected_function:
                selected_function()
            else:
                print("\nPlease make sure to enter a valid option.")
    
        except ValueError:
            print("\nPlease makse sure to enter a valid number.")

        except (KeyboardInterrupt, EOFError):
            print("\nThank you for using TO-DO MANAGER by BelacEr!")
            sys.exit()  # Exit the program.
