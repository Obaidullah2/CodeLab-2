#Exercise III: Arrows
#Write a Python program to print the asterisk pattern shown below ( hint : Use print statements)

#  *
#  ***
# *****
#*******
#*********

# Define the number of rows in the pattern
rows = 5

# Print the asterisk pattern
for i in range(1, rows + 1):
    # Print spaces before the asterisks
    for j in range(rows - i):
        print(" ", end="")
    
    # Print the asterisks
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line after completing each row
    print()

  