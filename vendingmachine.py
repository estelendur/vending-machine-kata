class VendingMachine:

    inserted = []

    def __init__(self):
        self.inserted = []

    def display(self):
        if len(self.inserted) == 0:
            return 'INSERT COIN'
        else:
            return self.total_inserted()

    def insert_coin(self, coin):
        self.inserted.append(coin)

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
