#Exercise 5: Password Check 
#Develop a GUI App to check the validity of a password given by the user in the entry widget. The password should satisfy the following criteria:

#Contain at least 1 letter between a and z
#Contain at least 1 number between 0 and 9
#Contain at least 1 letter between A and Z
#Contain at least 1 character from $, #, @
#Minimum length of password: 6
#Maximum length of password: 12
#Ask user to include a maximum of 5 passcode attempts. Each time the user enters an incorrect passcode, they should be prompted of how many passcode attempts remain. If there are 5 failed passcode attempts the while loop should break and inform the user that the authorities have been alerted!    

import tkinter as tk
from tkinter import messagebox
import re

class PasswordValidatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Validator App")

        # Label to instruct the user
        self.label = tk.Label(master, text="Enter password:")
        self.label.pack(pady=10)

        # Entry widget to input the password
        self.entry = tk.Entry(master, show="*")
        self.entry.pack(pady=10)

        # Button to trigger the password validation
        self.button = tk.Button(master, text="Check Password", command=self.check_password)
        self.button.pack(pady=10)

        # Variable to track the number of remaining attempts
        self.attempts_remaining = 5

    def check_password(self):
        # Get the password entered by the user
        password = self.entry.get()

        # Validate the password
        if self.validate_password(password):
            # If the password is valid, show success message and close the application
            tk.messagebox.showinfo("Success", "Password is valid!")
            self.master.destroy()
        else:
            # If the password is invalid, decrease the attempts remaining
            self.attempts_remaining -= 1

            if self.attempts_remaining > 0:
                # If there are attempts remaining, show a warning message
                tk.messagebox.showwarning("Invalid Password",
                                          f"Invalid password! {self.attempts_remaining} attempts remaining.")
            else:
                # If no attempts remaining, show an error message, alert the authorities, and close the application
                tk.messagebox.showerror("Alert", "Authorities have been alerted! Too many failed attempts.")
                self.master.destroy()

    def validate_password(self, password):
        # Check if the password meets the specified criteria
        if 6 <= len(password) <= 12:
            if re.search("[a-z]", password) and re.search("[A-Z]", password) \
                    and re.search("[0-9]", password) and re.search("[$#@]", password):
                return True
        return False

if __name__ == "__main__":
    # Create and run the Tkinter application
    root = tk.Tk()
    app = PasswordValidatorApp(root)
    root.mainloop()
