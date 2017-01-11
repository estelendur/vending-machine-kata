import unittest
from vendingmachine import *

class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vend = VendingMachine()
        for product in ["chips", "candy", "cola"]:
            self.vend.set_stock(product, 5)

    def test_display_initially_shows_insert_coins(self):
        self.assertEqual("INSERT COIN", self.vend.display())

    def test_machine_accepts_dime(self):
        self.vend.insert_coin("dime")
        self.assertEqual("0.10", self.vend.display())

    def test_machine_shows_total_inserted_money(self):
        self.vend.insert_coin("dime")
        self.vend.insert_coin("nickel")
        self.assertEqual("0.15", self.vend.display())
        self.vend.insert_coin("quarter")
        self.assertEqual("0.40", self.vend.display())

    def test_machine_rejects_penny(self):
          self.vend.insert_coin("penny")
          self.assertEqual("INSERT COIN", self.vend.display())
          self.assertEqual(["penny"], self.vend.returned_coins)

    def test_machine_does_not_drop_valid_coins_when_penny_inserted(self):
        self.vend.insert_coin("dime")
        self.vend.insert_coin("penny")
        self.assertEqual(["penny"], self.vend.returned_coins)
        self.assertEqual(["dime"], self.vend.inserted_coins)

    def test_machine_returns_coins_when_return_button_is_pressed(self):
        self.vend.insert_coin("nickel")
        self.vend.insert_coin("quarter")
        self.vend.return_coins()
        self.assertEqual(["nickel", "quarter"], self.vend.returned_coins)
        self.assertEqual([], self.vend.inserted_coins)

    def test_machine_dispenses_cola_when_one_dollar_is_inserted(self):
        for i in range(0,4):
            self.vend.insert_coin("quarter")
        self.assertEqual("cola", self.vend.dispense("cola"))
        self.assertEqual(0.0, self.vend.total_inserted_coins())
        self.assertEqual("THANK YOU", self.vend.display())
        self.assertEqual("INSERT COIN", self.vend.display())

    def test_machine_displays_price_when_insufficient_money_is_inserted(self):
        self.assertEqual("", self.vend.dispense("chips"))
        self.assertEqual("PRICE 0.50", self.vend.display())
        self.assertEqual("INSERT COIN", self.vend.display())

    def test_cola_costs_a_dollar(self):
        for i in range(0, 3):
            self.vend.insert_coin("quarter")
        self.assertEqual("", self.vend.dispense("cola"))
        self.assertEqual("PRICE 1.00", self.vend.display())
        self.assertEqual("0.75", self.vend.display())

    def test_candy_costs_sixty_five_cents(self):
        self.assertEqual("", self.vend.dispense("candy"))
        self.assertEqual("PRICE 0.65", self.vend.display())

    def test_machine_returns_change_when_extra_money_inserted(self):
        for i in range(0, 3):
            self.vend.insert_coin("quarter")
        self.assertEqual("candy", self.vend.dispense("candy"))
        self.assertEqual(["dime"], self.vend.returned_coins)

    def test_machine_returns_40_cents_when_90_given_for_chips(self):
        for coin in ["quarter", "quarter", "dime", "quarter", "nickel"]:
            self.vend.insert_coin(coin)
        self.assertEqual("chips", self.vend.dispense("chips"))
        self.assertEqual(["quarter", "dime", "nickel"], self.vend.returned_coins)

    def test_machine_displays_soldout_when_sold_out(self):
        self.vend.set_stock("chips", 1)
        for coin in ["quarter", "quarter"]:
            self.vend.insert_coin(coin)
        self.assertEqual("chips", self.vend.dispense("chips"))
        self.assertEqual("", self.vend.dispense("chips"))
        self.assertEqual("SOLD OUT", self.vend.display())
        self.assertEqual("INSERT COIN", self.vend.display())


if __name__ == '__main__':
    unittest.main()
