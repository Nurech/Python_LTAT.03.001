import re


def get(words, hint):
    hint_pattern = re.compile("".join(letter if letter != "_" else "." for letter in hint))

    matching_words = []

    for word in words:
        if len(word) == len(hint):
            if hint_pattern.match(word):
                matching_words.append(word)

    return matching_words


def most_common_letter(possible_words, hint, offered_letters):
    letter_counts = {}

    for word in possible_words:
        for letter in word:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1

    for letter in hint:
        if letter in letter_counts:
            del letter_counts[letter]

    for letter in offered_letters.get(hint, []):
        if letter in letter_counts:
            del letter_counts[letter]

    if letter_counts:
        most_common = max(letter_counts, key=letter_counts.get)
        if hint not in offered_letters:
            offered_letters[hint] = []
        offered_letters[hint].append(most_common)
        return most_common
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
