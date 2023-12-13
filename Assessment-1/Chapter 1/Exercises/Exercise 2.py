#Exercise 2: Maths 
#Write a program that evaluates the following calculations for two int numbers obtained from the user and outputs the results to the console:

#Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)



# Asking the user to enter two numbers for the  required calculations
num1 = int(input("\n Please enter the first number = "))
num2 = int(input("\n Please enter the second number = "))

#  now Calculating both of the numbers

add = num1 + num2  # adding both of the numbers
sub = num1 - num2  # subtracting  both of the numbers
mul = num1 * num2  # multiplying both  of the numbers
div = num1 / num2  # dividing both of the numbers
mod = num1 % num2  # modulus (remainder) for both the numbers

#Displaying the output for each  of the calculations

print("\n The addition of the two numbers is = ", add)
print("\n The subtraction of the two numbers is = ", sub)
print("\n The multiplication of the two numbers is = ", mul)
print("\n The division of the two numbers is = ", div)
print("\n The modulus (remainder) of the two numbers is = ", mod)

# The End