from art import logo
import data

print(logo)
print("!!!!Welcome to the coffee machine!!!!")

resources = data.resources
resources_measure = data.resources_measure
profit = data.profit
MENU = data.MENU
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True if the order can be made and False if the ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from the coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quaters?: "))*0.25
    total += int(input("how many dime?: "))*0.1
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if the payment is accepted, False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enought money. Money refunded.")
    return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients form the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}👌☕")


while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        for i in resources:
            print(f"{i.capitalize()}: {resources[i]}{resources_measure[i]}")
        print(f"Money: $ {profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            paymmnet = process_coins()
            if is_transaction_successful(paymmnet, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
