class Jockey:
    MIN_AGE = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
        self.__age = value

    def __gt__(self, other):
        return self.horse.speed > other.horse.speed
