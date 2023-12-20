#Exercise A: Temperature Converter
#Develop a GUI that implements a temperature converter application using Tkinter, allowing users to convert between Celsius and Fahrenheit. 
import tkinter as tk

def convert_temperature():
    try:
        if selected_unit.get() == "Celsius to Fahrenheit":
            result = (float(entry_temperature.get()) * 9/5) + 32
            result_label.config(text=f"Result: {result:.2f} °F")
        elif selected_unit.get() == "Fahrenheit to Celsius":
            result = (float(entry_temperature.get()) - 32) * 5/9
            result_label.config(text=f"Result: {result:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Entry widget for user input
entry_temperature = tk.Entry(window, width=15)
entry_temperature.insert(0, "Enter temperature")

# Bind event to remove default text when entry is clicked
def on_entry_click(event):
    if entry_temperature.get() == "Enter temperature":
        entry_temperature.delete(0, tk.END)
        entry_temperature.config(fg="black")

entry_temperature.bind("<FocusIn>", on_entry_click)

# Label and dropdown menu for selecting conversion unit
unit_label = tk.Label(window, text="Select Conversion:")
selected_unit = tk.StringVar()
selected_unit.set("Celsius to Fahrenheit")
unit_menu = tk.OptionMenu(window, selected_unit, "Celsius to Fahrenheit", "Fahrenheit to Celsius")

# Button to perform the conversion
convert_button = tk.Button(window, text="Convert", command=convert_temperature)

# Label to display the result
result_label = tk.Label(window, text="Result: ")

# Grid layout
entry_temperature.grid(row=0, column=0, padx=10, pady=10)
unit_label.grid(row=1, column=0, padx=10, pady=10)
unit_menu.grid(row=1, column=1, padx=10, pady=10)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
