#Exercise 6: FizzBuzz 
#Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


# Loop through numbers from 1 to 100 
for i in range(1, 101):
    # Check if the number is a multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if the number is a multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if the number is a multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    # If the number is not a multiple of 3 or 5, print the number itself
    else:
        print(i)
