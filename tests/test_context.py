""" Sample problem featuring the factory pattern. """

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../factory')))

# pylint: disable=E0401,W0611,C0413
from calzone import Calzone
from pizza import Pizza
from pizza_dish import PizzaDish
from pizza_dish_factory import PizzaDishFactory
