class VendingMachine:

    inserted = []

    def display(self):
        if len(self.inserted) == 0:
            return 'INSERT COIN'
        else:
            return "0.10"

    def insert_coin(self, coin):
        self.inserted.append(coin)
