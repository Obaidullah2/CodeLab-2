#Exercise 1: Greeting App 
#Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.

#In InputFrame, include the following:

#A title label in blue.
#An entry field for the user's name.
#A dropdown menu for selecting a color.
#An "Update Greeting" button.
#In DisplayFrame, include a label to display the personalized greeting.
#Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.
#Use different background colors for each frame.

import tkinter as tk
from tkinter import ttk

class GreetingApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Greeting App")

        # Create InputFrame for user input
        self.input_frame = ttk.Frame(root, padding="10", style="Input.TFrame")
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create DisplayFrame for displaying personalized greeting
        self.display_frame = ttk.Frame(root, padding="10", style="Display.TFrame")
        self.display_frame.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Set default background colors for frames and labels
        self.root.option_add('*TFrame*background', 'lightgray')
        self.root.option_add('*TLabel*background', 'lightgray')

        style = ttk.Style()
        style.configure("Input.TFrame", background="lightblue")
        style.configure("Display.TFrame", background="lightgreen")

        # Create and place widgets in InputFrame
        ttk.Label(self.input_frame, text="Greeting App", foreground="blue", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=5)

        ttk.Label(self.input_frame, text="Enter your name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(self.input_frame)
        self.name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(self.input_frame, text="Select color:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.color_var = tk.StringVar(value="blue")  # Default color
        color_dropdown = ttk.Combobox(self.input_frame, textvariable=self.color_var, values=["blue", "red", "green"])
        color_dropdown.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        update_button = ttk.Button(self.input_frame, text="Update Greeting", command=self.update_greeting)
        update_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Create and place widgets in DisplayFrame
        self.greeting_label = ttk.Label(self.display_frame, text="", font=("Helvetica", 14))
        self.greeting_label.grid(row=0, column=0, pady=20)

    def update_greeting(self):
        # Get user input and update the greeting label with the selected color
        name = self.name_entry.get()
        color = self.color_var.get()
        greeting_text = f"Hello, {name}!"
        self.greeting_label.config(text=greeting_text, foreground=color)

if __name__ == "__main__":
    # Run the application
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()

