#Exercise 2 b: Square Grid ☑️
#With the pack layout manager, Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame
#Using Pack() align A and C at the top and B and D at the bottom of the frames that contain them
#Support resizing. Use the ‘expand’ and ‘fill’ attributes of the pack method to make the labels grow and expand into the available space.
#Assign border value as 5 to the frames
import tkinter as tk

# Creating the main window
root = tk.Tk()
root.title("Frames with Labels")

# Creating 2 frames for adding a pair of labels inside it
frame1 = tk.Frame(root, relief="groove", border=5)
frame2 = tk.Frame(root, relief="groove", border=5)

# creating two labels inside frame 1
labelA = tk.Label(frame1, text="A", padx=70, pady=40, bg="#22263D", fg="white")
labelB = tk.Label(frame1, text="B", padx=70, pady=40)
# creating two labels inside frame 2
labelC = tk.Label(frame2, text="C", padx=70, pady=40)
labelD = tk.Label(frame2, text="D", padx=70, pady=40, bg="#22263D", fg="white")

labelA.pack(side="top", expand=True, fill=tk.BOTH)
labelB.pack(side="bottom", expand=True, fill=tk.BOTH)

labelC.pack(side="top", expand=True, fill=tk.BOTH)
labelD.pack(side="bottom", expand=True, fill=tk.BOTH)

# Placing the frames in the main window
frame1.pack(side="left", expand=True, fill=tk.BOTH)
frame2.pack(side="right", expand=True, fill=tk.BOTH)

# Displaying the window
root.mainloop()