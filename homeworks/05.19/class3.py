import random

def to_the_sea(distance, walked=0):
    print("distance: ", distance)
    if distance == 0:
        print("Reached the sea")
        return walked
    else:
        direction = random.choice(["East", "Towards the sea", "To the west"])
        print(direction)
        if direction == "Towards the sea":
            return to_the_sea(distance-1, walked+1)
        else:
            return to_the_sea(distance, walked+1)

print("blocks walked:", to_the_sea(3))
