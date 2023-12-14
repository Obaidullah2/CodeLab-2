#Exercise 13: Product of list items
#Write a program that passes a list as an argument to a function. The function should then calculate the product (values multiplied) of the list values and return this value back to the main program. 

def calculate_product(my_list):
    # Function to calculate the product of values in a list
    product = 1  # Initialize the product to 1
    for value in my_list:
        product *= value  # Multiply each value in the list
    return product

# Example list
sample_list = [2, 3, 5, 7, 11]

# Call the function with the sample list
result = calculate_product(sample_list)

# Display the result
print(f"The product of the values in the list is: {result}")
