# 1. Shopping (1/4) Tom went shopping. He wrote the prices of all items he purchased in the file prices.txt, where each line contains the
# price of one item:
#
# 3.25
# 1.56
# 3
# 8.99
# 0.52
# Write a program that reads the data from the file prices.txt and computes the total price of all items.
#
# For example, in the case of the file above, the program should output:
#
# The total price of all purchased items is 17.32.

total_price = 0
total_items = 0

with open('prices.txt') as prices, open('shopping.txt', 'w') as shopping_file:
    for line in prices:
        try:
            total_price += float(line)
            total_items += 1
        except ValueError:
            pass

    shopping_file.write(f'The total number of items is {total_items}, with a total price of {total_price:.2f}.')
