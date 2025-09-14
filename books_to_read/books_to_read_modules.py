import json

import sys

import os

# Global variables.
filename = "books.json"
thank_you = "\nThank you for using books-to-read by BelacEr."

def add_book():
    """Function to add the book name and the author in the JSON file."""
    try:
        # Ask for the book and author name with try-except for built-in exceptions.
        book = input("\nEnter the book name: ").strip()
        author = input("Enter the author name: ").strip()

    except (KeyboardInterrupt, EOFError):
        print(thank_you)
        sys.exit() # Exit the program.

    new_data = {book: author}

    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}   # File is emtpy or corrupted, reset to emtpy dict.
        else:
            data = {}
    
        # Update dictionary with new data.
        data.update(new_data)

        # Write back to file (overwrite with updated data)
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Book '{book}' by {author} succesfully added to {filename}.")
        
    except IOError as e:
        print(f"Error writing to fle '{filename}': {e}")


def read_book():
    try:
        with open(filename, "r") as file:
            loaded_data = json.load(file)
            print(f"JSON data successfully loaded from {filename}.\n")
            
            print("Books to read:")
            for book, author in loaded_data.items():
                print(f"- {book} by {author}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error loading to file {filename}: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{filename}': {e}")


def show_menu():
    print("""
==== BOOKS-TO-READ ====
1. Add new book
2. See books
3. Exit
""")


def exit_journal():
    """Gracefully exit the program."""
    print(thank_you)
    sys.exit()


def main():
    """Main functin of the program."""
    menu_options = {
        1, add_book,
        2, read_book,
        3, exit_journal,
        }

    while True:
        show_menu() # Show the menu of the program.
        try:
            # Ask for a number that will be used in the menu with try-except for built-in exceptions.
            choice = int(input("Choose the option: "))

            selected_function = menu_options.get(choice)

            if selected_function:
                selected_function()
            else:
                print("\nPlease make sure to enter a valid number.")

        except ValueError:
            print("\nPlease make sure to enter a valid number.")
        except (KeyboardInterrupt ,EOFError):
            print(thank_you)
            return  # Exit early.