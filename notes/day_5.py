# Loops

# for loop
# --------
# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)

# for n in range(0, 9):
#     print(n)

# fruits = ["apple", "peach", "pear"]
# for n in range(0, len(fruits)):
#     print(n)            # prints index
#     print(fruits[n])    # prints item at index

# Challenge 5.1
# Don't use sum(student_heights) / len(student_heights)
# student_heights = [180, 140, 166, 189, 155, 182]
# total = 0
# number_of_students = 0

# for height in student_heights:
#     total += height
#     number_of_students += 1

# average_height = round(total / number_of_students)
# print(average_height)


# Challenge 5.2
# Don't use max(student_scores)
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest_score = 0

# for score in student_scores:
#     if(score > highest_score):
#         highest_score = score

# print(f"The highest score is {highest_score}")

# Range
# Range includes first number, but not last number
# Range for this will be 1-100
# Can add a third parameter to change the step it will increment
# Default step is 1
# total = 0  # accumulator
# for n in range(1, 101):
#     total += n
# print(total)

# Challenge 5.3
# total = 0
# for n in range(2, 101, 2):
#     total += n
# print(total)

# Challenge 5.4
# Typical FizzBuzz question
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

# Day 5 Project
# Random Password Generator
# Could have just added everything in any order and used random.shuffle(password)
# to randomly shuffle everything instead of adding it in a random order
import secrets

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%',  '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input(
    "How many letters would you like in your password?\n"))
number_of_symbols = int(input(
    "How many symbols would you like?\n"))
number_of_numbers = int(input(
    "How many numbers would you like?\n"))

password_length = number_of_letters + number_of_symbols + number_of_numbers
password = ""
letters_used = 0
numbers_used = 0
symbols_used = 0

for n in range(1, password_length + 1):
    character_types = []
    if letters_used < number_of_letters:
        character_types.append("letter")
    if symbols_used < number_of_symbols:
        character_types.append("symbol")
    if numbers_used < number_of_numbers:
        character_types.append("number")

    random_type = secrets.choice(character_types)

    if random_type == "letter":
        password += secrets.choice(letters)
        letters_used + 1
    elif random_type == "symbol":
        password += secrets.choice(symbols)
        symbols_used += 1
    elif random_type == "number":
        password += secrets.choice(numbers)
        numbers_used += 1

print(f"Here is your password: {password}")
