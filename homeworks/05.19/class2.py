def max_bottles(money, price, deposit):
    print("value for money: ", money)
    total_price = price + deposit
    bottles = int(money / total_price)
    remaining_money = money % total_price

    if bottles == 0:
        return 0
    else:
        return bottles + max_bottles(bottles * deposit + remaining_money, price, deposit)

money = 7.0
price = 0.27
deposit = 0.10
print("Juku can buy", max_bottles(money, price, deposit), "bottles.")
