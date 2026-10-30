# Name: Tonmoy Kar
# Description: A Simple Python Calculator for Basic Financial Arithmetic
# Sources:
# - https://peps.python.org/pep-0008/#comments
# - https://peps.python.org/pep-0008/#blank-lines
# - https://peps.python.org/pep-0008/#maximum-line-length
# - https://peps.python.org/pep-0008/#method-names-and-instance-variables
# - https://peps.python.org/pep-0008/
# - https://bandit.readthedocs.io/en/latest/
# - geeksforgeeks.org/python/difference-between-end-and-sep-in-python/
# - https://www.w3schools.com/python/python_if_elif.asp
# - https://www.learnpython.org/en/Conditions
# - https://greenteapress.com/wp/think-python-2e/
# - https://www.learnpython.org/en/Functions
# - https://www.w3schools.com/python/ref_func_range.asp
# - https://www.learnpython.org/en/Loops
# - https://www.learnpython.org/en/Exception_Handling


# -- Function Definitions --
def add_funds(val_1, val_2):
    total = val_1 + val_2
    return total


def subtract_funds(val_1, val_2):
    difference = val_1 - val_2
    return difference


def multiply_funds(val_1, val_2):
    compounded = val_1 * val_2
    return compounded


def divide_funds(val_1, val_2):
    dividend = val_1 / val_2
    return dividend


def floor_divide_funds(val_1, val_2):
    whole_number = val_1 // val_2
    return whole_number


def modulo_funds(val_1, val_2):
    leftover = val_1 % val_2
    return leftover


def exponent_funds(val_1, val_2):
    exponential = val_1 ** val_2
    return exponential


# Start loop to rerun calculator, with proper check
run_again = "yes"

while run_again == "yes":

    # -- Decorative Banner and Welcoming --
    # Includes string operators + and * to efficiently create the banner
    print("╭" + ("═" * 41) + "╮")
    print("│" + "Welcome to the Simple Finance Calculator!" + "│")
    print("╰" + ("═" * 41) + "╯")

    # -- User Onboarding --
    # Storing the user's name as a variable after prompted input
    user_name = input("Please enter a Username: ")

    # Shortcut Operator used to add a title to the username
    user_name += " [Account Holder]"

    # -- Prints a Personalized Greeting for the User --
    # Used sep="" to attach the exclamation mark to username
    print("Greetings, ", user_name, "!", sep="", end="\n\n")

    # -- Calculation Menu System --
    # Using if-elif-else in a option choice menu
    # Option 1 is the original Sprint 1 Calc
    # Option 2 is a 3 Year forecast calculator
    print("Please choose an option: ")
    print("1. Simple Financial Calculator")
    print("2. 3 Year Financial Planner Calculator")
    menu_choice = input("Select Choice (1/2): ")

    # if-elif-else loop to control choosing between the two calculators/exit
    if menu_choice == "1":
        # Prompts user for numbers to use in the Simple Calculator
        num_1 = float(input("Please enter your first number: "))
        num_2 = float(input("Please enter your second number: "))

        # Usage of end= to create a buffer text
        print("Please wait for calculations...", end="\n\n")

        # -- Basic Arithmetic Calculations --
        # All outputs are limited to 2 decimal places using ".2f"
        print("Addition Result (Total Balance): $", end="")
        print(format(add_funds(num_1, num_2), ".2f"))

        # Inputs the first and second number into an - operation
        print("Subtraction Result (Net Difference): $", end="")
        print(format(subtract_funds(num_1, num_2), ".2f"))

        # Inputs the first and second number into a * operation
        print("Multiplication Result (Compounded): $", end="")
        print(format(multiply_funds(num_1, num_2), ".2f"))

        # Inputs the first and second number into a / operation, checks for zero
        print("Division Result (Dividend): $", end="")
        if num_2 == 0:
            print("Cannot divide by 0!")
        else:
            print(format(divide_funds(num_1, num_2), ".2f"))

        # Inputs the first and second number into a // operation, checks for zero
        print("Floor Division Result (Whole Number): $", end="")
        if num_2 == 0:
            print("Cannot divide by 0!")
        else:
            print(format(floor_divide_funds(num_1, num_2), ".2f"))

        # Inputs the first and second number into a % operation, checks for zero
        print("Modulo Result (Leftover Remainder): $", end="")
        if num_2 == 0:
            print("Cannot divide by 0!")
        else:
            print(format(modulo_funds(num_1, num_2), ".2f"))

        # Inputs the first and second number into a ** operation
        # Check for valid input
        # Outputs in scientific notation for max value
        print("Exponentiation Result (Exponential): $", end="")
        if num_1 > 0 and num_2 != 0:
            print(format(exponent_funds(num_1, num_2), ".2e"), end="\n\n")
        else:
            print("Invalid base or exponent values entered.", end="\n\n")

    elif menu_choice == "2":
        print("\n--- 3 Year Financial Planner Calculator ---")
        starting_balance = float(input("Please enter your starting balance: "))
        annual_deposit = float(input("Please enter your annual deposit: "))

        current_balance = starting_balance

        for forecast_year in range(1, 4):
            current_balance += annual_deposit
            print("Year ", forecast_year, " Projected Balance: $",
                  format(current_balance, ".2f"), sep="")
        print()

    else:
        print("Invalid choice selected. Skipping to the end.\n")

    # Recalling the start of the Restart Calculator Loop
    run_again = input("Restart Calculator? (yes/no): ")

    # While not loop that checks for valid input
    while not (run_again == "yes" or run_again == "no"):
        print("Invalid response. Please type yes or no.")
        run_again = input("Restart Calculator? (yes/no): ")

# Prints end of task statement
print("Calculation completed, exiting program!")