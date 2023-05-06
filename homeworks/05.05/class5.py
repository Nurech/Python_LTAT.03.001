class Person:
    def __init__(self, name: str, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def common_mother(self, other_person):
        if self.mother is None or other_person.mother is None:
            return False
        return self.mother.name == other_person.mother.name

    def common_father(self, other_person):
        if self.father is None or other_person.father is None:
            return False
        return self.father.name == other_person.father.name

    def ancestor(self, other_person):
        if self.mother is None and self.father is None:
            return False
        if self.mother == other_person or self.father == other_person:
            return True
        return self.mother.ancestor(other_person) if self.mother else self.father.ancestor(other_person)

    def relatives(self, other_person):
        if self.common_mother(other_person) or self.common_father(other_person):
            return True
        if self.ancestor(other_person) or other_person.ancestor(self):
            return True
        return False


abraham = Person("Abraham")
mona = Person("Mona")
clancy = Person("Clancy")
jackie = Person("Jackie")
herb = Person("Herb", mona, abraham)
homer = Person("Homer", mona, abraham)
marge = Person("Marge", jackie, clancy)
bart = Person("Bart", marge, homer)
lisa = Person("Lisa", marge, homer)
maggie = Person("Maggie", marge, homer)

print("Bart and Lisa are relatives:", bart.relatives(lisa))  # TRUE
print("Bart and Abraham are relatives:", bart.relatives(abraham))  # Grandfather
print("Marge and Mona are relatives:", marge.relatives(mona))  # no
