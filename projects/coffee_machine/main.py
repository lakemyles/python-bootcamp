import coffee_machine_ui
from coffee_machine import validate_payment, process_order, validate_resources


is_on = True

while is_on:
    user_selection = coffee_machine_ui.get_user_selection()
    if user_selection == "off":
        is_on = False
    elif user_selection == "report":
        coffee_machine_ui.display_report()
    else:
        has_sufficient_resources = validate_resources(user_selection)
        if has_sufficient_resources:
            user_payment = coffee_machine_ui.get_user_payment()
            is_payment_successful = validate_payment(user_selection, user_payment)
            if is_payment_successful:
                process_order(user_selection, user_payment)
            else:
                coffee_machine_ui.display_insufficient_payment()
        else:
            coffee_machine_ui.display_missing_ingredients(user_selection)









