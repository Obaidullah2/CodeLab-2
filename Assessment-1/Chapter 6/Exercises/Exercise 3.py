#Exercise 3: Calculator☑️
#Write a program that will display the following calculator menu

#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Modulus
#6. Check greater number
#The program will prompt the user to choose the operation choice (from 1 to 6). Then it asks the user to input values for the calculation. The program outputs the results of the calculation.Use operator module functions

#Extension Problem (Bonus):Allow the user to keep entering values until they enter Q to quit.
#Handle incorrect input

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    return x % y

def check_greater(x, y):
    return "The greater number is: {}".format(max(x, y))

def get_user_input():
    while True:
        try:
            # Prompt user for operation choice
            choice = input("Choose an operation (1-6) or Q to quit: ")

            # Check if the user wants to quit
            if choice.lower() == 'q':
                break

            # Convert the choice to an integer
            choice = int(choice)

            # Check if the choice is within the valid range
            if 1 <= choice <= 6:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
                perform_operation(choice, x, y)
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            # Handle invalid input (non-numeric)
            print("Invalid input. Please enter a valid number.")

def perform_operation(choice, x, y):
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: modulus,
        6: check_greater,
    }

    # Perform the selected operation
    result = operations[choice](x, y)

    # Display the result
    print("Result: {}".format(result))

if __name__ == "__main__":
    get_user_input()
