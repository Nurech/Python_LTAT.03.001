def car_price(price, years):
    if years == 0:
        return round(price, 2)
    else:
        return car_price(price * 0.8, years - 1)


# print(car_price(8000.0, 5))
