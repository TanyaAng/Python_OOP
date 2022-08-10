from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    FISH_TYPES = ('FreshwaterFish', 'SaltwaterFish')

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        if self.decorations:
            return sum([d.comfort for d in self.decorations])
        return 0

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return f"Not enough capacity."
        if fish.__class__.__name__ in self.FISH_TYPES:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        else:
            return f"Water not suitable."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def calculate_total_price(self):
        value = 0
        value += sum([f.price for f in self.fish])
        value += sum([d.price for d in self.decorations])
        return value

    def __str__(self):
        result = f'{self.name}:\n'
        if self.fish:
            result += f"Fish: {' '.join([f.name for f in self.fish])}\n"
        else:
            result += f"Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"
        return result
