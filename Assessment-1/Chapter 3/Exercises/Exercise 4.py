#Exercise 4: Draw Shape
#Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and draw the shape using canvas.  

#Extension:Ask the user to input the coordinate values of the selected option.

import tkinter as tk
from tkinter import simpledialog

class ShapeDrawer:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Shape Drawer")

        # Create a canvas for drawing shapes
        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Variable to store the selected shape
        self.shape_var = tk.StringVar()
        self.shape_var.set("oval")

        # Label and option menu for selecting the shape
        shape_label = tk.Label(master, text="Select Shape:")
        shape_label.pack()

        shape_options = ["oval", "rectangle", "square", "triangle"]
        shape_menu = tk.OptionMenu(master, self.shape_var, *shape_options)
        shape_menu.pack(pady=5)

        # Button to draw the selected shape
        draw_button = tk.Button(master, text="Draw Shape", command=self.draw_shape)
        draw_button.pack(pady=10)

    def draw_shape(self):
        # Get the selected shape from the variable
        shape = self.shape_var.get()

        # Call the appropriate draw function based on the selected shape
        if shape == "oval":
            self.draw_oval()
        elif shape == "rectangle":
            self.draw_rectangle()
        elif shape == "square":
            self.draw_square()
        elif shape == "triangle":
            self.draw_triangle()

    def get_coordinates(self):
        # Ask the user to input coordinates using a simple dialog
        coordinates = simpledialog.askstring("Input", "Enter coordinates (x1, y1, x2, y2):")
        
        # If the user provided coordinates, convert them to a tuple of integers
        if coordinates:
            coordinates = tuple(map(int, coordinates.split(',')))
            return coordinates
        else:
            return None

    def draw_oval(self):
        # Get coordinates from the user and draw an oval on the canvas
        coordinates = self.get_coordinates()
        if coordinates:
            self.canvas.create_oval(coordinates, outline="black")

    def draw_rectangle(self):
        # Get coordinates from the user and draw a rectangle on the canvas
        coordinates = self.get_coordinates()
        if coordinates:
            self.canvas.create_rectangle(coordinates, outline="black")

    def draw_square(self):
        # Get coordinates from the user and draw a square on the canvas
        coordinates = self.get_coordinates()
        if coordinates:
            x1, y1, x2, y2 = coordinates
            side_length = min(abs(x2 - x1), abs(y2 - y1))
            self.canvas.create_rectangle(x1, y1, x1 + side_length, y1 + side_length, outline="black")

    def draw_triangle(self):
        # Get coordinates from the user and draw a triangle on the canvas
        coordinates = self.get_coordinates()
        if coordinates:
            x1, y1, x2, y2 = coordinates
            x3 = x1 + (x2 - x1) / 2
            y3 = y1
            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black")

if __name__ == "__main__":
    # Create the main Tkinter window and run the application
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop()
