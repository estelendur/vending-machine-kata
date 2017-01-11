import unittest
from vendingmachine import *

class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vend = VendingMachine()
        for product in ["chips", "candy", "cola"]:
            self.vend.set_stock(product, 5)

    def assertDispensed(self, product):
        self.assertEqual(product, self.vend.dispense(product))

    def assertDisplayed(self, string):
        self.assertEqual(string, self.vend.display())

    def test_display_initially_shows_insert_coins(self):
        self.assertDisplayed("INSERT COIN")

    def test_machine_accepts_dime(self):
        self.vend.insert_coin("dime")
        self.assertDisplayed("0.10")

    def test_machine_shows_total_inserted_money(self):
        self.vend.insert_coin("dime")
        self.vend.insert_coin("nickel")
        self.assertDisplayed("0.15")
        self.vend.insert_coin("quarter")
        self.assertDisplayed("0.40")

    def test_machine_rejects_penny(self):
          self.vend.insert_coin("penny")
          self.assertDisplayed("INSERT COIN")
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
        self.assertDispensed("cola")
        self.assertEqual(0.0, self.vend.total_inserted_coins())
        self.assertDisplayed("THANK YOU")
        self.assertDisplayed("INSERT COIN")

    def test_machine_displays_price_when_insufficient_money_is_inserted(self):
        self.assertEqual("", self.vend.dispense("chips"))
        self.assertDisplayed("PRICE 0.50")
        self.assertDisplayed("INSERT COIN")

    def test_cola_costs_a_dollar(self):
        for i in range(0, 3):
            self.vend.insert_coin("quarter")
        self.assertEqual("", self.vend.dispense("cola"))
        self.assertDisplayed("PRICE 1.00")
        self.assertDisplayed("0.75")

    def test_candy_costs_sixty_five_cents(self):
        self.assertEqual("", self.vend.dispense("candy"))
        self.assertDisplayed("PRICE 0.65")

    def test_machine_returns_change_when_extra_money_inserted(self):
        for i in range(0, 3):
            self.vend.insert_coin("quarter")
        self.assertDispensed("candy")
        self.assertEqual(["dime"], self.vend.returned_coins)

    def test_machine_returns_40_cents_when_90_given_for_chips(self):
        for coin in ["quarter", "quarter", "dime", "quarter", "nickel"]:
            self.vend.insert_coin(coin)
        self.assertDispensed("chips")
        self.assertEqual(["quarter", "dime", "nickel"], self.vend.returned_coins)

    def test_machine_displays_soldout_when_sold_out(self):
        self.vend.set_stock("chips", 1)
        for coin in ["quarter", "quarter"]:
            self.vend.insert_coin(coin)
        self.assertDispensed("chips")
        self.assertEqual("", self.vend.dispense("chips"))
        self.assertDisplayed("SOLD OUT")
        self.assertDisplayed("INSERT COIN")

    def test_machine_displays_remaining_money_after_soldout(self):
        self.vend.set_stock("chips", 0)
        self.vend.insert_coin("dime")
        self.assertEqual("", self.vend.dispense("chips"))
        self.assertDisplayed("SOLD OUT")
        self.assertDisplayed("0.10")


if __name__ == '__main__':
    unittest.main()
