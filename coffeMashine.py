supplies = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}
espresso = {"water": 250, "milk": 0, "beans": 16, "cups": 1, "money": 4}
latte = {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7}
cappuchino = {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}

def remaining():
    print(f"""The coffee machine has:
    {supplies["water"]} of water
    {supplies["milk"]} of milk
    {supplies["beans"]} of coffee beans
    {supplies["cups"]} of disposable cups
    {supplies["money"]} of money""")

def makingCoffee(recepie):
    if supplies["water"] < recepie["water"]:
        print("Sorry, not enough water")
    elif supplies["milk"] < recepie["milk"]:
        print("Sorry, not enough milk")
    elif supplies["beans"] < recepie["beans"]:
        print("Sorry, not enough beans")
    elif supplies["cups"] < recepie["cups"]:
        print("Sorry, not enough disposable cups")
    else:
        print("I have enough resources, making you a coffee!")
        supplies["water"] -= recepie["water"]
        supplies["milk"] -= recepie["milk"]
        supplies["beans"] -= recepie["beans"]
        supplies["money"] += recepie["money"]
        supplies["cups"] -= recepie["cups"]

def buy():
    while True:
        coffeeChoice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffeeChoice == "back":
            break
        if coffeeChoice == "1":
            makingCoffee(espresso)
            break
        if coffeeChoice == "2":
            makingCoffee(latte)
            break
        if coffeeChoice == "3":
            makingCoffee(cappuchino)
            break

def fill():
    supplies["water"] += int(input("How many ml of water do you want to add:\n"))
    supplies["milk"] += int(input("How many ml of milk do you want to add:\n"))
    supplies["beans"] += int(input("How many grams of coffee beans do you want to add:\n"))
    supplies["cups"] += int(input("How many disposable cups do you want to add:\n"))

def take():
    print(f'I gave you ${supplies["money"]}')
    supplies["money"] = 0

def coffeMachine():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "exit":
            break
        if action == "remaining":
            remaining()
        if action == "buy":
            buy()
        if action == "fill":
            fill()
        if action == "take":
            take()

coffeMachine()
