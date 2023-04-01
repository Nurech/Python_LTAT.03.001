def good_weather(type, speed):
    if type == "plane":
        if speed <= 15:
            return True
        else:
            return False
    elif type == "ship":
        if speed <= 20:
            return True
        else:
            return False
    else:
        # because bus not affected by weather
        return True
        
print(good_weather("plane", 10))



def ticket_price(type, price):
    if type == "plane":
        pkm = 0.25
        return price * pkm + 100
    elif type == "ship":
        pkm = 0.10
        return price * pkm + 30
    if type == "bus":
        pkm = 0.05
        return price * pkm + 10
    
print(ticket_price("plane", 1000))

budget = input("Enter budget: ") or int(1000)
wind = input("Enter the wind speed on the date of travel: ") or 17
distance = input("Enter the distance to the destination: ") or 500


def check_trip(budget, wind, distance):
    options = ["plane", "ship", "bus"]
    flag = False
    for option in options:
        #print(option)
        if (good_weather(option, wind)):
            if (ticket_price(option, distance) <= budget):
                flag = True
                print("You can go on a trip by "+ option)
                print("The ticket price is " + str(ticket_price(option, distance)) +" euros.")
    
    if flag == True:
        print("No suitable trip was found.")
    
check_trip(budget, wind, distance)

