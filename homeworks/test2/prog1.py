def read_inventory(file):
    inv = {}
    with open(file, "r") as f:
        for l in f:
            code, name, color, pay, condition = l.strip().split("; ")
            if condition == 'good':
                inv[code] = [name, color, float(pay)]
    return inv

def products(products, product_name, max_price):
    check = True
    for code, item in products.items():
        name, color, price = item
        if name == product_name and price <= max_price:
            check = False
            print(code + ' ' + name + ' ' + color  + ' ' + str(price))
    
    if check == True:
        print("No suitable product found.")
        

def main():
    inv = read_inventory("inventory.txt")
    product_name = input("Enter product name: ") or "shirt"
    max_price = float(input("ENter max price: ")) or 10
    products(inv, product_name, max_price)

main()

