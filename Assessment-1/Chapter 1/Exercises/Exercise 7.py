#Exercise 7: Even Numbers:Write a program that prints the even numbers from 1 to 100. Hint - Use Continue Statement


# Loop through numbers from 1 to 100 
for i in range(1, 101):
    # Check if the number is odd
    if i % 2 != 0:
        # If the number is odd, skip to the next iteration
        continue
    # If the number is even, print it
    print(i)
