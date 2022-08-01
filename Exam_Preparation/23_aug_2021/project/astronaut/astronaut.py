from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_DECREASE = 10

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE

    @abstractmethod
    def increase_oxygen(self, amount):
        pass

    def __str__(self):
        if self.backpack!=[]:
            return f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {', '.join(self.backpack)}"
        return f'Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: none'

