from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    AQUARIUM_TYPES = ("FreshwaterAquarium", "SaltwaterAquarium")
    DECORATION_TYPES = ('Ornament', 'Plant')
    FISH_TYPES = ('FreshwaterFish', 'SaltwaterFish')

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def make_aquarium_instance(type, name):
        if type == 'FreshwaterAquarium':
            return FreshwaterAquarium(name)
        elif type == 'SaltwaterAquarium':
            return SaltwaterAquarium(name)

    @staticmethod
    def make_decoration_instance(type):
        if type == 'Ornament':
            return Ornament()
        elif type == 'Plant':
            return Plant()

    @staticmethod
    def make_fish_instance(fish_type, fish_name, fish_species, price):
        if fish_type == 'FreshwaterFish':
            return FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            return SaltwaterFish(fish_name, fish_species, price)

    def get_decoration_by_type(self, decoration_type):
        return self.decorations_repository.find_by_type(decoration_type)

    def find_aquarium_by_name(self, name):
        aqua = [a for a in self.aquariums if a.name == name]
        if aqua:
            return aqua[0]

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.AQUARIUM_TYPES:
            return "Invalid aquarium type."

        aqua = self.make_aquarium_instance(aquarium_type, aquarium_name)
        self.aquariums.append(aqua)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.DECORATION_TYPES:
            return "Invalid decoration type."
        decoration = self.make_decoration_instance(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.get_decoration_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        aqua = self.find_aquarium_by_name(aquarium_name)
        if aqua and decoration:
            aqua.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self.FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        aqua = self.find_aquarium_by_name(aquarium_name)
        fish = self.make_fish_instance(fish_type, fish_name, fish_species, price)
        if aqua and fish:
            return aqua.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aqua = self.find_aquarium_by_name(aquarium_name)
        aqua.feed()
        return f"Fish fed: {len(aqua.fish)}"

    def calculate_value(self, aquarium_name):
        aqua = self.find_aquarium_by_name(aquarium_name)
        total_value = aqua.calculate_total_price()
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ''
        for aqua in self.aquariums:
            result += str(aqua)
        return result
