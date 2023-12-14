#Exercise 12: Area Function
#Code a program to display a menu on the screen that asks if the user wants to

#1: Calculate the area of a square
#2: Calculate the area of a circle
#3: Calculate the area of a triangle 
#Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.   

#Importing Math Library
import math

def calculate_square_area():
    # Function to calculate the area of a square
    side_length = float(input("Enter the side length of the square: "))
    area = side_length ** 2
    print(f"The area of the square is: {area}")

def calculate_circle_area():
    # Function to calculate the area of a circle
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area}")

def calculate_triangle_area():
    # Function to calculate the area of a triangle
    base_length = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base_length * height
    print(f"The area of the triangle is: {area}")

# Display menu
while True:
    print("\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("0: Exit")

    # Get user choice
    choice = input("Enter your choice (0-3): ")

    # Execute the corresponding function based on user choice
    if choice == "1":
        calculate_square_area()
    elif choice == "2":
        calculate_circle_area()
    elif choice == "3":
        calculate_triangle_area()
    elif choice == "0":
        # Exit the program if the user chooses 0
        print("Exiting the program. Goodbye!")
        break
    else:
        # Handle invalid input
        print("Invalid choice. Please enter a number between 0 and 3.")

#The End.. 