import unittest
from vendingmachine import VendingMachine

class TestVendingMachine(unittest.TestCase):

    def test_display_initially_shows_insert_coins(self):
        vend = VendingMachine()
        self.assertEqual("INSERT COIN", vend.display())

if __name__ == '__main__':
    unittest.main()
