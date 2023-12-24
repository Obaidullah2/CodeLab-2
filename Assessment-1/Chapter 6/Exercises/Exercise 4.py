#Exercise 4: Line graph 
#Draw a line in a diagram from position (1, 2) to position (6, 8)
#Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)


import tkinter as tk

def draw_lines(canvas):
    # Solid Line
    canvas.create_line(10, 20, 60, 80, fill="black")

    # Dotted Line
    canvas.create_line(10, 30, 20, 80, fill="black", dash=(2, 2))
    canvas.create_line(20, 80, 60, 10, fill="black", dash=(2, 2))
    canvas.create_line(60, 10, 80, 100, fill="black", dash=(2, 2))

# Create the main window
root = tk.Tk()
root.title("Line Drawing Example")

# Create a canvas widget
canvas = tk.Canvas(root, width=100, height=120)
canvas.pack()

# Draw the lines
draw_lines(canvas)

# Start the Tkinter event loop
root.mainloop()
