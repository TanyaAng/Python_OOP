from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS_TYPE = ("Biologist", "Geodesist", "Meteorologist")

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    @staticmethod
    def make_instance_of_astronaut(astronaut_type, name):
        if astronaut_type == 'Biologist':
            return Biologist(name)
        elif astronaut_type == 'Geodesist':
            return Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            return Meteorologist(name)

    def find_suitable_astronauts(self):
        suitable_astronauts = []
        for a in sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True):
            if a.oxygen > 30:
                suitable_astronauts.append(a)
        if suitable_astronauts:
            if len(suitable_astronauts) > 5:
                suitable_astronauts = suitable_astronauts[0:5]
            return suitable_astronauts
        return None

    def is_mission_successful(self, collected_items, total_items_on_planet):
        if collected_items == total_items_on_planet:
            self.successful_missions += 1
            return True
        self.unsuccessful_missions += 1
        return False

    def collect_items(self, astronauts, items_on_planet):
        collected_items = 0
        for astronaut in sorted(astronauts, key=lambda a: a.oxygen, reverse=True):
            while items_on_planet:
                current_item = items_on_planet.pop()
                astronaut.backpack.append(current_item)
                collected_items += 1
                astronaut.breathe()
                if astronaut.oxygen < astronaut.OXYGEN_DECREASE:
                    break
        return collected_items

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        if astronaut_type not in self.VALID_ASTRONAUTS_TYPE:
            raise Exception("Astronaut type is not valid!")
        astronaut = self.make_instance_of_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}"

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")
        astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name][0]
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")
        suitable_astronauts = self.find_suitable_astronauts()
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        planet_to_explore = self.planet_repository.find_by_name(planet_name)

        items = planet_to_explore.items
        total_items_on_planet = len(items)
        collected_items = self.collect_items(suitable_astronauts, items)

        if self.is_mission_successful(collected_items, total_items_on_planet):
            return f"Planet: {planet_name} was explored. {len(suitable_astronauts)} astronauts participated in collecting items."
        return f"Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!"
        result += f"{self.unsuccessful_missions} missions were not completed!"
        result += f"Astronauts' info:\n"
        for a in self.astronaut_repository.astronauts:
            result += str(a) + '\n'
        return result.strip()
