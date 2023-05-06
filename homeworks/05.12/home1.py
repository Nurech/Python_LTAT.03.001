class Vehicle:
    def __init__(self, brand: str, price: int, fuel_consumption: float):
        self.brand = brand
        self.price = price
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"{self.brand}, price {self.price} euros, fuel consumption {self.fuel_consumption} liters per 100 km."


class Truck(Vehicle):
    def trip_cost(self, distance: int) -> float:
        return round(distance * self.fuel_consumption * 1.8 / 100, 1)

    def horsepower(self):
        print(500)


class Car(Vehicle):
    def trip_cost(self, distance: int) -> float:
        return round(distance * self.fuel_consumption * 1.9 / 100, 1)

    def horsepower(self):
        print(180)


class Motorcycle(Vehicle):
    def trip_cost(self, distance: int) -> float:
        return round(distance * self.fuel_consumption * 1.85 / 100, 1)

    def horsepower(self):
        print(85)


class Garage:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def display(self):
        print("The following vehicles are in the garage:\n")
        for vehicle in self.vehicles:
            print(vehicle)
            print(f"The {vehicle.__class__.__name__.lower()} has ", end="")
            vehicle.horsepower()
            print(f"It costs {vehicle.trip_cost(186)} euros to travel from Tartu to Tallinn.\n")


def create_vehicle(line: str):
    vehicle_type, vehicle_info = line.split(" - ")
    brand, price, fuel_consumption = vehicle_info.split(", ")
    price, fuel_consumption = int(price), float(fuel_consumption)

    if vehicle_type == "Truck":
        return Truck(brand, price, fuel_consumption)
    elif vehicle_type == "Car":
        return Car(brand, price, fuel_consumption)
    elif vehicle_type == "Motorcycle":
        return Motorcycle(brand, price, fuel_consumption)


def main():
    with open("vehicles.txt", "r") as file:
        vehicles = [create_vehicle(line.strip()) for line in file]

    garage = Garage(vehicles)
    garage.display()


if __name__ == "__main__":
    main()
