#Exercise 1: User information 
#Develop a GUI App to create a file called bio.txt and write the following information to the file asking user to enter the values: Name Age Hometown Each piece of data should be on a new line Once the data has been written to the file, read the data from the file and output the data.    


import tkinter as tk
from tkinter import messagebox

class BioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bio App")

        # Create and set up GUI elements
        self.label_name = tk.Label(root, text="Name:")
        self.label_age = tk.Label(root, text="Age:")
        self.label_hometown = tk.Label(root, text="Hometown:")

        self.entry_name = tk.Entry(root)
        self.entry_age = tk.Entry(root)
        self.entry_hometown = tk.Entry(root)

        self.button_submit = tk.Button(root, text="Submit", command=self.submit_data)
        self.button_display = tk.Button(root, text="Display Data", command=self.display_data)

        # Organize GUI elements using grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.label_age.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.label_hometown.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_age.grid(row=1, column=1, padx=10, pady=5)
        self.entry_hometown.grid(row=2, column=1, padx=10, pady=5)

        self.button_submit.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_display.grid(row=4, column=0, columnspan=2, pady=10)

    def submit_data(self):
        # Get user input
        name = self.entry_name.get()
        age = self.entry_age.get()
        hometown = self.entry_hometown.get()

        # Write data to file
        with open("bio.txt", "w") as file:
            file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

        # Clear entry fields after submission
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_hometown.delete(0, tk.END)

        messagebox.showinfo("Success", "Data submitted and written to bio.txt")

    def display_data(self):
        # Read data from file and display in a messagebox
        try:
            with open("bio.txt", "r") as file:
                content = file.read()
            messagebox.showinfo("Bio Data", content)
        except FileNotFoundError:
            messagebox.showerror("Error", "File bio.txt not found. Please submit data first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BioApp(root)
    root.mainloop()
