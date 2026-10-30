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

# -- Decorative Banner and Welcoming --
# Includes string operators + and * to efficiently create the banner
print("╭" + ("═" * 41) + "╮")
print("│" + "Welcome to the Simple Finance Calculator!" + "│")
print("╰" + ("═" * 41) + "╯")

# -- User Onboarding --
# Storing the user's name as a variable after prompted input
user_name = input("Please enter a Username: ")

# -- Prints a Personalized Greeting for the User --
# Used sep="" to attach the exclamation mark to username
print("Greetings, ", user_name, "!", sep="", end="\n\n")

# -- Prompts user for numbers to use in basic calculation --
num_1 = float(input("Please enter your first number: "))
num_2 = float(input("Please enter your second number: "))

# Usage of end= to create a buffer text
print("Please wait for calculations...", end="\n\n")

# -- Basic Arithmetic Calculations --
# All outputs are limited to 2 decimal places using ".2f"
print("Addition Result (Total Balance): $", end="")
print(format(num_1 + num_2, ".2f"))

# Inputs the first and second number into an - operation
print("Subtraction Result (Net Difference): $", end="")
print(format(num_1 - num_2, ".2f"))

# Inputs the first and second number into a * operation
print("Multiplication Result (Compounded): $", end="")
print(format(num_1 * num_2, ".2f"))

# Inputs the first and second number into a / operation, checks for zero
print("Division Result (Dividend): $", end="")
if num_2 == 0:
    print("Cannot divide by 0!")
else:
    print(format(num_1 / num_2, ".2f"))

# Inputs the first and second number into a // operation, checks for zero
print("Floor Division Result (Whole Number): $", end="")
if num_2 == 0:
    print("Cannot divide by 0!")
else:
    print(format(num_1 // num_2, ".2f"))

# Inputs the first and second number into a % operation, checks for zero
print("Modulo Result (Leftover Remainder): $", end="")
if num_2 == 0:
    print("Cannot divide by 0!")
else:
    print(format(num_1 % num_2, ".2f"))

# Inputs the first and second number into a ** operation
print("Exponentiation Result (Exponential): $", end="")
if num_1 > 100 or num_2 > 20:
    print(
        "Assigned values are too large for a float calculation...",
        end="\n\n"
    )
else:
    print(format(num_1 ** num_2, ".2f"), end="\n\n")

# Prints end of task statement
print("Calculation completed, exiting program!")
