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

    def display(self):
        if self.can_make_change():
            if (self.soldout):
                self.soldout = False
                if (self.dispensed):
                    self.dispensed = False
                return "SOLD OUT"
            elif (self.dispensed):
                self.dispensed = False
                if (self.soldout):
                    self.soldout = False
                return "THANK YOU"
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
            self.inserted_coins = []
        else:
            self.returned_coins.append(coin)

    def insert_coin(self, coin):
        if (len(coin) in [4, 6, 7]):
            self.inserted_coins.append(coin)
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
            change -= 25
        while change >= 10:
            self.returned_coins.append("dime")
            change -= 10
        if change >= 5:
            self.returned_coins.append("nickel")

    def dispense(self, product):
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
        pass

    def can_make_change(self):
        return True
