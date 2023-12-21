#Exercise 3: Area Function
#Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes, including circles, squares, and rectangles. The application should utilize a tabbed interface to organize the calculations for each shape. Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.

import tkinter as tk
from tkinter import ttk
import math

class AreaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)

        # Add tabs for different shapes
        self.circle_tab = ttk.Frame(self.notebook)
        self.square_tab = ttk.Frame(self.notebook)
        self.rectangle_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.circle_tab, text="Circle")
        self.notebook.add(self.square_tab, text="Square")
        self.notebook.add(self.rectangle_tab, text="Rectangle")

        self.notebook.pack(padx=10, pady=10)

        # Circle tab
        self.radius_label = tk.Label(self.circle_tab, text="Radius:")
        self.radius_entry = tk.Entry(self.circle_tab)
        self.calculate_circle_button = tk.Button(self.circle_tab, text="Calculate", command=self.calculate_circle)
        self.result_label_circle = tk.Label(self.circle_tab, text="Area: ")

        self.radius_label.grid(row=0, column=0, padx=5, pady=5)
        self.radius_entry.grid(row=0, column=1, padx=5, pady=5)
        self.calculate_circle_button.grid(row=1, column=0, columnspan=2, pady=5)
        self.result_label_circle.grid(row=2, column=0, columnspan=2, pady=5)

        # Square tab
        self.side_label = tk.Label(self.square_tab, text="Side:")
        self.side_entry = tk.Entry(self.square_tab)
        self.calculate_square_button = tk.Button(self.square_tab, text="Calculate", command=self.calculate_square)
        self.result_label_square = tk.Label(self.square_tab, text="Area: ")

        self.side_label.grid(row=0, column=0, padx=5, pady=5)
        self.side_entry.grid(row=0, column=1, padx=5, pady=5)
        self.calculate_square_button.grid(row=1, column=0, columnspan=2, pady=5)
        self.result_label_square.grid(row=2, column=0, columnspan=2, pady=5)

        # Rectangle tab
        self.length_label = tk.Label(self.rectangle_tab, text="Length:")
        self.width_label = tk.Label(self.rectangle_tab, text="Width:")
        self.length_entry = tk.Entry(self.rectangle_tab)
        self.width_entry = tk.Entry(self.rectangle_tab)
        self.calculate_rectangle_button = tk.Button(self.rectangle_tab, text="Calculate", command=self.calculate_rectangle)
        self.result_label_rectangle = tk.Label(self.rectangle_tab, text="Area: ")

        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        self.width_label.grid(row=1, column=0, padx=5, pady=5)
        self.width_entry.grid(row=1, column=1, padx=5, pady=5)
        self.calculate_rectangle_button.grid(row=2, column=0, columnspan=2, pady=5)
        self.result_label_rectangle.grid(row=3, column=0, columnspan=2, pady=5)

    def calculate_circle(self):
        try:
            radius = float(self.radius_entry.get())
            area = math.pi * radius ** 2
            self.result_label_circle.config(text=f"Area: {area:.2f}")
        except ValueError:
            self.result_label_circle.config(text="Invalid input")

    def calculate_square(self):
        try:
            side = float(self.side_entry.get())
            area = side ** 2
            self.result_label_square.config(text=f"Area: {area:.2f}")
        except ValueError:
            self.result_label_square.config(text="Invalid input")

    def calculate_rectangle(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            area = length * width
            self.result_label_rectangle.config(text=f"Area: {area:.2f}")
        except ValueError:
            self.result_label_rectangle.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()
# The End...