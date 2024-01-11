from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
order = ""

art = ("""
      )  (
     (   ) )
      ) ( (
  _________.'
 |- - - - - |
(  COFFEE   `} 
 `-.______.-'
""")

coffee_icons = {
    "latte": "☕",
    "espresso": "🍵",
    "cappuccino": "🍮",
}

print("Welcome to the Coffee Machine!")
print("================================")
print(art)
print("================================")


while order != "off":
    print("\nWhat would you like to drink?")
    for item in menu.get_items().split('/'):
        print(f"{coffee_icons.get(item, '🍶')} {item.capitalize()}")
    order = input("Please enter your choice: ").lower()
    if order == "report":
        print("\n================ REPORT ================")
        coffee_maker.report()
        money_machine.report()
        print("========================================")
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                print(f"\nThat will be ${drink.cost}. Please insert coins.")
                if money_machine.make_payment(drink.cost):
                    print(f"Here is your change: ${money_machine.change}")
                    print("\nMaking your drink...")
                    coffee_maker.make_coffee(drink)
                    print("================================")
                    