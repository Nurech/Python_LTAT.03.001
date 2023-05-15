import random


class Dragon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} roars")


class EarthDragon(Dragon):
    def __init__(self, name, energy):
        super().__init__(name)
        self.energy = energy

    def attack(self):
        if self.energy > 0:
            print(f"{self.name} shakes the ground")
            self.energy -= 1
        else:
            super().attack()


class FireDragon(Dragon):
    def __init__(self, name, fuel):
        # print(f"Fuel: {fuel}")
        super().__init__(name)
        self.fuel = fuel

    def attack(self):
        # print(self.fuel)
        if self.fuel >= 10:
            print(f"{self.name} spits fire")
            self.fuel -= 10
        else:
            super().attack()


class StoneDragon(EarthDragon):
    def __init__(self, name, energy, stones):
        super().__init__(name, energy)
        self.stones = stones

    def attack(self):
        if self.stones > 0:
            stones_to_throw = min(self.stones, 3)
            print(f"{self.name} throws {stones_to_throw} stones")
            self.stones -= stones_to_throw
        else:
            super().attack()


class LavaDragon(FireDragon):
    def __init__(self, name, fuel, lava):
        super().__init__(name, fuel)
        self.lava = lava

    def attack(self):
        if self.lava > 0:
            # print('here')
            lava_to_spew = random.randint(1, min(self.lava, 100))
            print(f"{self.name} spews {lava_to_spew} lava")
            self.lava -= lava_to_spew
        else:
            # print('here')
            super().attack()


dragons = [StoneDragon("Stony1", 5, 10), StoneDragon("Stony2", 5, 10),
           LavaDragon("Lavy1", 50, 500), LavaDragon("Lavy2", 50, 500)]

for _ in range(20):
    dragon = random.choice(dragons)
    dragon.attack()
