""" Sample problem featuring the factory pattern. """

import unittest

from test_context import Calzone
from test_context import Pizza
from test_context import PizzaDishFactory

class TestPizzaDishFactory(unittest.TestCase):
    """ Tests the PizzaDishFactory class """

    def test_init(self):
        """ Tests the constructor of the PizzaDishFactory class """
        factory = PizzaDishFactory()
        calzone = factory.createPizzaDish("C")
        self.assertEqual(calzone.getName(), "calzone")
        pizza = factory.createPizzaDish("P")
        self.assertEqual(pizza.getName(), "pizza")

if __name__ == '__main__':
    unittest.main()
