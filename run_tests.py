import unittest
from vendingmachine import *

class TestVendingMachine(unittest.TestCase):

    def test_display_initially_shows_insert_coins(self):
        vend = VendingMachine()
        self.assertEqual("INSERT COIN", vend.display())

    def test_machine_accepts_dime(self):
        vend = VendingMachine()
        vend.insert_coin("dime")
        self.assertEqual("0.10", vend.display())

    def test_machine_shows_total_inserted_money(self):
        vend = VendingMachine()
        vend.insert_coin("dime")
        vend.insert_coin("nickel")
        vend.insert_coin("quarter")
        self.assertEqual("0.40", vend.display())

    def test_machine_rejects_penny(self):
          vend = VendingMachine()
          vend.insert_coin("penny")
          self.assertEqual("INSERT COIN", vend.display())
          self.assertEqual(["penny"], vend.returned_coins)

if __name__ == '__main__':
    unittest.main()
