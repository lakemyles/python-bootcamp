# Dictionaries & Nesting

# Initalize dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over"
}
# print(programming_dictionary["Bug"])

# Update or append a key/value pair to a dictionary
programming_dictionary["Method"] = "A function that's part of a class"
# print(programming_dictionary["Method"])

# Loop through dictionary
# for key in programming_dictionary:
#   print(key)  # prints the key
#   print(programming_dictionary[key])  # prints the value assigned to the key


# Clear dictionary
programming_dictionary = {}

# Nesting list or dictionary in a dictionary
nesting_dictionary = {
    "List": ["First", "Second", "Third"],
    "Dictionary": {
        1: "First",
        2: "Second",
        3: "Third"
    }
}

# Print items in the nested dictionary
# for key in nesting_dictionary:
#     if key == "Dictionary":
#         for key2 in nesting_dictionary[key]:
#             print(nesting_dictionary[key][key2])


# Nesting dictionaries in a list
nesting_list = [{
    1: "First",
    2: "Second"
},
    {
    3: "Third",
    4: "Fourth"
}]

# Append dictionary to the list
nesting_list.append({
    5: "Fifth",
    6: "Sixth"
})

# Print all items from both dictionaries in the list
for item in nesting_list:
    for key in item:
        print(item[key])
