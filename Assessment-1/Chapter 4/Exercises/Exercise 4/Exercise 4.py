#Exercise 4: letter count 
#Develop a GUI App that asks the user to enter a character, reads the contents of the sentences.txt file, and counts the occurrences of the letter.

import tkinter as tk
import os

# counting the occurraneces of the target strings
def count_occurrences(sentences, target):
    return sentences.lower().count(target.lower())


# function to count the user's target string
def count_letter():
    # getting user entry
    target = letter_entry.get()
    if target and target.isalpha() and len(target) == 1:
        occurrences = count_occurrences(sentences, target)
        result_label.config(text=f"Occurrences of '{target}': {occurrences}")
    else:
        result_label.config(text="Please enter a single alphabet letter.")

# Set up the main window
root = tk.Tk()
root.title("Letter Counter")
root.geometry("400x200")
root.config(bg="sky blue")

# getting the file with os
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "sentences2.txt")
# reading the file
with open(file_path, 'r') as file:
    sentences = file.read()

# Create and pack widgets
userlabel = tk.Label(root, text="Enter a letter:", bg="sky blue", font=("Arial",10,"bold"))
userlabel.pack(pady=10)
# User Entry
letter_entry = tk.Entry(root, width=5)
letter_entry.pack(pady=10)
# calling function button
count_button = tk.Button(root, text="count occurrences", command=count_letter, bg="#565888", fg="white",padx=5,pady=2)
count_button.pack(pady=10)
# answer
result_label = tk.Label(root, text="", bg="#aeafff")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()