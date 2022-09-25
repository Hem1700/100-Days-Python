from resources import MENU, resources

profit = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")


def check_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print("Sorry, there is not enough ingridients")
            return False
    return True


def process_coins():
    print("Please enter coins: ")
    total = int(input('How many quaters? ')) * 0.25
    total += int(input('How many dimes? ')) * 0.1
    total += int(input('How many nickles? ')) * 0.05
    total += int(input('How many cents? ')) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is your change ${change}")
        global  profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True


while is_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == 'off':
        is_on = False
    elif coffee == 'report':
        report()
    else:
        drink = MENU[coffee]

    check_sufficient(drink["ingredients"])
    payment = process_coins()
    if transaction_successful(payment, drink["cost"]):
        make_coffee(coffee, drink["ingredients"])





