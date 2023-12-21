#Exercise 1: Woof Woof 
#Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects from this class and assign data to its members. The program should then output the data from each object and the oldest dog should woof via a class method.


import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

    @classmethod
    def oldest_dog_woof(cls, dog1, dog2):
        oldest_dog = dog1 if dog1.age > dog2.age else dog2
        messagebox.showinfo("Woof!", f"{oldest_dog.name} says: Woof!")

class DogGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dog Information")

        self.dog1 = Dog("Buddy", 3, "Labrador")
        self.dog2 = Dog("Max", 5, "Golden Retriever")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Dog 1 Information:").pack()
        tk.Label(self.root, text=self.dog1.display_info()).pack()

        tk.Label(self.root, text="\nDog 2 Information:").pack()
        tk.Label(self.root, text=self.dog2.display_info()).pack()

        tk.Button(self.root, text="Woof! (Oldest Dog)", command=self.woof).pack()

    def woof(self):
        Dog.oldest_dog_woof(self.dog1, self.dog2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DogGUI(root)
    root.mainloop()
