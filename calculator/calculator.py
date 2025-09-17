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
        print("Error: Division by zer!")
    return n1 / n2


def mul(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def sqr_root(n1):
    """Calculate the square root of a numer. Returns an error for negative inputs."""
    if n1 < 0:
        print("Error: Cannot calculate square root of negative numbers.")
    return n1 ** 0.5


def exp(n1, n2):
    """Return n1 raised to the power of n2."""
    return n1 ** n2


def show_menu():
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


def main():
    """The main function of the program"""
    while True:
        show_menu()
        try:
            choice = int(input("Choose the option: "))

            if 0 < choice < 6:
                n1 = float(input("\nEnter the first number: "))
                n2 = float(input("Enter the second number: "))
                if choice == 1:
                    print(f"\n{n1} + {n2} = {add(n1, n2)}")
                elif choice == 2:
                    print(f"\n{n1} - {n2} = {sub(n1, n2)}")
                elif choice == 3:
                    print(f"\n{n1} * {n2} = {mul(n1, n2)}")
                elif choice == 4:
                    print(f"\n{n1} / {n2} = {div(n1, n2)}")
                elif choice == 5:
                    print(f"\n{n1} ** {n2} = {exp(n1, n2)}")

            elif choice == 6:
                n1 = float(input("\nEnter the number: "))
                print(f"\n√{n1} = {sqr_root(n1)}")

            elif choice == 7:
                exit_calculator()

            else:
                print("\nPlease make sure to enter a valid number (1-7).")

        except ValueError:
            print("\nPlease make sure to enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit()
