# 2. Product
# Write a program that prompts the user for a positive integer n and prints out the value of the expression
#
# 2⋅21⋅23⋅43⋅45⋅…⋅2n2n−1⋅2n2n+1
#
# Hint. Combine the fractions in the product into pairs.
#
# Enter n: 1
# The product is 2.6666666666666665
#
# Enter n: 2
# The product is 2.844444444444444
#
# Test your program with an increasing set of inputs. Think yourself: what value does this product approach to, as n increases?


n = int(input('num: '))
product = 2


def first(num):
    return (2 * num) / ((2 * num) - 1)


def second(num):
    return (2 * num) / ((2 * num) + 1)


for k in range(1, n + 1):
    product *= first(k)
    product *= second(k)

print("The product is", product)
