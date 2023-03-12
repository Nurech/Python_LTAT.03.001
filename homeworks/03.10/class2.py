# Session exercises 2. Budget Hanna and Rasmus organize a party and want to estimate the costs. The party budget consists of expenses on
# food, which is 10 euros per person, and room rent, which is a fixed price of 55 euros regardless of the number of people.
#
# (1/5) First, create a function called budget. It has one parameter, the number of people, and calculates the budget size for a given
# number of people.
#
# >>> budget(4)
# 95
# >>> budget(10)
# 155

def budget(num_people):
    return (num_people * 10) + 55
file_name_in = input("Enter input file name: ")
file_name_out = input("Enter output file name: ")

num_invited = 0
num_coming = 0

with open(file_name_in, "r") as f:
    for line in f:
        if line.strip() == "+":
            num_coming += 1
        elif line.strip() == "?":
            num_invited += 1

total_invited = num_invited + num_coming
min_participants = num_coming
max_participants = num_coming + num_invited
min_budget = budget(min_participants)
max_budget = budget(max_participants)

with open(file_name_out, "w") as f:
    f.write(f"A total of {total_invited} people have been invited\n")
    f.write(f"The minimum number of participants is {min_participants}\n")
    f.write(f"The maximum number of participants is {max_participants}\n")
    f.write(f"The minimum budget for the party is {min_budget} euros\n")
    f.write(f"The maximum budget for the party is {max_budget} euros\n")

print("Data written to file.")
