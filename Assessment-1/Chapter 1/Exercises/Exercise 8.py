#Exercise 8: Print Pattern
#Write a program to display the following pattern using nested loops.
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

# Set the number of rows for the pattern
rows = 5

# Outer loop to iterate through each row
for i in range(1, rows + 1):
    # Inner loop to iterate through each number in the row
    for j in range(1, i + 1):
        # Print the current number with a space, end="" prevents a newline after each print
        print(j, end=" ")
    
    # Move to the next line after printing the numbers in the current row
    print()
