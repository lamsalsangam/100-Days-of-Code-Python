from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()
is_off = True
while is_off:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        is_off = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
