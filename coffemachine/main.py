# machine warehouse
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

INIT_RES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# main functions


def print_report(resources):
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: '
          f'{resources["coffee"]}g\nMoney: ${resources["money"]}')


def check_input(order_input, resources):
    if order_input == 'off':
        return False
    elif order_input == 'report':
        print_report(resources)
    elif order_input in list(MENU.keys()):
        if check_resources(resources, order_input) and money_check(order_input, resources):
            reduce_res(order_input, resources)
            print(f'Here is your {order_input}, enjoy!')
    return True


def check_resources(resources, drink):
    for r in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][r] > resources[r]:
            print(f'Sorry there is not enough {r}')
            return False
        else:
            return True


def coin_insert():
    total = 0
    coins = {
        'quarter': 0.25,
        'dime': 0.1,
        'nickel': 0.05,
        'penny': 0.01
    }
    print('Insert coins')
    for coin in coins:
        total += round((int(input(f'Insert count of {coin}: ')) * coins[coin]), 2)
    return total


def money_check(drink, res):
    total = coin_insert()
    price = MENU[drink]['cost']
    if price > total:
        print('Sorry, not enough money, money refund...')
        return False
    elif price < total:
        res['money'] += price
        print(f'Here is ${(total-price):.2f} dollars in change')
        # print_report(res)
    else:
        res['money'] += price
        # print_report(res)
    return True


def reduce_res(drink_type, resources):
    for res in MENU[drink_type]['ingredients']:
        resources[res] -= MENU[drink_type]['ingredients'][res]


def machine_working():
    """init function with while"""
    on = True
    resource = INIT_RES
    while on:
        order = input('What would you like? espresso/latte/cappuccino: ').lower()
        on = check_input(order, resource)


# init
machine_working()
