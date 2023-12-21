#Exercise 2: CountString 
#The file sentences.txt has a list of string data. Develop a GUI App that finds out how many times the following string appears

#Hello my name is Peter Parker
#I love Python Programming
#Love
#Enemy  
#Extension:Create an entry label for free search in the above app
import tkinter as tk
from tkinter import messagebox

class StringCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Counter App")

        # Create and set up GUI elements
        self.label_search = tk.Label(root, text="Search String:")
        self.entry_search = tk.Entry(root)

        self.button_count = tk.Button(root, text="Count Occurrences", command=self.count_occurrences)

        # Organize GUI elements using grid layout
        self.label_search.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_search.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

        self.button_count.grid(row=1, column=0, columnspan=3, pady=10)

        # Try to read default text from the file
        try:
            with open("sentences.txt", "r") as file:
                self.sentences = file.read().splitlines()
        except FileNotFoundError:
            # If the file is not found, create it with predefined sentences
            self.sentences = [
                "Hello my name is Peter Parker",
                "I love Python Programming",
                "Love",
                "Enemy"
            ]
            with open("sentences.txt", "w") as file:
                file.write("\n".join(self.sentences))

        # Create a label to display the default text
        self.label_default_text = tk.Label(root, text="\n".join(self.sentences), justify="left")
        self.label_default_text.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

    def count_occurrences(self):
        # Get user input for the search string
        search_string = self.entry_search.get()

        if not search_string:
            messagebox.showwarning("Warning", "Please enter a search string.")
            return

        # Count occurrences of the search string in the list of sentences
        count = sum(1 for sentence in self.sentences if search_string.lower() in sentence.lower())

        # Display the count in a messagebox
        messagebox.showinfo("Occurrences Count", f"The string '{search_string}' appears {count} times.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StringCounterApp(root)
    root.mainloop()
