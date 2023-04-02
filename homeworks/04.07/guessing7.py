import re

def get(words, hint):
    hint_pattern_str = "".join(letter if letter != "_" else "." for letter in hint)
    hint_pattern = re.compile(hint_pattern_str)

    matching_words = []
    for word in words:
        if len(word) == len(hint) and hint_pattern.match(word):
            matching_words.append(word)

    return matching_words


def next_guess(words, hint, guessed_letters):
    letter_counts = {}
    for word in words:
        for letter in word:
            if letter not in guessed_letters:
                if letter not in letter_counts:
                    letter_counts[letter] = 0
                letter_counts[letter] += 1

    if not letter_counts:
        return None

    best_letter = max(letter_counts, key=letter_counts.get)
    guessed_letters.add(best_letter)

    if len(words) == 1:
        return words[0]
    return best_letter

def start(words):
    hint = "_"
    guessed_letters = set()

    while "_" in hint:
        hint = input().upper()

        if "_" not in hint:
            print(hint)
            break

        possible_words = get(words, hint)
        guess = next_guess(possible_words, hint, guessed_letters)

        if guess:
            print(guess)
            if "_" not in guess and len(guess) != 1:
                break

my_words = []

with open("corncob_caps.txt", "r") as file:
    my_words = [line.strip() for line in file]

start(my_words)
