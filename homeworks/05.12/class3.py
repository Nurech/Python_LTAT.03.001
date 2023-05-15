class Produc:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class BonusCard:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_bonus(self):
        # print(self.products)
        bonus = sum([product.price * 0.05 for product in self.products if product.price >= 10])
        return round(bonus, 2)


class GoldCard(BonusCard):
    def calculate_bonus(self):
        bonus = super().calculate_bonus()
        return round(bonus * 1.5, 2)


def main():
    card_type = input("Do you want a bonus card or a gold card (B/G)? ")
    if card_type.upper() == "B":
        card = BonusCard()
    else:
        card = GoldCard()

    while True:
        action = input("What do you want to do: add product, calculate bonus, exit (A/C/E)? ")
        if action.upper() == "A":
            product_name = input("Enter the product name: ")
            product_price = float(input("Enter the price of the product: "))
            product = Produc(product_name, product_price)
            card.add_product(product)
        elif action.upper() == "C":
            print(f"Your bonus is {card.calculate_bonus()} euros.")
        elif action.upper() == "E":
            break
        else:
            print("Invalid action, please try again.")


main()
