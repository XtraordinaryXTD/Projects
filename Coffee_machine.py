MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(ingredients):
    """Checks if the machine has enough resources"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f'Sorry there are not enough {item}')
            return False
    return True


def check_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_payment(coins_received, drink_cost):
    """Checks if there are enough coins inserted into the machine"""
    if coins_received > drink_cost:
        change = round(drink_cost - coins_received, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f'Sorry there is not enough coins, here is your change money back.')
        return False


def make_coffee(drink_name, order_ingredients):
    """deducts ingredients to make a coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕, enjoy!')


is_on = True


while is_on:
    choice = input('What kind of coffee would you like? (espresso $1.50 /latte $2.50 /cappuccino $3.00): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = check_coins()
            if check_payment(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
