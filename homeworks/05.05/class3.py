class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def bmi(self) -> float:
        height_in_meters = self.height / 100
        bmi_value = self.weight / (height_in_meters ** 2)
        # print(bmi_value)
        return round(bmi_value, 1)


def read_person_data(file_path: str) -> list:
    persons = []

    with open(file_path, 'r') as file:
        for line in file:
            name, age, height, weight = line.strip().split(', ')
            persons.append(Person(name, int(age), int(height), int(weight)))

    return persons


def print_bmi_information(persons: list):
    for person in persons:
        bmi = person.bmi()
        weight_status = "you are of normal weight"

        if bmi < 19:
            weight_status = "you should gain weight"
        elif bmi > 25:
            weight_status = "you should lose weight"

        print(f"{person.name}, {person.age} years old: your body mass index is {bmi}, {weight_status}")


file_path = "healthcheck.txt"
persons = read_person_data(file_path)
print_bmi_information(persons)
