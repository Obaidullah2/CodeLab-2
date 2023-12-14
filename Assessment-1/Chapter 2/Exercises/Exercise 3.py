#Exercise 3: Login page 
#Create a login page using the Grid geometry.

import tkinter as tk
from tkinter import messagebox

def check_login():
    username = entry_username.get()
    password = entry_password.get()

    # You can add your authentication logic here
    # For simplicity, we'll just check if the username and password are not empty
    if username and password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place widgets using the grid layout
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Show asterisks for password
button_login = tk.Button(root, text="Login", command=check_login)

label_username.grid(row=0, column=0, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_login.grid(row=2, column=0, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
