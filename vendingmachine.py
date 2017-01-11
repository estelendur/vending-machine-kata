class VendingMachine:

    def __init__(self):
        self.inserted_coins = []
        self.returned_coins = []
        self.dispensed = False
        self.total_needed = 0

    def display(self):
        if (self.total_needed > 0):
            answer = "PRICE " + ('%.2f' % (self.total_needed / 100.0))
            self.total_needed = 0
            return answer
        if (self.dispensed):
            self.dispensed = False
            return "THANK YOU"
        elif len(self.inserted_coins) == 0:
            return "INSERT COIN"
        else:
            return '%.2f' % (self.total_inserted_coins() / 100.0)

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
        if self.total_inserted_coins() > self.price(product):
            self.dispense_change(product)
        if self.total_inserted_coins() >= self.price(product):
            self.inserted_coins = []
            self.dispensed = True
            return product
        else:
            self.total_needed = self.price(product)
            return ""
