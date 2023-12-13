#Exercise 4: Largest Number:
#Write a program to input three numbers and outputs the largest using the multiple if -else statements.

# start of the program

# asking the user to enter the three numbers
num1 = int(input("\n Please enter the first number = "))
num2 = int(input("\n Please enter the second number = "))
num3 = int(input("\n Please enter the third number = "))

#checking if all 3 numbers are equal
if num1 == num2 == num3:
    print("All three numbers are equal")
# using conditional statements to check the largest number
if num1 > num2 and num1 > num3: # will run if the first number is the largest
    print(f"\n The number {num1} is the largest number.")

elif num2 > num1 and num2 > num3: # will run if the second number is largest
    print(f"\n The number {num2} is the largest number.")

elif num3 > num1 and num3 > num2: # will run if the third number is the largest
    print(f"\n The number {num3} is the largest number.")

# end of the program    