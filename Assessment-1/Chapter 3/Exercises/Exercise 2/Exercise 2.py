#Exercise 2: Coffee Vending Machine
#Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.  

#Extension :Add other features to the previous app such as handling money.
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def calculate_total_price(coffee_type, sugar_level, milk_level, cup_size):
    # Setting prices and getting user preferences
    coffee_price_dict = {"Coffee": 2.50, "Latte": 3.00, "Espresso": 2.00}
    base_price = coffee_price_dict.get(coffee_type, 0)
    sugar_price_dict = {"None": 0, "Less": -0.25, "Standard": 0, "Extra": 0.25}
    sugar_price = sugar_price_dict.get(sugar_level, 0)
    milk_price_dict = {"None": 0, "Less": -0.25, "Standard": 0, "Extra": 0.25}
    milk_price = milk_price_dict.get(milk_level, 0)
    
    # Add price based on cup size
    cup_size_price_dict = {"Small": 0.25, "Medium": 0.50, "Large": 1.00}
    cup_size_price = cup_size_price_dict.get(cup_size, 0)

    return base_price + sugar_price + milk_price + cup_size_price

def make_receipt():
    # Get user preferences
    coffee_type = coffee_var.get()
    sugar_level = sugar_var.get()
    milk_level = milk_var.get()
    cup_size = cup_size_var.get()

    total_price = calculate_total_price(coffee_type, sugar_level, milk_level, cup_size)
    receipt_total_price.config(text=f"Total Price: ${total_price:.2f}")

    # Update the order_label with the customized message
    order_message = f"You ordered a {cup_size} cup size {coffee_type.lower()} with {milk_level.lower()} milk and {sugar_level.lower()} sugar."
    order_label.config(text=order_message)

    receipt_frame.pack()

def calc_change():
    cost = float(receipt_total_price.cget("text").split("$")[1])
    change = float(money_entry.get()) - cost
    if change > 0:
        receipt_total_price.config(text="Total Price: $0.00")
        change_label.config(text=f"Change: ${change:.2f}")
        changelabel.config(text="Thank you for buying!\nEnjoy your coffee!")
    else:
        change_label.config(text=f"Insufficient money. Try again")
        changelabel.config(text="")

root = tk.Tk()
root.geometry("800x400")
root.title("Coffee Vending Machine")

# Colors
background_color = "#E6E6E6"
button_color = "#FFA500"
text_color = "#333333"
label_color = "#663300"

# Input Frame
input_frame = tk.Frame(root, bg=background_color, pady=10, border=1, relief="groove", highlightbackground=label_color, highlightcolor=label_color)
input_frame.pack(side="left", expand=1, fill="both", padx=10, pady=10)

# Welcome text
label_title = tk.Label(input_frame, text="Welcome to the Coffee Vending Machine!", fg=label_color, font=("Helvetica", 14, "bold"), bg=background_color)
label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Type
label_coffee_type = tk.Label(input_frame, text="Coffee Type:", bg=background_color)
label_coffee_type.grid(row=1, column=0)
# Dropdown for user to pick
coffee_options = ["Coffee", "Latte", "Espresso"]
coffee_var = tk.StringVar()
coffee_menu = ttk.Combobox(input_frame, textvariable=coffee_var, values=coffee_options, style="TCombobox")
coffee_menu.grid(row=1, column=1, pady=5)
coffee_var.set("Coffee")

# Sugar
label_sugar = tk.Label(input_frame, text="Sugar:", bg=background_color)
label_sugar.grid(row=2, column=0)
sugar_options = ["None", "Less", "Standard", "Extra"]
sugar_var = tk.StringVar()
sugar_menu = ttk.Combobox(input_frame, textvariable=sugar_var, values=sugar_options, style="TCombobox")
sugar_menu.grid(row=2, column=1, pady=5)
sugar_var.set("Standard")

# Milk
label_milk = tk.Label(input_frame, text="Milk:", bg=background_color)
label_milk.grid(row=3, column=0)
milk_options = ["None", "Less", "Standard", "Extra"]
milk_var = tk.StringVar()
milk_menu = ttk.Combobox(input_frame, textvariable=milk_var, values=milk_options, style="TCombobox")
milk_menu.grid(row=3, column=1, pady=5)
milk_var.set("Standard")

# Cup
label_cup_size = tk.Label(input_frame, text="Cup Size:", bg=background_color)
label_cup_size.grid(row=4, column=0)
cup_size_options = ["Small", "Medium", "Large"]
cup_size_var = tk.StringVar()
cup_size_menu = ttk.Combobox(input_frame, textvariable=cup_size_var, values=cup_size_options, style="TCombobox")
cup_size_menu.grid(row=4, column=1, pady=5)
cup_size_var.set("Medium")

# Receipt making button which will show the receipt
make_receipt_button = tk.Button(input_frame, text="Make Receipt", command=make_receipt, bg=button_color, fg="white")
make_receipt_button.grid(row=5, column=0, columnspan=2, pady=20)

# Display Frame
display_frame = tk.Frame(root, bg=background_color, pady=10, border=1, relief="groove")
display_frame.pack(side="right", expand=1, fill="both", padx=10, pady=10)

script_directory = os.path.dirname(os.path.realpath(__file__))
img = Image.open(os.path.join(script_directory, "espresso.png"))
tk_img = ImageTk.PhotoImage(img)

# Creating a label which contains the image and placing it as a background
background_label = tk.Label(display_frame, image=tk_img)
background_label.place(relwidth=1, relheight=1)

# Receipt Frame
receipt_frame = tk.Frame(display_frame, bg=label_color, pady=30, padx=20)

# User's order label
order_label = tk.Label(receipt_frame, text="", wraplength=300, justify='left', fg=background_color, bg=label_color)
order_label.pack(pady=10)

receipt_total_price = tk.Label(receipt_frame, text="Total Price: $0.00", fg=background_color, bg=label_color)
receipt_total_price.pack()

# Enter Money Label
enter_money_label = tk.Label(receipt_frame, text="Enter Money:", fg=background_color, bg=label_color)
enter_money_label.pack()
# Entry for user to input money
money_entry = tk.Entry(receipt_frame, bg=text_color)
money_entry.pack(pady=10)

# Change and bill labels
change_label = tk.Label(receipt_frame, text="", fg=background_color, bg=label_color)
change_label.pack()

# Change label which will either give change or say thank you for buying
changelabel = tk.Label(receipt_frame, text="", fg=background_color, bg=label_color)
changelabel.pack()

# Buy button which will give the change if there is any using the function to calculate
buy_button = tk.Button(receipt_frame, text="Buy", command=calc_change, bg=button_color, padx=10)
buy_button.pack(pady=10)

receipt_frame.pack()

root.mainloop()
