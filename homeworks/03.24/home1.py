def calculate_prices(prices, percent):
    marked_up_prices = [price * (1 + percent / 100) for price in prices]
    # 1.2 - 20% VAT
    new_arr = [price * 1.2 for price in marked_up_prices]
    return new_arr

prices = [100.0, 1200.0]
percent = 10.0
print(calculate_prices(prices, percent))
