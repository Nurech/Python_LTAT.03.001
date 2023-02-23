# 3. Einstein's theory of special relativity If two bodies are moving in the same direction, where the speed of the first body with
# respect to the observer is u and the speed of the second body with respect to the first body is v, then according to the special theory
# of relativity, the speed of the first body with respect to the observer is calculated from the formula
#
# u+v1+u⋅vc2,
#
# where c is the speed of light (299792.458 km/s). This expression is called the sum of speeds u and v.
#
# Create a function called einsum, whose parameters are speeds u and v, and which returns the sum of these speeds according to the
# special theory of relativity.
#
# >>> u = 100000
# >>> v = 200000
# >>> einsum(u, v)
# 245392.74884785622
#
# Use this function to calculate the sum of speeds of four bodies that move in the same direction. The program should prompt for four
# speeds and print out their sum.
#
# Enter speed of the first body with respect to the observer: 100000
# Enter speed of the second body with respect to the first: 150000
# Enter speed of the third body with respect to the second: 200000
# Enter speed of the fourth body with respect to the third: 250000
# Sum of speeds is 297993.41836837644 km/s
#
# Hint. Add first two speeds. Then add the third speed to the sum. Then add the fourth speed to the sum.
import math


def einsum(u, v):
    c = 299792.458
    return (u + v) / (1+(u*v/(c*c)))

# prompt for each speed
u1 = float(input("Enter speed of the first body with respect to the observer: ") or 100000)
u2 = float(input("Enter speed of the second body with respect to the first: ") or 150000)

# calculate sum of first two speeds
sum_speed = einsum(u1, u2)

# prompt for each additional speed and add it to the sum
u3 = float(input("Enter speed of the third body with respect to the second: ") or 200000)
sum_speed = einsum(sum_speed, u3)

u4 = float(input("Enter speed of the fourth body with respect to the third: ") or 250000)
sum_speed = einsum(sum_speed, u4)

# print the sum of all speeds
print("Sum of speeds is", sum_speed, "km/s")
