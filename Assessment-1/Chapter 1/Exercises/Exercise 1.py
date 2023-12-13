#Exercise 1: User Input Output:
#Write code to prompt the user to input her/his name and age and print these details on the screen. Find the length of the name and also the age of the user after one year. The format of text should look like the sample output below. (Use title() function)
#Hello, user!:


#greeting the user
print("\n Hello User !!!")

#Now  Asking the user for their name and age and saving it as variables
user_name = str(input("\n What is your name ? \n "))
user_age = int(input("\n What is your age ? \n "))

# printing statement to show appreciation to the user, using title() function to capitalize the first letter of the user's name.
print("\n It's great to see you, ", user_name.title())

#using len function to count the letters in the name of the user, then displaying the output to the user
print("\n The length of your name is: ", len(user_name))

#incrementing the user's age by 1 to display the age of the user for upcoming year
age_nxt_yr = user_age + 1
print(f"\n You will be {age_nxt_yr} next year.")
#The End:)
