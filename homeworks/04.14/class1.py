import random

def gen():
    return (random.randint(0, 5), random.randint(0, 5))


def main():
    secret = gen()
    guesses = 0

    while True:
        x = int(input("Enter the x cord (0-5): "))
        y = int(input("Enter the y cord (0-5): "))

        user_guess = (x, y)
        guesses += 1

        if user_guess == secret:
            print(f"Congratulations! You found the secret point in {guesses} guesses.")
            break
        else:
            print(f"Wrong guess! point is: {secret}")


main()
{'central_bonus': 6, 'protection_bonus': 10, 'capturing_bonus': 2, 'mobility_bonus': 10, 'potential_capture_bonus': 2, 'exposure_penalty': 7, 'aggressive_capture_bonus': 3}
