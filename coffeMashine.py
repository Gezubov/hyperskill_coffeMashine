supplies = {"water": 1200, "milk": 540, "beans": 120, "cups": 9, "money": 550}

def stats():
    print(f"""The coffee machine has:
    {supplies["water"]} of water
    {supplies["milk"]} of milk
    {supplies["beans"]} of coffee beans
    {supplies["cups"]} of disposable cups
    {supplies["money"]} of money""")

def espresso():
    supplies["water"] -= 250
    supplies["beans"] -= 16
    supplies["money"] += 4
    supplies["cups"] -= 1

def latte():
    supplies["water"] -= 350
    supplies["milk"] -= 75
    supplies["beans"] -= 20
    supplies["money"] += 7
    supplies["cups"] -= 1

def cappuchino():
    supplies["water"] -= 200
    supplies["milk"] -= 100
    supplies["beans"] -= 12
    supplies["money"] += 6
    supplies["cups"] -= 1

def buy():
    coffeeChoice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    if coffeeChoice == 1:
        espresso()
    if coffeeChoice == 2:
        latte()
    if coffeeChoice == 3:
        cappuchino()

def fill():
    supplies["water"] += int(input("How many ml of water do you want to add:\n"))
    supplies["milk"] += int(input("How many ml of milk do you want to add:\n"))
    supplies["beans"] += int(input("How many grams of coffee beans do you want to add:\n"))
    supplies["cups"] += int(input("How many disposable cups of coffee do you want to add:\n"))

def take():
    print(f'I gave you ${supplies["money"]}')
    supplies["money"] = 0

def coffeMachine():
    stats()
    action = input("Write action (buy, fill, take):\n")
    if action == "buy":
        buy()
    if action == "fill":
        fill()
    if action == "take":
        take()
    stats()

coffeMachine()
