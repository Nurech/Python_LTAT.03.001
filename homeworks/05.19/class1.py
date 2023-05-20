def gold1(n):
    print("value for n: ", n)
    if n == 1:
        return 1
    else:
        return n + gold1(n-1)

# Testing our function
print("gold coins in the safe: ", gold1(10))

def gold2(n):
    print("Testing value for n: ", n)
    if n == 1:
        return 1
    else:
        return (n**2) + gold2(n-1)

print("Total gold coins in the safe: ", gold2(4))

def gold3(n):
    print("value for n: ", n)
    if n == 1:
        return 1
    else:
        return 2 * gold3(n-1) + 1

print("Total gold coins in the safe: ", gold3(3))
