# TODO todo no 1 print a report for all coffee resources
Menu = {
        "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            },
            "cost":1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost":2.5,
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

def is_resource_sufficient(order_ingredients):
    """Returns True if the ingredients are sufficient. False otherwise."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarter?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Returns True if the money received and sufficient is successful. If money is insufficient return the cash."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is  ${change} in change.")
        global profit
        profit += drink_cost

        return True
    else:
        print(f"Sorry, not enough {money_recieved}. Money Refunded {money_recieved}.")
        return False
is_on = True

def make_coffee(drink_name, order_ingredients):
    global is_on
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's a coffee for {drink_name}. 🍵☕"),


while is_on:
    choice = input("what would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml " ),
        print(f"Milk: {resources['milk']}ml"),
        print(f"Coffee: {resources['coffee']}gm"),
        print(f"Money: ${profit}"),
    else:
        drink = Menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
