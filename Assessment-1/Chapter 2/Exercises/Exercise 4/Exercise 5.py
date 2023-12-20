#Exercise 5: Calculator
#Develop a GUI to perform basic arithmetic operations like addition, subtraction, multiplication, Division, and modulo division using buttons. You can ask the user to enter the values in entry widget and select the operation to be performed.


import tkinter as tk

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation.get() == "Addition":
            result = num1 + num2
        elif operation.get() == "Subtraction":
            result = num1 - num2
        elif operation.get() == "Multiplication":
            result = num1 * num2
        elif operation.get() == "Division":
            result = num1 / num2
        elif operation.get() == "Modulo":
            result = num1 % num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Arithmetic Calculator")

# Entry widgets for user input with default text
default_text_color = "#aaaaaa"  # Light gray
entry_num1 = tk.Entry(window, width=15, fg=default_text_color)
entry_num1.insert(0, "1st entry")
entry_num2 = tk.Entry(window, width=15, fg=default_text_color)
entry_num2.insert(0, "2nd entry")

# Bind events to remove default text when entry is clicked
def on_entry_click(event):
    if entry_num1.get() == "1st entry":
        entry_num1.delete(0, tk.END)
        entry_num1.config(fg="black")

def on_entry2_click(event):
    if entry_num2.get() == "2nd entry":
        entry_num2.delete(0, tk.END)
        entry_num2.config(fg="black")

entry_num1.bind("<FocusIn>", on_entry_click)
entry_num2.bind("<FocusIn>", on_entry2_click)

# Label and entry widget for operation selection
operation_label = tk.Label(window, text="Select Operation:")
operation = tk.StringVar()
operation.set("Addition")
operation_menu = tk.OptionMenu(window, operation, "Addition", "Subtraction", "Multiplication", "Division", "Modulo")

# Button to perform the operation
calculate_button = tk.Button(window, text="Calculate", command=perform_operation)

# Label to display the result
result_label = tk.Label(window, text="Result: ")

# Grid layout
entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10)
operation_label.grid(row=1, column=0, padx=10, pady=10)
operation_menu.grid(row=1, column=1, padx=10, pady=10)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
