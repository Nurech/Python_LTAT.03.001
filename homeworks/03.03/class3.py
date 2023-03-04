dragons = int(input("Enter number of dragons: "))
snakes = int(input("Enter number of snakes: "))
dinosaurs = int(input("Enter number of dinosaurs: "))

day = 1

while dragons > 0 and snakes > 0 and dinosaurs > 0:
    dragons += 1
    snakes += 1
    dinosaurs += 1
    day += 1

print("The last meal will be on day " + str(day))

if dragons > 0:
    print("There will be " + str(dragons) + " dragons left")

if snakes > 0:
    print("There will be " + str(snakes) + " snakes left")

if dinosaurs > 0:
    print("There will be " + str(dinosaurs) + " dinosaurs left")
