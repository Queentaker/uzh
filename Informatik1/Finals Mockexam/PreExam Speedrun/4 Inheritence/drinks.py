#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

from abc import ABC, abstractmethod
import unittest

class Product(ABC):

    @abstractmethod
    def get_price(self):
        pass

class Bottle(Product):
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def get_price(self):
        return self.price

class Crate(Product):
    def __init__(self):
        self.__bottles = []

    def add(self, bottles):
        if len(self.__bottles) == 20:
            raise RuntimeError
        self.__bottles.append(bottles)

    def get_price(self):
        price = 0
        for f in self.__bottles:
            price += f.get_price()
        return price

    def get_size(self):
        return len(self.__bottles)

class DiscountCrate(Crate):
    def get_price(self):
        price = super().get_price()
        nbottles = self.get_size()
        percent_off = 2 * nbottles
        if percent_off > 25: percent_off = 25
        price -= (percent_off/100) * price
        return round(price, 2)


class FixedPriceCrate(Crate):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def get_price(self):
        return self.price


class ShopTestSuite(unittest.TestCase):

    def test_crate_add(self):
        c = Crate()
        c.add(Bottle(4.50, "Light Beer"))
        self.assertEqual(c.get_size(), 1)

    def test_crate_max_size(self):
        c = Crate()
        with self.assertRaises(RuntimeError):
            for b in range(20+1):
                c.add(Bottle(1.0, "Light Beer"))

    def test_crate_price(self):
        c = Crate()
        bottles = 5 * [Bottle(4.00, "Strong Stuff")]
        for b in bottles:
            c.add(b)
        self.assertEqual(c.get_price(), 20)

    def test_discount_crate_price(self):
        c = DiscountCrate()
        bottles = 5 * [Bottle(4.00, "Strong Stuff")]
        for b in bottles:
            c.add(b)
        self.assertEqual(c.get_price(), 18.00)


#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
if __name__ == '__main__':
    bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
    assert(bottles[0].get_price() == 3.50)

    c = Crate()
    for b in bottles: c.add(b)
    assert(c.get_size() == 5)
    assert(c.get_price() == 20.00)

    c = FixedPriceCrate(11.11)
    for b in bottles: c.add(b)
    assert(c.get_price() == 11.11)

    c = DiscountCrate()
    for b in bottles: c.add(b)
    assert(c.get_price() == 18.00)

    unittest.main()
