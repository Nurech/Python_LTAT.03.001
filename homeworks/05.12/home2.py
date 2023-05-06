class Record:
    def __init__(self, name: str, genre: str, year: int):
        self.name = name
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.genre}, {self.year}"


class Rock(Record):
    def __init__(self, name: str, year: int):
        super().__init__(name, "Rock", year)

    def cost(self, days: int) -> float:
        return days * 2.5


class Pop(Record):
    def __init__(self, name: str, year: int):
        super().__init__(name, "Pop", year)

    def cost(self, days: int) -> float:
        return days * 1.7


class Classical(Record):
    def __init__(self, name: str, year: int):
        super().__init__(name, "Classical", year)

    def cost(self, days: int) -> float:
        return days * 4.9


class RentalShop:
    def __init__(self, records):
        self.records = records

    def borrow(self):
        balance = float(input("How many euros do you have for renting records? "))
        while True:
            print("------------------------")
            print("Your balance is", balance, "euros.")
            command = input("Enter command: ").split()
            if command[0] == "L":
                for record in self.records:
                    print(record)
            elif command[0] == "B":
                name, days = command[1], int(command[2])
                record = next((record for record in self.records if record.name == name), None)
                if record:
                    cost = record.cost(days)
                    if balance >= cost:
                        balance -= cost
                        self.records.remove(record)
                        print(name, "borrowed.")
                    else:
                        print("Not enough money for rental!")
                else:
                    print("No such record in the rental!")
            elif command[0] == "R":
                name, genre, year = command[1], command[2], int(command[3])
                if genre == "Rock":
                    record = Rock(name, year)
                elif genre == "Pop":
                    record = Pop(name, year)
                elif genre == "Classical":
                    record = Classical(name, year)
                self.records.append(record)
                print(name, "returned.")
            elif command[0] == "E":
                break


def main():
    records = [
        Rock("Nevermind", 1991),
        Pop("Thriller", 1982),
        Classical("Symphony No. 40", 1788),
        Rock("Back of My Mind", 2021),
        Pop("Evermore", 2021),
        Classical("Experiment", 2019)
    ]
    # records = [
    #     Rock("Back of My Mind", 2021),
    #     Pop("Evermore", 2021),
    #     Classical("Experiment", 2019)
    # ]
    rental_shop = RentalShop(records)
    rental_shop.borrow()

# def main():
#     rock = Rock("Nevermind", 1991)
#     pop = Pop("Thriller", 1982)
#     classical = Classical("Symphony No. 40", 1788)
#     print(rock)
#     print(pop)
#     print(classical)

if __name__ == "__main__":
    main()
