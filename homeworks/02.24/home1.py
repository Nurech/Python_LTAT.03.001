# A bakery produces three types of cakes: chocolate cakes (0.05 €/cm2), strawberry cakes (0.04 €/cm2),
# and Napoleon cakes (0.08 €/cm2). Write a function called cake_price, which takes cake name and cake size as
# parameters and returns the price of the cake in euros, rounded to two decimal digits. Chocolate cake and
# strawberry cake are round and their sizes are entered as radius. Napoleon cake is square-shaped and
# its size is entered as a side length. If the cake type is something else, then the function should return -1.
#
# >>> cake_price('Napoleon cake', 10)
# 8.0
# >>> cake_price('chocolate cake', 5)
# 3.93
# >>> cake_price('bisquit cake', 10)
# -1
#
# Cake names are 'chocolate cake', 'strawberry cake' or 'Napoleon cake'. Size is given in centimeters.

import math


def cake_price(type, size):
    price_cm = 0
    if type == 'chocolate cake':
        price_cm = 0.05
        return round(math.pi * (size * size) * price_cm, 2)
    elif type == 'strawberry cake':
        price_cm = 0.04
        return round(math.pi  * (size * size) * price_cm, 2)
    elif type == 'Napoleon cake':
        price_cm = 0.08
        return round((size * size) * price_cm, 2)
    else:
        return -1
