# 1. Salary The length of a regular working week is 40 hours. The pay rate for overtime work is one and a half times higher than the
# standard hourly rate.
#
# (1/3) Write a function with two parameters: the number of hours worked and the standard hourly rate. The function returns the amount of
# pay, taking into account possible overtime work.
#
# >>> calculate_pay(45, 10)
# 475.0
#
# Explanation: 40*10 + 5*1.5*10 = 475.0

hours = 45
pay = 10


def calculate_pay(hours, pay):
    if hours <= 40:
        return hours * pay
    else:
        extra = hours - 40
        return 40 * pay + (extra * 1.5 * pay)


print(calculate_pay(hours, pay))
