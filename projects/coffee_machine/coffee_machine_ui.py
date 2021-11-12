import coffee_machine


def get_user_selection():
    return input("What would you like? (espresso/latte/cappuccino): ")


def get_user_payment():
    print("Please inserts coins.")

    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    return coffee_machine.calculate_user_payment(quarters, dimes, nickels, pennies)


def display_report():
    resources = coffee_machine.resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def display_refund(refund_amount):
    print(f"Here is ${refund_amount} in change.")


def display_choice(selection):
    print(f"Here is your {selection}. Enjoy!\n")


def display_missing_ingredients(selection):
    missing_ingredients = coffee_machine.get_missing_ingredients(selection)
    for ingredient in missing_ingredients:
        print(f"Sorry there is not enough {ingredient}\n")


def display_insufficient_payment():
    print("Sorry that's not enough money. Money refunded.\n")

