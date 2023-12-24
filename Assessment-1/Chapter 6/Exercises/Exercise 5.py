# Create a JSON file named 'StudentJson.json' with the following details

# Ask the user to enter the student name, ID, and course and write these contents to the JSON file. 2.Read the contents 
# from the JSON file and display the individual values.
# Expected Output :
# Details of the Student are
#   	Name: Alpha
#   	ID: 1
#   	course: BSc CC
# Append another dictionary as follows as key value pair for student 1 in StudentDetails dictionary to form a nested dictionay. 
# Later update the JSON file.
#  "CourseDetails":{ 
#              		 "Group": "A",
#              		 "Year": 2
# 		}
# Print the individual vlaues of the Student details reading from JSON file.
# Expected Output :

# Details of the Student are
# 		  Name: Alpha
# 		  ID: 1
#  		 course: BSc CC
#  		 Group: A
#  		 Year: 2


import json

# Function to input student details and write to JSON file
def write_to_json():
    student_details = {}
    
    # Get user input
    student_details['Name'] = input("Enter student name: ")
    student_details['ID'] = int(input("Enter student ID: "))
    student_details['course'] = input("Enter course: ")

    # Append CourseDetails as a nested dictionary
    student_details['CourseDetails'] = {
        "Group": input("Enter group: "),
        "Year": int(input("Enter year: "))
    }

    # Write to JSON file
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file)

    print("Student details written to StudentJson.json")

# Function to read and display student details from JSON file
def read_from_json():
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    # Display individual values
    print("\nDetails of the Student are")
    print(f"\tName: {student_details['Name']}")
    print(f"\tID: {student_details['ID']}")
    print(f"\tcourse: {student_details['course']}")
    print(f"\tGroup: {student_details['CourseDetails']['Group']}")
    print(f"\tYear: {student_details['CourseDetails']['Year']}")

# Write to JSON file
write_to_json()

# Read from JSON file and display individual values
read_from_json()
