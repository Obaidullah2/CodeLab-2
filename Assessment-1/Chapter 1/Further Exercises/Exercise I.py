#Exercise I: Count seconds
#Write a program that calculates the number of seconds in a day. Hint: Ask user to enter number of days, Convert days into hours, hours to minutes, minutes to seconds.


# Ask the user to enter the number of days
days = int(input("Enter the number of days: "))

# Convert days to hours, hours to minutes, and minutes to seconds
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Display the result
print(f"{days} days is equal to:")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")
#The End..