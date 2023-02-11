import math

# name = input("What is your name? ")
# print("It's been ages since I've seen you, " + name)


pizza_size = float(input("What is the diameter of your pizza? "))
pizza_cost = float(input("How many euros does it cost? "))

pizza_square_cm = (pizza_size / 2) ** 2 * math.pi
square_cm_price = pizza_cost / pizza_size

print("One square cm of your pizza costs " + str(square_cm_price) + " cents.")
