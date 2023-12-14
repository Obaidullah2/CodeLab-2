#Exercise A: Multiplication Tables 
#Write a program to print Multiplication table in following format from 1 to 10 tables Hint: Use nested loops
# Print multiplication table from 1 to 10

for a in range(1, 11):  # Outer loop for the multiplicand
    print(f"\nMultiplication table for {a}:\n")
    for b in range(1, 11):  # Inner loop for the multiplier
        result = a * b
        print(f"{a} x {b} = {result}")
