#Exercise B: Age Calculator
#Create a program to take input of the user's date of birth and output the age. Expected input: 8/5/2018 Expected output: Your age is 5 years Hint: you can use the date from datetime package to get today's date.

from datetime import datetime  #Using datetime library

def calculate_age(birthdate):    #Asking the user DOB
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%m/%d/%Y")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age

def main():
    # Sample input: 8/5/2018
    user_input = input("Enter your date of birth (MM/DD/YYYY): ")
    try:
        age = calculate_age(user_input)
        print(f"Your age is {age} years.")
    except ValueError:
        print("Invalid date format. Please enter the date in MM/DD/YYYY format.")

if __name__ == "__main__":
    main()                 #The main function prompts the user to enter their date of birth...
