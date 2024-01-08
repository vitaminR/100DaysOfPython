from data.art import *
from data.game_data import *
# pylint: disable=global-variable-not-assigned



# get and set the longest drink size to variable
max_length = max(len(drink) for drink in MENU)

machine_on = True

while machine_on:

    def handle_customer_input():
        """
        Handle customer inputs.
        """
        print("Welcome to the Coffee Bot!")
        print(
            "Type 'menu' to see today's drinks or 'help' for a list of all other commands."
        )
        # Loop until the user wants to turn the machine off
        while True:
            # Prompt the user to enter a command
            command = input("What drink would you like? ").lower()

            # If the user wants to make a drink
            if command == "espresso":
                make_espresso(command)

            elif command == "latte":
                make_latte(command)

            elif command == "cappuccino":
                make_cappuccino(command)

            # If the user wants to see a report of the current resource levels
            elif command == "report":
                print_report()

            # If the user wants to see the menu
            elif command == "menu":
                print_menu()

            # If the user wants to turn the machine off
            elif command == "off":
                print("Turning off...")
                break

            # If the user wants help
            elif command == "help":
                print(
                    "Available commands: espresso, latte, cappuccino, report, menu, off, help"
                )

            # If the user enters an invalid command
            else:
                print("Invalid command.")

    machine_on = False

    #print menu and left justify by the longest drink
    def print_menu():
        '''print the drink menu'''
        for drink, details in MENU.items():
            print(
                f'{kettle_emoji} : {drink.ljust(max_length)} {coffee_emoji} ${details["cost"]}'
            )

    # Print report.
    def print_report():
        for key, value in resources.items():
            print(f" {key} : {value}ml")
        print(f" Total Money : ${money}")

    # Check resources sufficient?
    def enough_resources(drink, res):
        '''checks if enough supplies and returns T/F'''
        required_ingredients = MENU[drink]["ingredients"]
        for ingredient, required_amount in required_ingredients.items():
            # print(f"You need {required_amount}ml of {ingredient}. " )
            # print(f"you have {res[ingredient]}ml")
            if required_amount > res[ingredient]:
                print(f"you don't have enough {ingredient}.")
                return False

        return True

    # Process coins.
    def payment(drink):
        total_payment = 0
        paid = False
        while not paid:
            print(f"Please insert ${MENU[drink]['cost']} \n")
            print(" we accept pennies, nickels, dimes, and quarters ")
            total_payment += int(input("how many pennies? \n $0.01 X:") or 0) * 0.01
            print(f"credit: ${total_payment}")
            total_payment += int(input("how many nickles? \n $0.05 X:") or 0) * 0.05
            print(f"credit: ${total_payment}")
            total_payment += int(input("how many dimes? \n $0.10 X:") or 0) * 0.10
            print(f"credit: ${total_payment}")
            total_payment += int(
                input("how many quarters? \n $0.25 X:") or 0) * 0.25
            print(total_payment)
            if input(
                    f"Total inserted: ${total_payment} \n Do you want to add more money?\n y/n:"
            ) == 'y':
                continue
            else:
                return total_payment

    # make change
    def make_change(total_payment, drink_cost):
        change = total_payment - drink_cost
        if change > 0:
            print(f"Your change is ${change}")

    #  Make Coffee.
    def make_espresso(drink):
        '''takes a drink and depletes resources and adds money'''
        global resources, money
        if enough_resources(drink, resources):
            total_payment = payment(drink)
            if float(total_payment) >= float(MENU[drink]["cost"]):
                print(f"Preparing now.\n{maker_art}")
                print(f"here you go!\n{espresso_art}")
                for ingredient, values in MENU[drink]["ingredients"].items():
                    resources[ingredient] -= values
                money += MENU[drink]["cost"]
                make_change(total_payment, MENU[drink]["cost"])
            else:
                print("Not enough money honey.")
        else:
            print("Sorry we dont have enough resources")

    def make_latte(drink):
        '''takes a drink and depletes resources and adds money'''
        global resources, money
        if enough_resources(drink, resources):
            total_payment = payment(drink)
            if float(total_payment) >= float(MENU[drink]["cost"]):
                print(f"Preparing now.\n{maker_art}")
                print(f"here you go!\n{latte_art}")
                for ingredient, values in MENU[drink]["ingredients"].items():
                    resources[ingredient] -= values
                money += MENU[drink]["cost"]
                make_change(total_payment, MENU[drink]["cost"])
            else:
                print("Not enough money honey.")
        else:
            print("Sorry we dont have enough resources")

    def make_cappuccino(drink):
        '''takes a drink and depletes resources and adds money'''
        global resources, money
        if enough_resources(drink, resources):
            total_payment = payment(drink)
            if float(total_payment) >= float(MENU[drink]["cost"]):
                print(f"Preparing now.\n{maker_art}")
                print(f"here you go!\n{cappuccino_art}")
                for ingredient, values in MENU[drink]["ingredients"].items():
                    resources[ingredient] -= values
                money += MENU[drink]["cost"]
                make_change(total_payment, MENU[drink]["cost"])
            else:
                print("Not enough money honey.")
        else:
            print("Sorry we dont have enough resources")

    handle_customer_input()
