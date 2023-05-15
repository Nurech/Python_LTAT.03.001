import math

# 1
class Cake:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def area(self):
        return self.size ** 2

    def cm2price(self):
        price_per_cm2 = (self.price / self.area()) * 100
        # print(self.price, self.area(), price_per_cm2)
        return round(price_per_cm2, 2)


c1 = Cake("Blueberry cake", 8, 3.52)
print(c1.area())
print(c1.cm2price())

# 2
class Round_cake(Cake):
    def __init__(self, name, size, price):
        super().__init__(name, size, price)

    def area(self):
        radius = self.size / 2
        # print(self.size, radius)
        return math.pi * radius ** 2

    def cm2price(self):
        price_per_cm2 = (self.price / self.area()) * 100  # Convert to cents
        return round(price_per_cm2, 2)


c2 = Round_cake("Carrot-pumpkin pizza base", 24, 1.85)
print(c2.area())
print(c2.cm2price())


class Pizza(Round_cake):
    def __init__(self, name, size, price, cover_price):
        super().__init__(name, size, price)
        self.cover_price = cover_price

    def cm2price(self):
        total_price = self.price + self.cover_price
        price_per_cm2 = (total_price / self.area()) * 100
        # print(self.price, self.cover_price, self.area(), price_per_cm2)
        return round(price_per_cm2, 2)


# c3 = Pizza("here", 1, 1, 1)
c3 = Pizza("Caesar Pizza", 24, 1.85, 6.70)
print(c3.area())
print(c3.cm2price())
