import coffee_machine_ui
from coffee_machine import validate_payment, process_order, validate_resources


do_continue = True

while do_continue:
    user_selection = coffee_machine_ui.get_user_selection()
    if user_selection == "off":
        do_continue = False
    elif user_selection == "report":
        coffee_machine_ui.display_report()
    else:
        is_sufficient_resources = validate_resources(user_selection)
        if is_sufficient_resources:
            user_payment = coffee_machine_ui.get_user_payment()
            is_sufficient_payment = validate_payment(user_selection, user_payment)
            if is_sufficient_payment:
                process_order(user_selection, user_payment)
            else:
                coffee_machine_ui.display_insufficient_payment()
        else:
            coffee_machine_ui.display_missing_ingredients(user_selection)









