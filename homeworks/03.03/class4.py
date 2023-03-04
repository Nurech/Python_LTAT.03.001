# (1/2) A hermit lives on a private island. His house has two doors. At each door, there are n pairs of shoes. When the hermit wants to
# leave the house, he draws lots, out of which door he should go, puts on the shoes at that door, and goes outside. Coming back,
# he again draws lots through which door he should enter, and leaves the shoes behind that door. On average, after what number of times
# the hermit has to leave the house barefoot because there are no shoes at the selected door?
#
# The average number (that depends on n) can be found by an experiment. Write a program that simulates this process a large number of
# times and computes the average at the end.
#
# For example, try to find the average for n = 5.

import random

n_1 = 5
n_2 = 5

total_trips = 0

trips_without_shoes = 0

for i in range(1000):
    # draw lots for which door to use
    door = random.randint(1,2)

    # if the door has no shoes, trip without shoes
    if door == 1:
        if n_1 == 0:
            trips_without_shoes += 1
        else:
            n_1 -= 1

    if door == 2:
        if n_2 == 0:
            trips_without_shoes += 1
        else:
            n_2 -= 1

    # draw lots for which door to enter
    enter_door = random.randint(1,2)

    if enter_door == 1:
        n_1 += 1

    if enter_door == 2:
        n_2 += 1

    total_trips += 1

# calculate and print the average
average = trips_without_shoes/total_trips
print("Average number of trips without shoes for n = 5 is", average)
