#Bonus Assessment Exercise - Burger Shack Vendor
#Burger Shack is about to open in RAK, however, the fast food chain is in need of an ordering system. Write a program to handle the ordering process for the burger shack. The program should include:

#The ability to choose between at least three burger types (e.g. Beef, Chicken, Vegetarian)
#The ability to add toppings, with at least three to choose from (e.g. cheese, peanut butter, avocado)
#The ability to add condiments, with at least three to choose from (e.g. ketchup, mayonnaise, bbq sauce)
#The ability to add sides, these can include items such as fries and drinks.
#The ability to handle payment and return change to the user
#You should design your program to make use of functions and pass information to and from these as appropriate. Alongside the above requirements, you are free to extend the functionality of the program as you see fit.

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class BurgerShackOrderingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Burger Shack Ordering System")

        # Get the current script directory
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Load background image
        try:
            image_path = os.path.join(script_directory, "background_image.png")
            self.background_image = ImageTk.PhotoImage(Image.open(image_path))
        except Exception as e:
            messagebox.showerror("Error", f"Couldn't open the background image: {e}")
            root.destroy()
            return

        # Create a canvas to set the background image
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Variables to store user selections
        self.burger_var = tk.StringVar()
        self.toppings_var = tk.StringVar()
        self.condiments_var = tk.StringVar()
        self.side_var = tk.StringVar()

        # Menu options
        self.burger_options = ["Beef Burger", "Chicken Burger", "Vegetarian Burger"]
        self.toppings_options = ["Cheese", "Peanut Butter", "Avocado"]
        self.condiments_options = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
        self.side_options = ["Fries", "Drink", "Fries and Drink"]

        # Payment variables
        self.total_cost = tk.DoubleVar()
        self.amount_paid_var = tk.DoubleVar()

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Burger selection
        tk.Label(self.canvas, text="Select Burger:", bg="lightgrey").pack()
        for i, option in enumerate(self.burger_options):
            tk.Radiobutton(self.canvas, text=option, variable=self.burger_var, value=option, bg="lightgrey").pack()

        # Toppings selection
        tk.Label(self.canvas, text="Select Topping:", bg="lightgrey").pack()
        for i, option in enumerate(self.toppings_options):
            tk.Radiobutton(self.canvas, text=option, variable=self.toppings_var, value=option, bg="lightgrey").pack()

        # Condiments selection
        tk.Label(self.canvas, text="Select Condiment:", bg="lightgrey").pack()
        for i, option in enumerate(self.condiments_options):
            tk.Radiobutton(self.canvas, text=option, variable=self.condiments_var, value=option, bg="lightgrey").pack()

        # Side selection
        tk.Label(self.canvas, text="Select Side:", bg="lightgrey").pack()
        for i, option in enumerate(self.side_options):
            tk.Radiobutton(self.canvas, text=option, variable=self.side_var, value=option, bg="lightgrey").pack()

        # Payment section
        tk.Label(self.canvas, text="Payment:", bg="lightgrey").pack()
        tk.Label(self.canvas, text="Total Cost: $", bg="lightgrey").pack()
        tk.Entry(self.canvas, textvariable=self.total_cost, state='readonly').pack()

        tk.Label(self.canvas, text="Amount Paid: $", bg="lightgrey").pack()
        tk.Entry(self.canvas, textvariable=self.amount_paid_var).pack()

        # Order button
        tk.Button(self.canvas, text="Place Order", command=self.show_order_summary, bg="orange").pack()

    def show_order_summary(self):
        # Get user selections
        burger_choice = self.burger_var.get()
        toppings_choice = self.toppings_var.get()
        condiment_choice = self.condiments_var.get()
        side_choice = self.side_var.get()

        # Calculate total cost
        burger_price = 5.99  # Placeholder price for a burger
        topping_price = 1.50  # Placeholder price for each topping
        condiment_price = 0.75  # Placeholder price for each condiment
        side_price = 2.50  # Placeholder price for each side

        total_cost = (
            burger_price +
            topping_price +
            condiment_price +
            (side_price if "Fries" in side_choice else 0) +
            (side_price if "Drink" in side_choice else 0)
        )

        self.total_cost.set(f"{total_cost:.2f}")

        # Get amount paid by the user
        try:
            amount_paid = float(self.amount_paid_var.get())
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid amount.")
            return

        # Calculate change
        change = amount_paid - total_cost

        # Display order summary with amount paid and change
        order_summary = f"Order Summary:\n\n"
        order_summary += f"Burger: {burger_choice}\n"
        order_summary += f"Toppings: {toppings_choice}\n"
        order_summary += f"Condiments: {condiment_choice}\n"
        order_summary += f"Side: {side_choice}\n"
        order_summary += f"Total Cost: ${total_cost:.2f}\n"
        order_summary += f"Amount Paid: ${amount_paid:.2f}\n"
        order_summary += f"Change: ${change:.2f}"

        messagebox.showinfo("Order Summary", order_summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = BurgerShackOrderingSystem(root)
    root.mainloop()

