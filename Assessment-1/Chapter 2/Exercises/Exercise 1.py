#Exercise 1: Welcome 
#Develop a GUI program to do the following using the tkinter module

#create a label to display the welcome message and change the label font style (font name, bold, size)
#Set the default window size
#Disable resizing the window
#Add background color to the Window.

import tkinter as tk
from tkinter import font

class WelcomeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome App")
        
        # Set default window size
        self.master.geometry("400x200")
        
        # Disable resizing the window
        self.master.resizable(False, False)
        
        # Add background color to the window
        self.master.configure(bg="#e6e6e6")

        # Create a label to display the welcome message
        self.welcome_label = tk.Label(self.master, text="Welcome to the GUI Program!", bg="#e6e6e6")

        # Change label font style (font name, bold, size)
        custom_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.welcome_label['font'] = custom_font

        # Pack the label to display it in the window
        self.welcome_label.pack(pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeApp(root)
    root.mainloop()
