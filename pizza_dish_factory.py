from pizza import Pizza
from calzone import Calzone

class PizzaDishFactory():
    def createPizzaDish(self, pizzaDishType):
        if(pizzaDishType == "P"):
            return Pizza()
        if(pizzaDishType == "C"):
            return Calzone()
