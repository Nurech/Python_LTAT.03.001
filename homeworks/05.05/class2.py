class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def bmi(self) -> float:
        height_in_meters = self.height / 100
        bmi_value = self.weight / (height_in_meters ** 2)
        return round(bmi_value, 1)


def compare_heights(person1: Person, person2: Person):
    if person1.height > person2.height:
        print(f"{person1.name} is taller than {person2.name}")
    elif person1.height < person2.height:
        print(f"{person1.name} is shorter than {person2.name}")
    else:
        print(f"{person1.name} and {person2.name} are of the same height")


def compare_weights(person1: Person, person2: Person):
    if person1.weight > person2.weight:
        print(f"{person1.name} weighs more than {person2.name}")
    elif person1.weight < person2.weight:
        print(f"{person1.name} weighs less than {person2.name}")
    else:
        print(f"{person1.name} and {person2.name} have the same weight")


# Example usage
anne = Person("Anne", 22, 162, 69)
sirje = Person("Sirje", 43, 170, 58)

compare_heights(anne, sirje)
compare_weights(anne, sirje)
