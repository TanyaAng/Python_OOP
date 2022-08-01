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

    @staticmethod
    def make_instance_of_planet(name, items):
        planet = Planet(name)
        planet.items = items.split(', ')
        return planet

    def find_suitable_astronauts(self):
        suitable_astronauts = []
        for a in sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True):
            if a.oxygen > 30:
                suitable_astronauts.append(a)
        if suitable_astronauts:
            return suitable_astronauts[0:5]
        return None

    def collect_items(self, astronauts, items_on_planet):
        astronauts_on_mission = []
        for astronaut in astronauts:
            while items_on_planet:
                if astronaut.oxygen <= 0:
                    break
                current_item = items_on_planet.pop()
                astronaut.breathe()
                astronaut.backpack.append(current_item)
                if astronaut not in astronauts_on_mission:
                    astronauts_on_mission.append(astronaut)
        return astronauts_on_mission

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.VALID_ASTRONAUTS_TYPE:
            raise Exception("Astronaut type is not valid!")
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        astronaut = self.make_instance_of_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = self.make_instance_of_planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
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

        astronauts_on_mission = self.collect_items(suitable_astronauts, items)

        if not items and astronauts_on_mission:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {len(astronauts_on_mission)} astronauts participated in collecting items."
        self.unsuccessful_missions += 1
        return f"Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n"
        result += f"{self.unsuccessful_missions} missions were not completed!\n"
        result += f"Astronauts' info:\n"
        for a in self.astronaut_repository.astronauts:
            result += str(a) + '\n'
        return result.strip()

# station = SpaceStation()
#
# station.add_astronaut('Biologist', 'Pesho')
# station.add_astronaut('Geodesist', 'Gosho')
# station.add_astronaut('Meteorologist', 'Stamat')
# print(station.report())
#
# for _ in range(3):
#     for a in station.astronaut_repository.astronauts:
#         a.breathe()
#
# print(station.report())
# print(station.find_suitable_astronauts())
# print(station.add_astronaut('Biologist', 'Gosho'))
