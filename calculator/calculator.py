import sys

def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


def sub(n1, n2):
    """Return the difference between two numbers (n1 - n2)."""
    return n1 - n2


def div(n1, n2):
    """Divide n1 by n2. Returns an error message if division by zero is attempted."""
    if n2 == 0:
        print("Error: Division by zero!")
        return None
    return n1 / n2


def mul(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def sqr_root(n1):
    """Calculate the square root of a numer. Returns an error for negative inputs."""
    if n1 < 0:
        print("Error: Cannot calculate square root of negative numbers.")
        return None
    return n1 ** 0.5


def exp(n1, n2):
    """Return n1 raised to the power of n2."""
    return n1 ** n2


def show_menu():
    """Display the calculator menu options."""
    print(""" 
===== CALCULATOR-CLI =====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponentiation
6. Square root
7. Exit
    """)


def exit_calculator():
    """Gracefully exit the program."""
    print("Goodbye!")
    sys.exit()


def format_numbers(num):
    """Format numbers to display as integers when they're whole numbers."""
    if isinstance(num, (int, float)) and num == int(num):
        return int(num)
    return num


def get_number_input(prompt):
    """Get a valid number from input from the user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nPlease enter a valid number.")


def main():
    """The main function of the program."""
    while True:
        show_menu()
        try:
            choice = int(input("Choose the option: "))

            if 1 <= choice <= 5:
                n1 = float(get_number_input("\nEnter the first number: "))
                n2 = float(get_number_input("Enter the second number: "))

                if choice == 1:     # Addition.
                    result = add(n1, n2)
                    print(f"\n{format_numbers(n1)} + {format_numbers(n2)} = {format_numbers(result)}")

                elif choice == 2:   # Subtraction.
                    result = sub(n1, n2)
                    print(f"\n{format_numbers(n1)} - {format_numbers(n2)} = {format_numbers(result)}")

                elif choice == 3:  # Multiplication.
                    result = mul(n1, n2)
                    print(f"\n{format_numbers(n1)} × {format_numbers(n2)} = {format_numbers(result)}")

                elif choice == 4:   # Division.
                    result = div(n1, n2)
                    print(f"\n{format_numbers(n1)} ÷ {format_numbers(n2)} = {format_numbers(result)}")

                elif choice == 5:   # Exponentiation.
                    result = exp(n1, n2)
                    print(f"\n{format_numbers(n1)} ^ {format_numbers(n2)} = {format_numbers(result)}")


            elif choice == 6:       # Square rot.
                n1 = float(get_number_input("\nEnter the number: "))
                result = sqr_root(n1)
                print(f"\n√{format_numbers(n1)} = {format_numbers(result)}")

            elif choice == 7:
                exit_calculator()

            else:
                print("\nPlease make sure to enter a valid number (1-7).")

        except ValueError:
            print("\nPlease make sure to enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit()