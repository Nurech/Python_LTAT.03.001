class Item:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def output_item(self):
        print(f"{self.name}, {self.weight} kg")
        # print(self)


class Suitcase:
    def __init__(self, weight_limit: int):
        self.weight_limit = weight_limit
        self.items = []
        self.total_weight = 0

    def add_item(self, item: Item):
        if self.total_weight + item.weight <= self.weight_limit:
            self.items.append(item)
            self.total_weight += item.weight
        else:
            print("Weight limit exceeded!")
        # print('test')

    def output_summary(self):
        print(
            f"There {'is' if len(self.items) == 1 else 'are'} {len(self.items)} item{'s' if len(self.items) != 1 else ''} in the suitcase with a total weight of {self.total_weight} kg.")

    def output_items(self):
        for item in self.items:
            item.output_item()


class LuggageRoom:
    def __init__(self, weight_limit: int):
        self.weight_limit = weight_limit
        self.suitcases = []
        self.total_weight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.total_weight + suitcase.total_weight <= self.weight_limit:
            self.suitcases.append(suitcase)
            self.total_weight += suitcase.total_weight

    def output_summary(self):
        print(
            f"There {'is' if len(self.suitcases) == 1 else 'are'} {len(self.suitcases)} suitcase{'s' if len(self.suitcases) != 1 else ''} in the luggage room with {self.weight_limit - self.total_weight} kg of free space.")

    def output_items(self):
        for suitcase in self.suitcases:
            suitcase.output_items()


def main():
    # Create items
    laptop = Item("Laptop", 2)
    book = Item("Book", 1)
    dumbbell = Item("Dumbbell", 4)

    suitcase = Suitcase(5)
    suitcase.output_summary()
    suitcase.add_item(laptop)
    suitcase.output_summary()
    suitcase.add_item(book)
    suitcase.output_summary()
    suitcase.add_item(dumbbell)
    suitcase.output_summary()

    luggage_room = LuggageRoom(50)
    luggage_room.add_suitcase(suitcase)

    luggage_room.output_items()


main()
