def start1():
    optimal_order = ['U', 'M', 'L', 'W', 'I', 'A', 'X', 'J', 'T', 'C', 'O', 'G', 'Z', 'F', 'D', 'Q', 'R', 'K', 'P', 'B', 'S', 'V', 'E', 'Y',
                     'H', 'N']
    used = optimal_order.copy()
    solved = False
    hint = ""
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
            else:
                if hint[i] in used:
                    used.remove(hint[i])
                guess[i] = hint[i]


def ask_hint():
    res = input()
    return res


import re


def get(words, hint):
    hint_pattern = ""
    for letter in hint:
        if letter != "_":
            hint_pattern += letter
        else:
            hint_pattern += "."

    matching_words = []

    for word in words:
        if len(word) == len(hint):
            if re.match(hint_pattern, word):
                matching_words.append(word)

    return matching_words


def next(words, hint):
    possible_words = get(words, hint)
    return possible_words[0] if possible_words else None


def start(words):
    solved = False
    hint = ""

    while not solved:
        hint = ask_hint1()

        if "_" not in hint:
            solved = True
            break

        guessed_word = next(words, hint)
        if guessed_word:
            print(guessed_word)
        else:
            start1()


def ask_hint1():
    res = input()
    return res


with open("corncob_caps.txt", "r") as file:
    content = file.read()
    words = content.strip().split("\n")

start(words)
