#Bonus Assessment Exercise A: Bar graph
#Draw a bar graph with the following information

#Title: Most valuable brands worldwide in 2023 (in billion U.S. dollars)
#brands = [ "Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
#values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67 ]
#Source - https://www.statista.com/statistics/264875/brand-value-of-the-25-most-valuable-brands/

import tkinter as tk
from tkinter import ttk

# Data
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]

# Create a Tkinter window
root = tk.Tk()
root.title("Most Valuable Brands Worldwide in 2023 (in billion U.S. dollars)")

# Create a canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Bar graph parameters
bar_width = 30
padding = 20
scale_factor = 5  # Adjust this to scale the bars appropriately

# Draw bars
for i, value in enumerate(values):
    bar_height = value / scale_factor
    x1 = i * (bar_width + padding)
    y1 = 380 - bar_height
    x2 = x1 + bar_width
    y2 = 380
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    canvas.create_text(x1 + bar_width / 2, y1 - 10, text=f"${value}B", fill="black", font=("Helvetica", 8), anchor=tk.N)

# Draw x-axis labels
for i, brand in enumerate(brands):
    x = i * (bar_width + padding) + bar_width / 2
    y = 390
    canvas.create_text(x, y, text=brand, fill="black", font=("Helvetica", 8), anchor=tk.N, angle=45)

# Run the Tkinter main loop
root.mainloop()
