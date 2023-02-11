# 2. Name of the month
# Write a program that asks the user to enter a month number and then prints the name of the month.
#
# If the user enters an integer outside the range 1...12, then the programs should print a message informing about that. You can assume that the user enters only integers.
#
# Test your program with delifferent inputs.
#
# Examples
#
# Enter month number: 2
# February
#
# Enter month number: 0
# Month number must be in the range [1-12]
#
# Enter month number: 13
# The year has only 12 months

month_number = int(input("Enter month number: "))

if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
elif month_number <= 0:
    print("Month number must be in the range [1-12]")
elif month_number > 12:
    print("The year has only 12 months")
