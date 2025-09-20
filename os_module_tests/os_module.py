import os
import sys


def show_cwd():
    """Function to show the Current Working Directory."""
    cwd = os.getcwd()
    print(f"\nCurrent working directory: {cwd}")


def change_cwd():
    """Function to change the Current Working Directory."""
    print("Current working directory before:")
    print(os.getcwd(), end="\n\n")
    os.chdir("..")
    print("Current working directory after:")
    print(os.getcwd(), end="\n\n")


def get_non_empty_input(prompt):
    """Prompt user until a non-empty input is entered (q to cancel)."""
    while True:
        try:
            value = input(f"{prompt} (press 'q' to cancel): ").strip()
            if value.lower() == "q":
                return None
            if value:
                return value
            print("Input cannot be empty. Please try again.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit()


def get_integer_input(prompt):
    """Function that only accepts integers."""
    while True:
        try:
            value = input(f"{prompt} (press 'q' to cancel): ").strip()
            if value.lower() == "q":
                return None
            return int(value)
        except ValueError:
            print("\nPlease make sure to enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit()


def create_directory(parent_dir, dirname):
    """Function that creates a directory inside a parent directory."""
    try:
        if parent_dir.lower() == "c":  # Use current working dir
            parent_dir = os.getcwd()

        path = os.path.join(parent_dir, dirname)
        os.mkdir(path)
        print(f"\nThe directory '{dirname}' was created in '{parent_dir}'.")
    except FileExistsError:
        print(f"\nThe directory '{dirname}' already exists in '{parent_dir}'.")
    except FileNotFoundError:
        print(f"\nThe parent directory '{parent_dir}' does not exist.")
    except PermissionError:
        print(f"\nPermission denied: cannot create '{dirname}' in '{parent_dir}'.")


def listing_out(path):
    """Function that lists out files and directories."""
    try:
        if path.lower() == "c":  # Use current working dir
            path = os.getcwd()

        dir_list = os.listdir(path)
        print(f"\nFiles and directories in '{path}':")
        for item in dir_list:
            print(f"  - {item}")
    except FileNotFoundError:
        print(f"\nThe directory '{path}' does not exist.")


def delete_file(location, file):
    """Function that deletes files."""
    try:
        if location.lower() == "c":
            location = os.getcwd()

        path = os.path.join(location, file)
        os.remove(path)
        print(f"\nThe file '{file}' was successfully deleted.")
    except IsADirectoryError:
        print(f"\n'{file}' is a directory. Use option 6 to delete directories.")
    except FileNotFoundError:
        print(f"\nThe file '{file}' does not exist in '{location}'.")
    except PermissionError:
        print(f"\nPermission denied: cannot delete '{file}'.")


def delete_directory(location, dirname):
    """Function that deletes directories."""
    try:
        if location.lower() == "c":
            location = os.getcwd()

        path = os.path.join(location, dirname)
        os.rmdir(path)  # Only works if the directory is empty
        print(f"\nThe directory '{dirname}' was successfully deleted.")
    except FileNotFoundError:
        print(f"\nThe directory '{dirname}' does not exist in '{location}'.")
    except OSError:
        print(
            f"\nThe directory '{dirname}' could not be deleted. "
            "Make sure it is empty before deleting."
        )
    except PermissionError:
        print(f"\nPermission denied: cannot delete '{dirname}'.")


def exit_program():
    """Function to gracefully exit the program."""
    print("\nGoodbye!")
    sys.exit()


def show_menu():
    """Function to show the menu of the program."""
    print("""
    1. Show the Current Working Directory
    2. Change the Current Working Directory (go up one level)
    3. Create a directory
    4. List files and directories 
    5. Delete file
    6. Delete directory
    7. Exit
    """)


def main():
    """Main function of the program."""
    while True:
        show_menu()
        choice = get_integer_input("\nChoose your option: ")

        if choice is None:  # User pressed q
            continue

        if choice == 1:
            show_cwd()
        elif choice == 2:
            change_cwd()
        elif choice == 3:
            parent_dir = get_non_empty_input(
                "Enter the path of the parent directory ('c' for current directory)"
            )
            if parent_dir is None:
                continue

            dirname = get_non_empty_input(
                "Enter the name of the directory you want to create"
            )
            if dirname is None:
                continue

            create_directory(parent_dir, dirname)
        elif choice == 4:
            path = get_non_empty_input(
                "Enter the path of the directory you want to list ('c' for current directory)"
            )
            if path is None:
                continue
            listing_out(path)
        elif choice == 5:
            location = get_non_empty_input(
                "Enter the path of the file you want to delete ('c' for current directory)"
            )
            if location is None:
                continue

            file = get_non_empty_input("Enter the name of the file you want to delete")
            if file is None:
                continue

            delete_file(location, file)
        elif choice == 6:
            location = get_non_empty_input(
                "Enter the path of the directory you want to delete ('c' for current directory)"
            )
            if location is None:
                continue

            dirname = get_non_empty_input(
                "Enter the name of the directory you want to delete"
            )
            if dirname is None:
                continue

            delete_directory(location, dirname)
        elif choice == 7:
            exit_program()
        else:
            print("\nInvalid option. Please choose a valid number (1–7).")