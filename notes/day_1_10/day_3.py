# Control flow and logical operators

pi = 3.1414592653589

# Google Python Style Guide
# module_name, package_name, ClassName, method_name, ExceptionName,
# function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,
# function_parameter_name, local_var_name

# conditional operators
# >     # <
# >=    # <=
# ==    # !=

# logical operators
# and
# or
# not

# myVar += 3

# modulo operator: %
# returns remainder

# if / elif / else
# parentheses not required around conditional
# name = "Myles"
# age = 33

# if name == "Jeff":
#     print("Hey Jeff")
# elif name == "Myles":
#     if age > 30:
#         if age % 2 == 1:
#             print("You're odd :)")
#         else:
#             print("Even stevens")
#     else:
#         print("Yo Myles")
# else:
#     print("Hey you")

# Challenge 3.1
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     bmi_scale = "underweight"
# elif bmi < 25:
#     bmi_scale = "normal weight"
# elif bmi < 30:
#     bmi_scale = "overweight"
# elif bmi < 35:
#     bmi_scale = "obese"
# else:
#     bmi_scale = "You are clinically obese"

# print(f"Your BMI is {bmi}, you are {bmi_scale}.")

# Challenge 3.2
# leap year is evenly divisible by 4, unless it's divisible by 100 and not divisble by 400
# year = int(input("Which year do you want to check for a leap year? "))
# is_leap_year = False

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             is_leap_year = True
#     else:
#         is_leap_year = True

# if(is_leap_year):
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is a not a leap year :(")

# Challenge 3.3
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower()
# combined_name = name1 + name2
# true_count = 0
# love_count = 0

# true_count += combined_name.count("t")
# true_count += combined_name.count("r")
# true_count += combined_name.count("u")
# true_count += combined_name.count("e")

# love_count += combined_name.count("l")
# love_count += combined_name.count("o")
# love_count += combined_name.count("v")
# love_count += combined_name.count("e")

# total_score = int(str(true_count) + str(love_count))

# if total_score < 10 or total_score > 90:
#     print(f"You score is {total_score}, you go together like coke and mentos.")
# elif total_score >= 40 and total_score <= 50:
#     print(f"Your score is {total_score}, you are alright together.")
# else:
#     print(f"Your score is {total_score}.")


# Day 3 Project
# Choose your own adventure game
# 3 single quotes allows you to have a string on multiple lines.
print('''
_     /)---(\          /~~~\
\    (/ . . \)        /  .. \
 \ __)-\(*)/         (_,\  |_)
 \_       (_         /   \@/    /^^^\
 (___/-(____) _     /      \   / . . \
              \    /  `    |   V\ Y /V
               \ /  \   | _\    / - \
                \   /__'|| \ _  |    \
                 \_____)|_).\_).||(__V
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input(
    "You are at a crossroad. Where do you want to go? Type \"left\" or \"right\" \n").lower()

if direction == "left":
    action = input(
        "You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if action == "wait":
        color = input(
            "You arrive at the island unharmed. There is a hosue with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
        if color == "yellow":
            print("\nYou Win!")
        else:
            print("\nGame Over.")
    else:
        print("\nGame Over.")
else:
    print("\nGame Over.")
