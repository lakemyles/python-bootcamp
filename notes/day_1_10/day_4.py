# Randomization and Lists

import random
#import day_3
# print(day_3.pi)

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = round(random.random() * 10.5)
# print(random_float)

# Challenge 4.1
# random_number = random.randint(0, 1)

# if(random_number == 1):
#     print("Heads")
# else:
#     print("Tails")

# Python lists
# Can store multiple data types together
# Similar to arrays in other languages
# Negative index starts from the end
# fruits = ["apple", "banana", "orange"]
# apple = fruits[0]
# orange = fruits.pop()  # pop from end of list
# fruits.append("watermelon")  # append to end
# fruits.insert(orange)  # insert into first index
# fruits.remove("banana")  # remove item
# fruits.clear()  # remove all items

# Challenge 4.2
# names = input(
#     "Give me everybody's names, separated by a comma and a space. \n")
# names = names.split(", ")
# last_index = len(names) - 1
# random_index = random.randint(0, last_index)
# random_person = names[random_index]  # random.choice(names)
# print(f"{random_person} is going to buy the meal today.")

# Nested lists # list of lists
# fruits = ["apple", "banana", "orange"]
# vegetables = ["spinach", "peas", "kale"]
# fruits_and_veggies = [fruits, vegetables]

# Challenge 4.3
# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " "]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")
# position_x = int(position[0]) - 1
# position_y = int(position[1]) - 1

# map[position_y][position_x] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# Day 4 Project
# A rock paper scissors game to play with the computer

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
game_images = [rock, paper, scissors]

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(game_images[user_choice])
    print(f"Computer chooses: {computer_choice}")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
