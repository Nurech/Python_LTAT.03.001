class Scooter:
    def __init__(self, name, starting_fee, price_per_100m, distance):
        self.name = name
        self.starting_fee = starting_fee
        self.price_per_100m = price_per_100m
        self.distance = distance

    def ride(self, km):
        self.distance = int(self.distance) - km

    def charge(self, km):
        self.distance += km

    def calculate_price(self, km):
        return self.starting_fee + str((float(km) * 1000 / 100) * float(self.price_per_100m))

    def __str__(self):
        return f"Scooter(name = '{self.name}', starting_fee = {self.starting_fee}, price_per_100m = {self.price_per_100m}, distance = {self.distance})"


class Rental:
    def __init__(self, scooters):
        self.scooters = scooters

    def display_choices(self, km):
        available_scooters = [scooter for scooter in self.scooters if float(scooter.distance) >= float(km)]
        available_scooters.sort(key=lambda scooter: scooter.calculate_price(km))
        return available_scooters

    def ride_scooter(self, scooter_name, km):
        scooter = self._find_scooter(scooter_name)
        if scooter:
            scooter.ride(km)

    def charge_scooter(self, scooter_name, km):
        scooter = self._find_scooter(scooter_name)
        if scooter:
            scooter.charge(km)

    def _find_scooter(self, scooter_name):
        for scooter in self.scooters:
            if scooter.name == scooter_name:
                return scooter
        return None


def main():
    scooters = []

    for i in range(3):
        scooter_data = input(f"Enter company, starting fee, price per hundred meters, and distance: ")
        name, starting_fee, price_per_100m, distance = scooter_data.split(",")
        scooters.append(Scooter(name, starting_fee, price_per_100m, distance))

    rental = Rental(scooters)
    rental.display_choices(2)
    rental.ride_scooter("Bolt", 3)
    rental.ride_scooter("Tuul", 18)
    rental.ride_scooter("Tuul", 5)
    rental.charge_scooter("Tuul", 5)
    rental.ride_scooter("Tuul", 2)

main()

