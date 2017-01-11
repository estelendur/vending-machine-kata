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
        self.vend.insert_coin("quarter")
        self.assertEqual("0.40", self.vend.display())

    def test_machine_rejects_penny(self):
          self.vend.insert_coin("penny")
          self.assertEqual("INSERT COIN", self.vend.display())
          self.assertEqual(["penny"], self.vend.returned_coins)

if __name__ == '__main__':
    unittest.main()
