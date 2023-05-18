import os
import sys
import time

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

while True:
    choices = {}
    for index, items in enumerate(menu.menu):
        choices[str(index + 1)] = items
    user_choice = ""
    while user_choice not in ("1", "2", "3", "off", "report"):
        user_choice = input(
            f"What would you like?\n1: {choices['1'].name} cost -> ${choices['1'].cost} \n2: {choices['2'].name} cost -> ${choices['2'].cost} \n3: {choices['3'].name} cost -> ${choices['3'].cost}\n"
        )

    if user_choice == "off":
        sys.exit()
    elif user_choice == "report":
        coffee_maker.report()
        money.report()
    else:
        if coffee_maker.is_resource_sufficient(choices[user_choice]):
            if money.make_payment(choices[user_choice].cost):
                coffee_maker.make_coffee(choices[user_choice])

    time.sleep(3)
    os.system("clear")
