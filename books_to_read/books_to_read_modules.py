import json

import sys

import os

# Global variables.
filename = "books.json"
thank_you = "\nThank you for using books-to-read by BelacEr!"

def get_non_emtpy_input(prompt: str) -> str:
    """Keep asking until user enter non-emtpy string."""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.\n")
        except (KeyboardInterrupt, EOFError):
            print(thank_you)
            sys.exit()


def add_book():
    """This function adds the book name and author to the JSON file."""
    book = get_non_emtpy_input("Enter the book's name: ")
    author = get_non_emtpy_input("Enter the author's name: ")

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

        print(f"\nBook '{book}' by {author} succesfully added to {filename}.")
        
    except IOError as e:
        print(f"Error writing to fle '{filename}': {e}")


def read_book():
    """A function that shows books and their author."""
    try:
        with open(filename, "r") as file:
            loaded_data = json.load(file)
            print(f"The JSON data was successfully loaded from {filename}.\n")
            
            print("Books to read:")
            for book, author in loaded_data.items():
                print(f"- {book} by {author}")  # Print the book and author prettier!

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error loading to file '{filename}': {e}.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{filename}': {e}.")


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
    """The main function of the program"""
    menu_options = {
        1: add_book,
        2: read_book,
        3: exit_journal,
        }

    while True:
        show_menu() # Show the menu of the program.
        try:
            # Ask for a number that will be used in the menu with the try-except statement for built-in exceptions.
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