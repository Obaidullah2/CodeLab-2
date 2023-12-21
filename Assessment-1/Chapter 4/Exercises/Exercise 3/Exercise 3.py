#Exercise 3: Reading to a List 
#The file numbers.txt has a list of 100 integer numbers each on a newline. Create a python program that puts this data into a list, then output the values in integer format.


import tkinter as tk
import os

# Set up the main window
root = tk.Tk()
root.title("Reading")
root.geometry("400x200")

def show_numbers():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "numbers.txt")

    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    result_var.set(f"List of integers: {numbers}")

# Create and pack widgets
titlelabel = tk.Label(root, text="Click the button to display the list of integers.")
titlelabel.pack(pady=10)

readbtn = tk.Button(root, text="Read File", command=show_numbers, bg="#aeafef")
readbtn.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, wraplength=380)
result_label.pack(pady=10)

# Start the main loop
root.mainloop()