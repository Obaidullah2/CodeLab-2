#Exercise V: Lamda function
#Create the list marks with the given values

#marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]

#Using lambda function in the function sort the list elements of the tuple based on marks low to high and high to low.

# Given list of tuples
marks = [("CodeLab I", 67), ("Web Development", 75), ("CodeLab II", 74), 
         ("Smartphone Apps", 68), ("Games Development", 70), ("Responsive Web", 65)]

# Sort the list based on marks (low to high)
sorted_low_to_high = sorted(marks, key=lambda x: x[1])

# Sort the list based on marks (high to low)
sorted_high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)

# Display the results
print("Sorted list based on marks (low to high):")
for subject, mark in sorted_low_to_high:
    print(f"{subject}: {mark}")

print("\nSorted list based on marks (high to low):")
for subject, mark in sorted_high_to_low:
    print(f"{subject}: {mark}")
