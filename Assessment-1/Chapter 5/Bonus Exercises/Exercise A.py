#Exercise A: Playing around in class - Extension
#In the above Exercise -Playing around in class ask the user to enter the values of the Animal .

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
        tk.Button(self.master, text="Create Animal", command=self.create_animal).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Display Details", command=self.display_details).grid(row=7, column=0, columnspan=2, pady=10)

    def create_animal(self):
        # Create an Animal object and print a greeting
        animal_type = self.type_entry.get()
        name = self.name_entry.get()
        color = self.color_entry.get()
        age = self.age_entry.get()
        weight = self.weight_entry.get()
        noise = self.noise_entry.get()

        self.animal = Animal(animal_type, name, color, age, weight, noise)
        self.animal.sayHello()

    def display_details(self):
        try:
            # Display details of the created animal
            if hasattr(self, 'animal'):
                self.animal.animalDetails()
        except AttributeError:
            print("Please create an animal first.")

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of the AnimalGUI class
    app = AnimalGUI(root)
    # Start the Tkinter event loop
    root.mainloop()
