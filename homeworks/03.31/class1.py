# def name_and_price(string):
#     one, two, three = string.split(";")
#     print([one, float(three)])
#     return [one, float(three)]

def name_and_price():
    min = input("Enter the minimum price: ") or 5
    max = input("Enter the maximum price: ") or 10
    print("The following presents lie in that price range:")
    with open("presents.txt", "r") as file:
        for line in file:
            one, two, three = line.split(";")
            if float(three) >= float(min) and float(three) <= float(max):
                print(one)

name_and_price()
