class PizzaDish():
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getSize(self):
        return self._size

    def setSize(self, size):
        self._size = size

    def makePizzaDish(self):
        print(self.getSize() + " " + self.getName() + " is being made")

    def cookPizzaDish(self):
        print(self.getName() + " is being cooked")

    def boxPizzaDish(self):
        print(self.getName() + " is being boxed")
