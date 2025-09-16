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

        except (KeyboardInterrupt, EOFError):   # try-except for built-in exceptions.
            print(thank_you)
            sys.exit()


def add_book():
    """This function adds the name of the book and its author to the JSON file."""
    book = get_non_emtpy_input("Enter the book's name: ")
    author = get_non_emtpy_input("Enter the author's name: ")

    new_data = {book: author} 

    try:
        # Check if the file already exists.
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}   # File is emtpy or corrupted, reset to emtpy dict.
        else:
            data = {}
        
        # Check to see if the book already exists in the books.json file.
        if book not in data:
            # Update dictionary with new data.
            data.update(new_data)

            # Write back to file (overwrite with updated data)
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            print(f"\nBook '{book}' by {author} succesfully added to {filename}.")

        else:
            print(f"\nBook '{book}' already exists in {filename}.")

    except IOError as e:
        print(f"Error writing to fle '{filename}': {e}.")


def read_book():
    """A function that displays books and authors."""
    try:
        with open(filename, "r") as file:
            loaded_data = json.load(file)
            print(f"The JSON data was successfully loaded from {filename}.\n")
            
            if loaded_data:
                print("Books to read:")
                for book, author in loaded_data.items():
                    print(f"- {book} by {author}")  # Print the book and author prettier!
            else:
                print("There are no books.")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error loading to file '{filename}': {e}.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{filename}': {e}.")


def delete_book():
    """Delete a specific book by searching for its name."""
    # Show the books.
    read_book()
    # Ask for a book to delete.
    book = get_non_emtpy_input("\nEnter the name of the book you want to delete: ")

    try:
        # See if books.json exist.
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}   # File is emtpy or corrupted, reset to emtpy dict.
        else:
            print(f"The file '{filename}' doesn't exist.")
            return  # Exit early.

        if book in data:
            # Delete the book by its name.
            del data[book]
        
            # Update the JSON file with the new data.
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"\nBook {book} succesfully deleted.")
        else:
            print(f"\nBook '{book}' was not found in {filename}.")

    except FileNotFoundError:
        print("\nThere's no books to delete from. Write something first.")
    except IOError as e:
        print(f"\nError loading to file '{filename}': {e}.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}': {e}.")


def show_menu():
    print("""
==== BOOKS-TO-READ ====
1. Add new book
2. See books
3. Delete book
4. Exit
""")


def exit_journal():
    """Gracefully exit the program."""
    print(thank_you)
    sys.exit()


def main():
    """The main function of the program."""
    menu_options = {
        1: add_book,
        2: read_book,
        3: delete_book,
        4: exit_journal,
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
