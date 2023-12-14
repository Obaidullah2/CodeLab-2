#Exercise IV: Count items
#Write Python Program to Count the Number of Times an Item Appears in the List

#staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

#(Hint: For each item in the list consider it as a key, and the number of times these items appear will be its associated value)

staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Initialize an empty dictionary to store the count of each item
item_count = {}

# Count the number of times each item appears in the list
for item in staff:
    # If the item is already in the dictionary, increment its count
    if item in item_count:
        item_count[item] += 1
    # If the item is not in the dictionary, add it with a count of 1
    else:
        item_count[item] = 1

# Print the results
for item, count in item_count.items():
    print(f"{item}: {count} times")
