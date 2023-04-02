from collections import Counter
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

    return matching_words


def letters(possible_words, hint, offered_letters, optimal_order):
    letter_counts = Counter("".join(possible_words))
    for letter in hint:
        if letter in letter_counts:
            del letter_counts[letter]

    for letter in offered_letters.get(hint, []):
        if letter in letter_counts:
            del letter_counts[letter]

    if letter_counts:
        for letter in optimal_order:
            if letter in letter_counts:
                if hint not in offered_letters:
                    offered_letters[hint] = []
                offered_letters[hint].append(letter)
                return letter
    return None



def next(words, hint, offered_letters, optimal_order):
    possible_words = get(words, hint)
    # print(possible_words)

    if len(possible_words) == 1:
        # print(possible_words[0])
        return possible_words[0]
    elif possible_words:
        return letters(possible_words, hint, offered_letters, optimal_order)
    else:
        return None


def start(words):
    hint = "_"
    offered_letters = {}

    # http://datagenetics.com/blog/april12012/index.html

    optimal_order = ["E", "S", "I", "A", "R", "N", "T", "O", "L", "C", "D", "U", "P", "M", "G", "H", "B", "Y", "F", "V", "K", "W", "Z", "X", "Q", "J", ]

    while "_" in hint:
        hint = input()
        hint = hint.upper()

        if "_" not in hint:
            print(hint)
            break

        guessed_output = next(words, hint, offered_letters, optimal_order)


        if guessed_output:
            print(guessed_output)
            if "_" not in guessed_output and len(guessed_output) != 1:
                break

my_words = []

with open("corncob_caps.txt", "r") as file:
    for line in file:
        my_words.append(line.strip())

start(my_words)
