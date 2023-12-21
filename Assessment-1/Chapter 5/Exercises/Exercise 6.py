#Exercise 6: Arithmetic Operation 
#Develop a GUI to perform Arithmetic Operations.

#Create a class ArithmeticOperations with the following
#a result variable to store the result after calculation
#a function Calculate() - To perform an arithmetic operation selected by the user.
#You can use Combobox to provide users with options to perform selected arithmetic operations and entry widgets for the values.

import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("Arithmetic Operations")

        # Variables for user input and result
        self.result = tk.StringVar()
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()

        # Entry widgets for user input
        self.num1_entry = ttk.Entry(root, textvariable=self.num1)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_entry = ttk.Entry(root, textvariable=self.num2)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        # Labels for user guidance
        ttk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)

        # Combobox for selecting operation
        self.operation_var = tk.StringVar()
        operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
        self.operation_combobox = ttk.Combobox(root, values=operations, textvariable=self.operation_var)
        self.operation_combobox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.operation_combobox.set(operations[0])

        # Readonly entry widget to display the result
        ttk.Entry(root, textvariable=self.result, state='readonly').grid(row=3, column=1, padx=10, pady=10)

        # Button to trigger the calculation
        ttk.Button(root, text="Calculate", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            # Get user input and selected operation
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            operation = self.operation_var.get()

            # Perform the selected operation and update the result
            if operation == 'Addition':
                self.result.set(num1 + num2)
            elif operation == 'Subtraction':
                self.result.set(num1 - num2)
            elif operation == 'Multiplication':
                self.result.set(num1 * num2)
            elif operation == 'Division':
                if num2 != 0:
                    self.result.set(num1 / num2)
                else:
                    self.result.set("Cannot divide by zero")
        except ValueError:
            # Handle invalid input (non-numeric input)
            self.result.set("Invalid input")


if __name__ == "__main__":
    # Create the main Tkinter window and the ArithmeticOperations instance
    root = tk.Tk()
    app = ArithmeticOperations(root)

    # Start the Tkinter event loop
    root.mainloop()
