class VendingMachine:

    def __init__(self):
        self.inserted_coins = []
        self.returned_coins = []
        self.dispensed = False
        self.total_needed = 0
        self.chips_stock = 0
        self.candy_stock = 0
        self.cola_stock = 0
        self.soldout = False
        self.quarters = 0
        self.dimes = 0
        self.nickels = 0

    def display(self):
        if (self.dispensed):
            self.dispensed = False
            if (self.soldout):
                self.soldout = False
            return "THANK YOU"
        if self.can_make_change():
            if (self.soldout):
                self.soldout = False
                if (self.dispensed):
                    self.dispensed = False
                return "SOLD OUT"
            elif (self.total_needed > 0):
                answer = "PRICE " + ('%.2f' % (self.total_needed / 100.0))
                self.total_needed = 0
                return answer
            elif len(self.inserted_coins) == 0:
                return "INSERT COIN"
            else:
                return '%.2f' % (self.total_inserted_coins() / 100.0)
        else:
            return "EXACT CHANGE ONLY"

    def price(self, product):
        if (product == "chips"):
            return 50
        elif (product == "cola"):
            return 100
        elif (product == "candy"):
            return 65

    def return_coins(self, coin = "none"):
        if (coin == "none"):
            self.returned_coins = self.inserted_coins
            for coin in self.inserted_coins:
                self.remove_coin(coin)
            self.inserted_coins = []
        else:
            self.returned_coins.append(coin)

    def insert_coin(self, coin):
        if (len(coin) in [4, 6, 7]):
            self.inserted_coins.append(coin)
            self.add_coin(coin)
        else:
            self.return_coins(coin)

    def total_inserted_coins(self):
        total = 0
        for item in self.inserted_coins:
            if len(item) == 4:
                total += 10
            elif len(item) == 6:
                total += 5
            elif len(item) == 7:
                total += 25
        return total

    def dispense_change(self, product):
        change = self.total_inserted_coins() - self.price(product)
        while change >= 25:
            self.returned_coins.append("quarter")
            self.remove_coin("quarter")
            change -= 25
        while change >= 10:
            self.returned_coins.append("dime")
            self.remove_coin("dime")
            change -= 10
        if change >= 5:
            self.returned_coins.append("nickel")
            self.remove_coin("nickel")

    def dispense(self, product):
        if self.dispensed:
            self.dispensed = False
        if self.get_stock(product) == 0:
            self.soldout = True
            return ""
        if self.total_inserted_coins() > self.price(product):
            self.dispense_change(product)
        if self.total_inserted_coins() >= self.price(product):
            self.inserted_coins = []
            self.dispensed = True
            self.set_stock(product, self.get_stock(product) - 1)
            return product
        elif self.total_inserted_coins() < self.price(product):
            self.total_needed = self.price(product)
        return ""

    def get_stock(self, product):
        if product == "cola":
            return self.cola_stock
        elif product == "chips":
            return self.chips_stock
        elif product == "candy":
            return self.candy_stock

    def set_stock(self, product, quantity):
        if product == "cola":
            self.cola_stock = quantity
        elif product == "chips":
            self.chips_stock = quantity
        elif product == "candy":
            self.candy_stock = quantity

    def empty_coins(self):
        self.quarters = 0
        self.dimes = 0
        self.nickels = 0

    def can_make_change(self):
        # Exhaustive testing suggests that if we have a dime and a nickel,
        # it is possible to make change for any product given any valid input
        return (self.dimes > 0) & (self.nickels > 0)

    def add_coin(self, coin):
        if (len(coin) == 4):
            self.dimes += 1
        elif (len(coin) == 6):
            self.nickels += 1
        elif (len(coin) == 7):
            self.quarters += 1

    def remove_coin(self, coin):
        if (len(coin) == 4):
            self.dimes -= 1
        elif (len(coin) == 6):
            self.nickels -= 1
        elif (len(coin) == 7):
            self.quarters -= 1
