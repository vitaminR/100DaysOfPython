from day15_stuff import *

machine_on = True

print("welcome to coffee machine bot! Please take a look at our menu:")

# get and set the longest drink size to variable
max_length = max(len(drink) for drink in MENU.keys())
print(max_length)
#print menu and left justify by the longest drink
for drink, details in MENU.items(): 
    print(f'{kettle_emoji} : {drink.ljust(max_length)} {coffee_emoji} ${details["cost"]}')

# TODO turn machine off
off = "return machine_on = True"

# TODO Print report.
def report():
    for key, value in resources.items():
        print(f" {key} : {value}")

# TODO Check resources sufficient?


# TODO Process coins.


# TODO Check transaction successful?


# TODO Make Coffee.


