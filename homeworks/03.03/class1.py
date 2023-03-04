def letter_price(weight):
    if weight <= 250:
        return 1.75
    elif weight > 250 and weight <= 500:
        return 2.70
    elif weight > 500 and weight <= 1000:
        return 2.85
    else:
        return 4.35

num_letters = int(input("Enter number of letters: "))
total_cost = 0
for i in range(num_letters):
    weight = int(input(f"Enter weight of letter {i+1}: "))
    total_cost += letter_price(weight)

print(f"Sending these letters will cost {total_cost} euros.")
