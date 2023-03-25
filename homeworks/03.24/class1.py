# A certain number of people are standing in a queue in the store. Each of them has a certain number of items in the basket.
#
# (1/3) Write a program that lets the user enter the numbers of items of each person and outputs the total number of people standing in
# the queue.
#
# Enter the numbers of items: 2 4 10 8 3 1 12 5 2 1 7
# There are 11 people standing in the queue
#
# Hint. Convert the user input to a list of numbers and find its length.
#
# (2/3) Extend your program so that it finds how many people have more than three items in their baskets.
# (3/3) Extend the program so that it determines which person has the most items in the basket and outputs that person's number, together with the number of items.

people = input("Enter the number of items")
people_arr = [int(n) for n in people.split(" ", -1)]
num_of_people = len(people_arr)
result = list(filter(lambda x: int(x) > 3, people_arr))


def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

print(people_arr)
max_ = largest(people_arr, len(people_arr))
max_idx = people_arr.index(max_) + 1

print("There are " + str(num_of_people) + " people standing in the queue")
print(str(len(result)) + " people have more than three items in their baskets")
print("Person number " + str(max_idx) + "has the most items, " + str(max_) + " items")
