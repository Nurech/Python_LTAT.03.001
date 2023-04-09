def birthdays(birthdays):
    count = {}
    for date in birthdays:
        if date in count:
            count[date] += 1
        else:
            count[date] = 1

    max_count = max(count.values())
    common_dates = [date for date, count in count.items() if count == max_count]

    return common_dates

a = ['19.04', '21.05', '04.07', '21.05', '11.11', '12.03', '04.07', '08.06', '12.03', '21.05']

b = birthdays(a)

if len(b) == 1:
    print(f"The most common birthday is: {b[0]}")
else:
    print(f"The most common birthdays are: {', '.join(b)}")
