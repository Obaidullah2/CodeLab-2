#Exercise 5: Playing around in class 
#Use this exercise to play around with creating and accessing class members and methods. Develop a GUI using Tkinter to Create a class called Animal

#Give the class at least the following members Type, Name, Colour, Age, Weight, Noise
#The class should have the following methods sayHello() - says its name via print,makeNoise() -make an appropriate noise via print, animalDetails() -output all the details of the animal object
#Instantiate at least two objects from your animal class (e.g. Dog, Cow)
#Set values for each of the variables
#Invoke each of the class functions

import tkinter as tk

class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        # Initialize the attributes of the Animal class
        self.Type = animal_type
        self.Name = name
        self.Colour = color
        self.Age = age
        self.Weight = weight
        self.Noise = noise

    def sayHello(self):
        # Method to print a greeting using the animal's name
        print(f"Hello, I'm {self.Name}!")

    def makeNoise(self):
        # Method to print the noise the animal makes
        print(f"{self.Name} says: {self.Noise}")

    def animalDetails(self):
        # Method to print all details of the animal
        details = f"Type: {self.Type}\nName: {self.Name}\nColour: {self.Colour}\nAge: {self.Age}\nWeight: {self.Weight}\nNoise: {self.Noise}"
        print(details)
        return details

class AnimalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Animal Details")

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for input
        tk.Label(self.master, text="Type:").grid(row=0, column=0, sticky="e")
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="e")
        tk.Label(self.master, text="Colour:").grid(row=2, column=0, sticky="e")
        tk.Label(self.master, text="Age:").grid(row=3, column=0, sticky="e")
        tk.Label(self.master, text="Weight:").grid(row=4, column=0, sticky="e")
        tk.Label(self.master, text="Noise:").grid(row=5, column=0, sticky="e")

        self.type_entry = tk.Entry(self.master)
        self.name_entry = tk.Entry(self.master)
        self.color_entry = tk.Entry(self.master)
        self.age_entry = tk.Entry(self.master)
        self.weight_entry = tk.Entry(self.master)
        self.noise_entry = tk.Entry(self.master)

        self.type_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.color_entry.grid(row=2, column=1)
        self.age_entry.grid(row=3, column=1)
        self.weight_entry.grid(row=4, column=1)
        self.noise_entry.grid(row=5, column=1)

        # Buttons to create and display animal details
        tk.Button(self.master, text="Create Dog", command=self.create_dog).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Create Cow", command=self.create_cow).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Display Details", command=self.display_details).grid(row=8, column=0, columnspan=2, pady=10)

    def create_dog(self):
        # Create a Dog object and print a greeting
        self.dog = Animal("Dog", self.name_entry.get(), self.color_entry.get(), self.age_entry.get(), self.weight_entry.get(), self.noise_entry.get())
        self.dog.sayHello()

    def create_cow(self):
        # Create a Cow object and print a greeting
        self.cow = Animal("Cow", self.name_entry.get(), self.color_entry.get(), self.age_entry.get(), self.weight_entry.get(), self.noise_entry.get())
        self.cow.sayHello()

    def display_details(self):
        try:
            # Display details of the created animals
            if hasattr(self, 'dog'):
                self.dog.animalDetails()
            if hasattr(self, 'cow'):
                self.cow.animalDetails()
        except AttributeError:
            print("Please create an animal first.")

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of the AnimalGUI class
    app = AnimalGUI(root)
    # Start the Tkinter event loop
    root.mainloop()
