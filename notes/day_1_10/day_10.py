# Function outputs & docstrings

# Docstring needs to be first line after colon and indented
# def format_name(first_name, last_name):
#     """Take a first and last name and format it
#     to return the title case version of the full name"""
#     if first_name == "" or last_name == "":
#         return
#     first_name = first_name.title()
#     last_name = last_name.title()
#     return f"{first_name} {last_name}"


# print(format_name("myLeS", "lAke"))

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# YOU CAN STORE FUNCTIONS IN A DICTIONARY OR LIST
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("Welcome to the calculator!")

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation for the options above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"The answer is {answer}")
