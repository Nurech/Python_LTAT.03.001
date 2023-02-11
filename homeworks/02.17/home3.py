# 3. Painting the walls
# Mikk is renovating his apartment and wants to paint all the walls in his bathroom. In the store, wall paint is sold in cans of a fixed size. One liter of paint can cover 8 square meters.
# Write a program that asks for the length, width, and height of the room (in meters) and the volume of paint in one can (in liters) and outputs how many cans of paint he needs to buy to paint the walls.
#
# Assume that the bathroom has no windows and that the door will also be painted the same color. The ceiling and floor are not painted. All input data are floating point numbers.
#
# Example 1
#
# Enter room length: 3.5
# Enter room width: 2.8
# Enter room height: 2.5
# Enter volume of one can: 0.9
# You have to buy 5 cans of paint.
#
# Example 2
#
# Enter room length: 3
# Enter room width: 2
# Enter room height: 2.4
# Enter volume of one can: 2.7
# You have to buy 2 cans of paint.

import math

room_len = float(input("Enter room length: ") or 3)
room_width = float(input("Enter room width: ") or 2.8)
room_height = float(input("Enter room height: ") or 2.5)
can_volume = float(input("Enter volume of one can: ") or 0.9)

square_meters_to_paint = (room_len * room_height) * 2 + (room_width * room_height) * 2

total_paint_required = square_meters_to_paint / 8
cans_to_buy = math.ceil(total_paint_required / can_volume)

print(f"You have to buy {cans_to_buy} cans of paint.")
