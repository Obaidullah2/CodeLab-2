#Exercise II: Sum of Digits in a Number
#Write Python Program to Find the Sum of Digits in a Number .For example if enters a number 1234 the result is 1+2+3+4 = 10.

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Initialize the sum of digits to 0
sum_of_digits = 0

# Iterate through each digit in the number
while number > 0:
    digit = number % 10  # Extract the last digit
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit

# Display the result
print(f"The sum of digits in the entered number is: {sum_of_digits}")
