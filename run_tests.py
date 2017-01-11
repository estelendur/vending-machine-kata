import unittest
from vendingmachine import *

class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vend = VendingMachine()

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

if __name__ == '__main__':
    unittest.main()
