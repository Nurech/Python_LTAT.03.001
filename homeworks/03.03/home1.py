# 1. Number of days Write a function number_of_days with one integer parameter, which represents the number of month; the functions
# returns the number of days in that month. The numbers of months are 1, 2, ..., 12, and let's assume that it is not a leap year. If the
# number is some other integer, then the function should return −1.
#
# >>> number_of_days(9)
# 30
# >>> number_of_days(2)
# 28
# >>> number_of_days(100)
# -1
#
# Test the function with different arguments.
#
# Then write a program that repeatedly asks the user for a number of month and prints the number of days in that month until the user
# enters 'done'. The program should perform all necessary input checks and call the function number_of_days only if the number of month
# is an integer in the range 1, ..., 12.
#
# Enter number of month or 'done': 3
# This month has 31 days
# Enter number of month or 'done': 4
# This month has 30 days
# Enter number of month or 'done': fifth
# Please enter a valid number
# Enter number of month or 'done': -1
# Number of month must be in the range 1-12
# Enter number of month or 'done': 100
# Number of month must be in the range 1-12
# Enter number of month or 'done': 10
# This month has 31 days
# Enter number of month or 'done': done
#
# Optional modification. Implement the function number_of_days in such a way that it returns 28 or 29 for February, depending on whether
# the current year in the system is an ordinary year or leap year.

import calendar


def number_of_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 28
    else:
        return -1


while True:
    user_input = input("Enter number of month or 'done': ")
    if user_input.lower() == "done":
        break
    else:
        try:
            number = int(user_input)
            if 0 < number <= 12:
                result = number_of_days(number)
                if result == -1:
                    print("Please enter a valid number")
                else:
                    print(f"This month has {result} days")
            else:
                print("Number of month must be in the range 1-12")
        except ValueError:
            print("Please enter a valid number")
