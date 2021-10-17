# Data Types

# String
# "Hello"[4] # Python is 0 indexed

# Integer
# 123

# Float
# 3.14159

# Boolean
# True or False # First letter capitalized

# type function
# myType = type(123)
# print(myType)

# type casting
# myString = str(123)
# myFloat = float(123)
# myInt = int("123")
# myTypeString = type(myString)
# print(myTypeString)

# Challenge 2.1
# You can subscript any data type, not just strings
# twoDigitNumber = input("Type a two digit number: ")
# firstDigit = int(twoDigitNumber[0])
# secondDigit = int(twoDigitNumber[1])
# result = firstDigit + secondDigit
# print(result)

# In python, the result of division is considered a float

# Mathematical operators
# Addition: +
# Subtraction: -
# Multiplication *
# Division: /
# Exponent: **  # Ex: 2**2 is 2 to the power of 2

# Follows basic order of operations for mathematics (PEMDAS)

# round function
# number = round(2.66666666666, 3)
# print(number)

# floor division
# removes remainder and returns int instead of float
# number = 4 // 3
# print(number)

# mathematical shorthand
# +=
# -=
# *=
# /=

# f string
# string interpolation
# score = 100.0
# letterGrade = "A"
# myString = f"Your score is {score} and your grade is {letterGrade}"
# print(myString)

# Day 2 Project
# Create a calculator that determines the amount each person
# should pay when splitting an bill, including tip
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? "))
tip = float(input("What pecentage tip would you like to give? "))
tipPercentage = tip / 100
numberOfPeople = int(input("How many people to split the bill? "))
billTotalWithTip = totalBill + (totalBill * tipPercentage)
pricePerPerson = billTotalWithTip / numberOfPeople
formattedPricePerPerson = "{:.2f}".format(pricePerPerson)
userMessage = f"Each person should pay: ${formattedPricePerPerson}"
print(userMessage)
