import coffee_machine_ui


resources = dict(water=300, milk=200, coffee=100, money=0)
products = dict(
    espresso=dict(cost=2, ingredients=dict(water=50, milk=50, coffee=25)),
    latte=dict(cost=2, ingredients=dict(water=50, milk=50, coffee=25)),
    cappuccino=dict(cost=2, ingredients=dict(water=50, milk=50, coffee=25))
)


def calculate_user_refund(selection, payment_amount):
    product_price = products[selection]["cost"]
    refund_amount = payment_amount - product_price
    return round(refund_amount, 2)


def calculate_user_payment(quarters, dimes, nickels, pennies):
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def process_order(selection, payment):
    refund_amount = calculate_user_refund(selection, payment)
    if refund_amount > 0:
        payment -= refund_amount
        coffee_machine_ui.display_refund(refund_amount)
    resources["money"] += payment
    resources["water"] -= products[selection]["ingredients"]["water"]
    resources["milk"] -= products[selection]["ingredients"]["milk"]
    resources["coffee"] -= products[selection]["ingredients"]["coffee"]
    coffee_machine_ui.display_choice(selection)


def validate_resources(selection):
    missing_ingredients = get_missing_ingredients(selection)
    if len(missing_ingredients) > 0:
        return False
    return True


def validate_payment(selection, payment):
    selection_cost = products[selection]["cost"]
    if selection_cost > payment:
        return False
    return True


def get_missing_ingredients(selection):
    missing_ingredients = []
    for ingredient in products[selection]["ingredients"]:
        amount_required = products[selection]["ingredients"][ingredient]
        amount_available = resources[ingredient]
        if amount_required > amount_available:
            missing_ingredients.append(ingredient)
    return missing_ingredients

