#Exercise 9: Integer List:Create an integer list and perform following operations

#Create an int list with 10 values
#Output the list using a for loop
#Output the highest and lowest value
#Sort the elements in ascending order
#Sort the elements in descending order
#Append two elements
#Print the list after appending

# Create an integer list with 10 values
integer_list = [5, 2, 8, 1, 7, 3, 10, 4, 6, 9]

# Output the list using a for loop
print("Original List:")
for value in integer_list:
    print(value, end=" ")
print()

# Output the highest and lowest value
max_value = max(integer_list)
min_value = min(integer_list)
print(f"Highest value: {max_value}")
print(f"Lowest value: {min_value}")

# Sort the elements in ascending order
ascending_list = sorted(integer_list)
print("Ascending Order:")
for value in ascending_list:
    print(value, end=" ")
print()

# Sort the elements in descending order
descending_list = sorted(integer_list, reverse=True)
print("Descending Order:")
for value in descending_list:
    print(value, end=" ")
print()

# Append two elements
integer_list.append(11)
integer_list.append(0)

# Print the list after appending
print("List after Appending:")
for value in integer_list:
    print(value, end=" ")
print()
