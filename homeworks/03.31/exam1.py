def battery_time(capacity, age):
    rate = 15 if age > 3 else 8
    return round(capacity / rate * 60)

def is_battery_enough(battery_time, usage_time):
    return True if battery_time >= usage_time else battery_time - usage_time

capacity = int(input())
usage_time = int(input())
age = int(input())

remaining_time = battery_time(capacity, age)
result = is_battery_enough(remaining_time, usage_time)

if result is True:
    print(f"The battery of the computer has enough capacity for at least {usage_time} minutes.")
else:
    print(f"The battery is {abs(result)} minutes short. The computer must be charged.")
