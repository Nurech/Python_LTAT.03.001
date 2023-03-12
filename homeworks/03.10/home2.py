
fh = open("prices.txt", "r")

lines = fh.readlines()

for i in range(0, len(lines), 2):
    try:
        name = lines[i].strip()
        price = float(lines[i+1].strip())
        new_price = round(price * 0.9, 2)
        print("New price for {0} is {1} euros.".format(name, new_price))
    except:
        print("Cannot convert the price for {0}.".format(name))

fh.close()
