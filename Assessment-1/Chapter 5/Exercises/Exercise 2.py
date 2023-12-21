#Exercise 2: Student Class 
#Develop a GUI using Tkinter to Create a class called Students.

#The class should have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int) 
#The class should have the following methods calcGrade() - should return an average from the three marks.display()- should output the student name and calculated grade average
#Create one object using a constructor that contains parameters to initialize all of the variables
#Ask user to input the variable values using input() and pass the values to the second object

import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average

    def display(self):
        return f"Name: {self.name}\nAverage Grade: {self.calcGrade()}"

def create_student():
    # Get values from entry widgets
    name = entry_name.get()
    mark1 = int(entry_mark1.get())
    mark2 = int(entry_mark2.get())
    mark3 = int(entry_mark3.get())

    # Create Students object with entered values
    student = Students(name, mark1, mark2, mark3)
    
    # Display student information using a messagebox
    messagebox.showinfo("Student Information", student.display())

# GUI setup
root = tk.Tk()
root.title("Student Information")

# Labels
label_name = tk.Label(root, text="Name:")
label_mark1 = tk.Label(root, text="Mark 1:")
label_mark2 = tk.Label(root, text="Mark 2:")
label_mark3 = tk.Label(root, text="Mark 3:")

# Entry widgets
entry_name = tk.Entry(root)
entry_mark1 = tk.Entry(root)
entry_mark2 = tk.Entry(root)
entry_mark3 = tk.Entry(root)

# Button to create student
create_button = tk.Button(root, text="Create Student", command=create_student)

# Grid layout
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="E")
label_mark1.grid(row=1, column=0, padx=10, pady=5, sticky="E")
label_mark2.grid(row=2, column=0, padx=10, pady=5, sticky="E")
label_mark3.grid(row=3, column=0, padx=10, pady=5, sticky="E")

entry_name.grid(row=0, column=1, padx=10, pady=5)
entry_mark1.grid(row=1, column=1, padx=10, pady=5)
entry_mark2.grid(row=2, column=1, padx=10, pady=5)
entry_mark3.grid(row=3, column=1, padx=10, pady=5)

create_button.grid(row=4, column=1, pady=10)

root.mainloop()
