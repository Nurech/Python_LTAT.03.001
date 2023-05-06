def display_number(number: int, size: int):
    digit_layout = {
        0: (" - ", "| |", "   ", "| |", " - "),
        1: ("   ", "  |", "   ", "  |", "   "),
        2: (" - ", "  |", " - ", "|  ", " - "),
        3: (" - ", "  |", " - ", "  |", " - "),
        4: ("   ", "| |", " - ", "  |", "   "),
        5: (" - ", "|  ", " - ", "  |", " - "),
        6: (" - ", "|  ", " - ", "| |", " - "),
        7: (" - ", "  |", "   ", "  |", "   "),
        8: (" - ", "| |", " - ", "| |", " - "),
        9: (" - ", "| |", " - ", "  |", " - ")
    }

    digits = [int(d) for d in str(number)]
    for i in range(5):
        if i % 2 == 0:
            for digit_index, digit in enumerate(digits):
                print(" " + digit_layout[digit][i][1] * size + " ", end="")
                if digit_index != len(digits) - 1:
                    print(" " * size, end="")
            print()
        else:
            for _ in range(size):
                for digit_index, digit in enumerate(digits):
                    print(digit_layout[digit][i][0] + " " * size + digit_layout[digit][i][2], end="")
                    if digit_index != len(digits) - 1:
                        print(" " * size, end="")
                print()

number = int(input("Enter number: "))
size = int(input("Enter size: "))
display_number(number, size)
