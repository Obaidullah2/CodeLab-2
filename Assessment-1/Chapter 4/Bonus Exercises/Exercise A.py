#Exercise A: Petrol Price
#Every time a motorist buys some petrol, he notes the number of liters bought and the amount paid per liter. This data can be found in the petrolPrice.txt file in your GitHub repository.The data is stored in columns separated by a tabbed space, like the following sample:

#Liters	cost
#20.0	  56.40
#9.6	  29.95
#5.0	  15.60
#15.0	  54.30
#18.4	  65.32
#18.7	  75.36
#17.7	  80.00
 #   Develop a GUI App that calculates:

#What was the cost of petrol per liter bought?
#What was the overall average price per liter of petrol bought?
#How much petrol in liters was bought at under 3.5AED per liter?    

import tkinter as tk
from tkinter import filedialog
import pandas as pd

class PetrolCostCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Petrol Cost Calculator")
        
        self.label = tk.Label(root, text="Select Petrol Price File:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.load_file)
        self.browse_button.pack(pady=10)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.data = pd.read_csv(file_path, delimiter='\t')
            self.result_label.config(text="File loaded successfully!")

    def calculate(self):
        if hasattr(self, 'data'):
            # Calculate cost of petrol per liter bought
            self.cost_per_liter = self.data['cost'] / self.data['Liters']

            # Calculate overall average price per liter
            average_price_per_liter = self.data['cost'].sum() / self.data['Liters'].sum()

            # Calculate petrol bought at under 3.5 AED per liter
            petrol_under_3_5 = self.data[self.data['cost'] / self.data['Liters'] < 3.5]['Liters'].sum()

            result_text = (
                f"Cost of petrol per liter bought: \n{self.cost_per_liter.round(2)}\n\n"
                f"Overall average price per liter: {average_price_per_liter:.2f} AED\n\n"
                f"Petrol bought at under 3.5 AED per liter: {petrol_under_3_5:.2f} Liters"
            )
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Please load a file first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PetrolCostCalculatorApp(root)
    root.mainloop()
