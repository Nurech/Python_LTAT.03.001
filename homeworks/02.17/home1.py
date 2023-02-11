# When the maximum driving speed is exceeded, a fine is imposed. The size of the fine is obtained by multiplying the number of km/h's above the allowed limit by 3. The maximum fine is 190 euros.
#
# Write a program that
#
# prompts the user for the name, speed limit, and actual speed;
# calculates the fine according to the rules above;
# outputs the name and the size of the fine on the screen.
# Example
#
# Enter name: Jürgen
# Enter speed limit (km/h): 60
# Enter actual speed (km/h): 80
# Jürgen, your fine for speeding is €60.
#
# Explanation: the speed limit is exceeded by 80 − 60 = 20 km/h. Therefore, the fine is 3 · 20 = 60 euros.
#
# Second example
#
# Enter name: Hendrik
# Enter speed limit (km/h): 50
# Enter actual speed (km/h): 172
# Hendrik, your fine for speeding is €190.
#
# Explanation: the speed is exceeded by 172 − 50 = 122 km/h. The calculation gives a fine of 3 · 122 = 366 euros. Since it exceeds the maximum amount of the fine, the actual fine will be 190 euros.

name = input("Enter name: ")
speed = input("Enter speed limit (km/h): ")
actual_speed = input("Enter actual speed (km/h): ")
fine = (int(actual_speed) - int(speed)) * 3
if fine > 190:
    fine = 190

ans = print(f"{name}, your fine for speeding is €{fine}.")
