cooling_percentage = 19
initial_temperature = 30
room_temperature = 0

soup_temperature = initial_temperature

for _ in range(2):
    soup_temperature -= (soup_temperature - room_temperature) * cooling_percentage / 100
    print(soup_temperature)

print(f'Soup temperature is {soup_temperature:.2f}')
