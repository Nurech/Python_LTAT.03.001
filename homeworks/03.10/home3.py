print("Enter distance in kilometers:")
dist = float(input())

cheapest_taxi = None
cheapest_fare = None

with open('taxiprices.txt', 'r') as f:
    for line in f:
        taxi_info = line.split(',')
        taxi_name = taxi_info[0]
        km_price = float(taxi_info[1])
        starting_fee = float(taxi_info[2])
        fare = km_price * dist + starting_fee
        if not cheapest_fare or fare < cheapest_fare:
            cheapest_fare = fare
            cheapest_taxi = taxi_name

print(f"{cheapest_taxi} is the cheapest.")
