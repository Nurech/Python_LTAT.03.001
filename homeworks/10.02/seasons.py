month = int(input("Enter month number: "))

if month == 12 or month <= 2:
    print("winter")
elif month >= 3 and month <= 5:
    print("spring")
elif month >= 6 and month <= 8:
    print("summer")
elif month >= 9 and month <= 11:
    print("autumn")
