# A plant grows according to firm rules. Each week, every branch of the plant splits into two branches, main branch and side branch,
# both of which grow one unit longer in the course of the week. If a branch has been grown three weeks as a main branch,
# a beautiful blossom appears at the top of it, and this branch doesn't grow any longer.
#
# Plant
#
#
#
# Write a program that finds how many new blossoms appear on the N-th week after a single main branch of the length one unit is planted
# in the pot. The program should prompt for the number of week and write the number of new blossoms on the screen.
#
# Example 1
# Enter number of week: 5
# Number of new blossoms will be 2
#
# Example 2
# Enter number of week: 6
# Number of new blossoms will be 3


# use dp memo, binary?
# Needs to memorized 4 things
# 1) number of branches that has a side branch before current length
# 2) number of branches that has a one main branch before current length
# 3) number of branches that has a two main branch before current length
# 4) number of branches that has a three main branch before current length
# on each day, grow each thing's by mapping to the correct new branches
# for example, for (1), the new branch can either be a main or side
# if its side, it goes back into (1)
# if its main, it goes into (2)
# Stop growing once something gets into (4)
# The final result is sum(4)

n = int(input("Enter number of week: ") or 5)

side_1 = 0
main_1 = 1
main_2 = 0
main_3 = 0

# n = 5

arr = []

for i in range(n + 1):
    if i > 0:
        main_3 = main_2
        main_2 = main_1
        main_1 = side_1
        side_1 = (main_1 + main_2 + side_1)
        arr.append(side_1)
        if i > 2:
            side_1 = (arr.pop() - main_1 + main_3)
            # should memo main_1 out of side_1

# print("side_1 ", side_1)
# print("main_1 ", main_1)
# print("main_2 ", main_2)
# print("main_3 ", main_3)
print("Number of new blossoms will be", main_3)
