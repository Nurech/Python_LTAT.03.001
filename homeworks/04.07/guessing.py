# 1. Use most optimal stategy for winning fast
# http://datagenetics.com/blog/april12012/index.html
# based on  corncob_caps.txt analyze to dermine most optimal order for the list


# 2. Use most optimal stategy time space compelxy, maybe bitwise operations
# max O(n)?, for each letter one operation

from collections import defaultdict

letter_counts = defaultdict(int)
with open("corncob_caps.txt") as file:
    for line in file:
        word = line.strip().upper()
        for letter in word:
            if letter not in ["-"]:
                letter_counts[letter] += 1
optimal_order = sorted(letter_counts.keys(), key=lambda letter: -letter_counts[letter])


# print(optimal_order)

def start():
    optimal_order = ["E", "S", "I", "A", "R", "N", "T", "O", "L", "C", "D", "U", "P", "M", "G", "H", "B", "Y", "F", "V", "K", "W", "Z", "X",
                     "Q", "J", ]
    used = optimal_order.copy()
    solved = False
    global hint
    guess = ""
    length = 0

    while not solved:

        hint = ask_hint()
        guess = list(hint)
        length = len(hint)

        if "_" not in hint:
            break

        for i in range(length):

            if hint[i] == "_":
                for letter in used:
                    if letter not in guess:
                        used.remove(letter)
                        print(letter)
                        break
                    break
                break

            if hint[i] in used:
                used.remove(hint[i])

            if hint[i] != "_":
                guess[i] = hint[i]

        # print("".join(guess))


def ask_hint():
    res = input()
    return res


start()
