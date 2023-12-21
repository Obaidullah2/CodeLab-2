#Exercise 3: Employee Class 
#Develop a GUI using Tkinter to Create an employee class with the following members: name, age, id, salary

#Add the following methods: setData() - should allow employee data to be set via user input,getData()- should output employee data to the console
#Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method and then display the output using the display_emloyee method as mentioned below Expected output:
#Name	Position	Salary	ID
#Alice	Manager		9500.0	1
#Bob	Accountant	6000.0	2
#Brain	Social Media	4000.0	3
#Frank	Salesman	2500.0	4
#Marker	Clerk		1500.0	5

import tkinter as tk

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.id = 0
        self.salary = 0.0

    def setData(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.id = emp_id
        self.salary = salary

    def getData(self):
        return f"{self.name}\t{self.getPosition()}\t{self.salary}\t{self.id}"

    def getPosition(self):
        # You can customize this method to return the position based on your data
        if self.id == 1:
            return "Manager"
        elif self.id == 2:
            return "Accountant"
        elif self.id == 3:
            return "Social Media"
        elif self.id == 4:
            return "Salesman"
        elif self.id == 5:
            return "Clerk"
        else:
            return "Unknown"

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Details")
        self.employees = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter Employee Details:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.entries = []
        labels = ["Name:", "Age:", "ID:", "Salary:"]
        for i, label_text in enumerate(labels):
            label = tk.Label(self.master, text=label_text)
            entry = tk.Entry(self.master)
            label.grid(row=i + 1, column=0, padx=10, pady=5)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entries.append(entry)

        self.add_button = tk.Button(self.master, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(self.master, text="Display Employees", command=self.display_employees)
        self.display_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.entries[0].get()
        age = int(self.entries[1].get())
        emp_id = int(self.entries[2].get())
        salary = float(self.entries[3].get())

        employee = Employee()
        employee.setData(name, age, emp_id, salary)
        self.employees.append(employee)

        for entry in self.entries:
            entry.delete(0, tk.END)

    def display_employees(self):
        print("Name\tPosition\tSalary\tID")
        for employee in self.employees:
            print(employee.getData())

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()
