#Exercise 4: Shapes 
#Develop a GUI using Tkinter to calculate the area of Shapes. Create a parent class called Shape. This should have the following methods inputSides() – Ask the user to enter the sides of the shape. Now create subclasses for a circle, rectangle, and triangle. These should include an appropriate  area() method that will use the side values from the shape class.    



import tkinter as tk
from math import pi


class Shape:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Shape Area Calculator")

        # Create widgets for shape selection
        self.label = tk.Label(master, text="Select a Shape:")
        self.label.pack()

        self.shape_var = tk.StringVar()
        self.shape_var.set("Circle")

        self.shape_option_menu = tk.OptionMenu(master, self.shape_var, "Circle", "Rectangle", "Triangle")
        self.shape_option_menu.pack()

        # Create widgets for entering side(s)
        self.side_label = tk.Label(master, text="Enter Side(s):")
        self.side_label.pack()

        self.side_entry = tk.Entry(master)
        self.side_entry.pack()

        # Create a button to calculate area
        self.calculate_button = tk.Button(master, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.pack()

        # Display the result
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_area(self):
        # Retrieve user input and calculate area based on selected shape
        shape_type = self.shape_var.get()
        side_input = self.side_entry.get()

        try:
            sides = [float(side) for side in side_input.split(",")]
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numeric values.")
            return

        if shape_type == "Circle":
            result = Circle(sides).area()
        elif shape_type == "Rectangle":
            result = Rectangle(sides).area()
        elif shape_type == "Triangle":
            result = Triangle(sides).area()
        else:
            result = "Invalid shape type."

        self.result_label.config(text=f"Area: {result}")


class Circle:
    def __init__(self, sides):
        # Initialize the Circle with its specific attributes
        if len(sides) == 1:
            self.radius = sides[0]
        else:
            raise ValueError("Circle requires exactly one side (radius).")

    def area(self):
        # Calculate area of a circle based on the radius
        return pi * self.radius ** 2


class Rectangle:
    def __init__(self, sides):
        # Initialize the Rectangle with its specific attributes
        if len(sides) == 2:
            self.length, self.width = sides
        else:
            raise ValueError("Rectangle requires exactly two sides (length and width).")

    def area(self):
        # Calculate area of a rectangle based on length and width
        return self.length * self.width


class Triangle:
    def __init__(self, sides):
        # Initialize the Triangle with its specific attributes
        if len(sides) == 3:
            self.a, self.b, self.c = sides
        else:
            raise ValueError("Triangle requires exactly three sides.")

    def area(self):
        # Calculate area of a triangle based on Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    
    # Create an instance of the Shape class to run the application
    app = Shape(root)
    
    # Start the Tkinter event loop
    root.mainloop()
