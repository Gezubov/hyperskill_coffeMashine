class CoffeeMachine:
    supplies = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}
    espresso = {"water": 250, "milk": 0, "beans": 16, "cups": 1, "money": 4}
    latte = {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7}
    cappuchino = {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}
    def __init__(self):
        while True:
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")
            if self.action == "exit":
                break
            if self.action == "remaining":
                self.remaining()
            if self.action == "buy":
                self.buy()
            if self.action == "fill":
                self.fill()
            if self.action == "take":
                self.take()

                


    def remaining(self):
        print(f"""The coffee machine has:
        {self.supplies["water"]} of water
        {self.supplies["milk"]} of milk
        {self.supplies["beans"]} of coffee beans
        {self.supplies["cups"]} of disposable cups
        {self.supplies["money"]} of money""")

    def makingCoffee(self,recepie):
        if self.supplies["water"] < recepie["water"]:
            print("Sorry, not enough water")
        elif self.supplies["milk"] < recepie["milk"]:
            print("Sorry, not enough milk")
        elif self.supplies["beans"] < recepie["beans"]:
            print("Sorry, not enough beans")
        elif self.supplies["cups"] < recepie["cups"]:
            print("Sorry, not enough disposable cups")
        else:
            print("I have enough resources, making you a coffee!")
            self.supplies["water"] -= recepie["water"]
            self.supplies["milk"] -= recepie["milk"]
            self.supplies["beans"] -= recepie["beans"]
            self.supplies["money"] += recepie["money"]
            self.supplies["cups"] -= recepie["cups"]

    def buy(self):
        while True:
            self.coffeeName = input(
                "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            if self.coffeeName == "back":
                break
            if self.coffeeName == "1":
                self.makingCoffee(self.espresso)
                break
            if self.coffeeName == "2":
                self.makingCoffee(self.latte)
                break
            if self.coffeeName == "3":
                self.makingCoffee(self.cappuccino)
                break

    def fill(self):
        self.supplies["water"] += int(input("How many ml of water do you want to add:\n"))
        self.supplies["milk"] += int(input("How many ml of milk do you want to add:\n"))
        self.supplies["beans"] += int(input("How many grams of coffee beans do you want to add:\n"))
        self.supplies["cups"] += int(input("How many disposable cups do you want to add:\n"))

    def take(self):
        print(f'I gave you ${self.supplies["money"]}')
        self.supplies["money"] = 0
CoffeeMachine()
