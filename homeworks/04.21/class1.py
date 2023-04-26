def read_file(filename):
    result = {}
    with open(filename, "r") as f:
        for line in f:
            name, price, color = line.strip().split(", ")
            if name not in result:
                result[name] = {}
            result[name][color] = float(price)
    return result


def print_products(products):
    for name, colors in products.items():
        for color, price in colors.items():
            print(f"{name} - {price}€ ({color})")


def main():
    products = read_file("pricelist.txt")
    print("The store has the following products:")
    print_products(products)

    subtotal = 0
    while True:
        product_name = input("Enter product name: ")
        if not product_name:
            break

        if product_name in products:
            product_color = input("Enter product color: ")
            if product_color in products[product_name]:
                subtotal += products[product_name][product_color]
                print(f"The current subtotal is {subtotal:.1f}€.")
            else:
                print("There is no product of this color.")
        else:
            print("There is no product with this name.")

    print(f"You have to pay {subtotal:.1f}€.")


if __name__ == "__main__":
    main()
