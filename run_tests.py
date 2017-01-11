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

if __name__ == '__main__':
    unittest.main()
