import argparse
from pizza import Pizza
from calzone import Calzone
from pizza_dish_factory import PizzaDishFactory

def main():
    """ Execute the program """
    args = parse_args()
    pizzaOption = args.type

    factory = PizzaDishFactory()
    thePizzaDish = factory.createPizzaDish(pizzaOption)
    doStuffPizzaDish(thePizzaDish)

def doStuffPizzaDish(pizzaDish):
    pizzaDish.makePizzaDish()
    pizzaDish.cookPizzaDish()
    pizzaDish.boxPizzaDish()

def parse_args():
    """ Parse input arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--type",
        help="What type of pizza dish? (P / C)",
        required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()
