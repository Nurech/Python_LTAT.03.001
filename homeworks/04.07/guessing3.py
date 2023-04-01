import random
import time
from collections import defaultdict

# Load words from corncob_caps.txt
with open("corncob_caps.txt") as file:
    words = [line.strip().upper() for line in file]

# Set testing parameters
test_duration = 2  # Test duration in seconds
max_test_duration = 5  # Maximum total test duration in seconds
test_iterations = 100
max_words_per_test = 10000

# Define the start function
def start(optimal_order, word):
    used = optimal_order.copy()
    solved = False
    hint = "_" * len(word)
    guess = list(hint)

    while not solved:

        for i, letter in enumerate(hint):
            if letter == "_":
                for letter in used:
                    if letter not in guess:
                        used.remove(letter)
                        break
                if letter in word:
                    indices = [i for i, l in enumerate(word) if l == letter]
                    for index in indices:
                        guess[index] = letter
                    hint = "".join(guess)
                break

        if "_" not in hint:
            solved = True

    return solved

# Test the optimal_order
def test_optimal_order(optimal_order, max_words_per_test):
    start_time = time.time()
    solved_words = 0
    words_tested = 0

    while time.time() - start_time < test_duration and words_tested < max_words_per_test:
        word = random.choice(words)
        if start(optimal_order, word):
            solved_words += 1
        words_tested += 1
    return time.time() - start_time

# Define the initial optimal_order
optimal_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Perform tests and shuffle optimal_order
best_order = optimal_order.copy()
best_score = 100

for i in range(test_iterations):
    random.shuffle(optimal_order)
    score = test_optimal_order(optimal_order, max_words_per_test)
    print(f"Iteration {i + 1}: {score} words solved")
    print(optimal_order)

    if score < best_score:
        best_score = score
        best_order = optimal_order.copy()

print("\nBest order:", best_order)
print("Best score:", best_score)
