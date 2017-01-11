class VendingMachine:

    def __init__(self):
        self.inserted = []
        self.returned_coins = []

    def display(self):
        if len(self.inserted) == 0:
            return 'INSERT COIN'
        else:
            return self.total_inserted()

    def return_coins(self, coin = "none"):
        if (coin == "none"):
            self.returned_coins = self.inserted
            self.inserted = []
        else:
            self.returned_coins.append(coin)

    def insert_coin(self, coin):
        if (len(coin) in [4, 6, 7]):
            self.inserted.append(coin)
        else:
            self.return_coins(coin)

    def total_inserted(self):
        total = 0.0
        for item in self.inserted:
            if len(item) == 4:
                total += 0.10
            elif len(item) == 6:
                total += 0.05
            elif len(item) == 7:
                total += 0.25
        return '%.2f' % total
