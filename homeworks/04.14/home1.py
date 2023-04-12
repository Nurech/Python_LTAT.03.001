import math
import random


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


point = int(input("Enter the number of points: "))

points = []

for i in range(1, point + 1):
    coord_input = input(f"Enter the coordinates of point {i}: ") or "(" + str(random.randint(0, 9)) + ", " + str(random.randint(0, 9)) + ")"
    coord_tuple = tuple(map(int, coord_input.strip("()").split(",")))
    points.append(coord_tuple)
    print(points)

min = float("inf")
tup_pair = ()

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        curr = distance(points[i], points[j])
        if curr < min:
            min = curr
            tup_pair = (i + 1, j + 1)

print(f"Points {tup_pair[0]} and {tup_pair[1]} are the closest to each other.")
