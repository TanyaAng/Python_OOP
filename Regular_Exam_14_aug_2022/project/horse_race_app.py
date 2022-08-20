from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = ("Appaloosa", "Thoroughbred")

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @staticmethod
    def make_horse_instance(type, name, speed):
        if type == 'Appaloosa':
            return Appaloosa(name, speed)
        elif type == 'Thoroughbred':
            return Thoroughbred(name, speed)

    def find_horse_by_name(self, name):
        searched_horse = [h for h in self.horses if h.name == name]
        if searched_horse:
            return searched_horse[0]

    def find_last_not_taken_horse_by_type(self, type):
        last_horse = [h for h in reversed(self.horses) if h.__class__.__name__ == type and not h.is_taken]
        if last_horse:
            return last_horse[0]

    def find_jockey_by_name(self, name):
        searched_jockey = [j for j in self.jockeys if j.name == name]
        if searched_jockey:
            return searched_jockey[0]

    def find_jockey_in_horse_race_by_name(self, name):
        searched_race = [r for r in self.horse_races if name in r.jockeys]
        if searched_race:
            return searched_race[0]

    def find_race_by_type(self, type):
        searched_race = [r for r in self.horse_races if r.race_type == type]
        if searched_race:
            return searched_race[0]

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type in self.HORSE_TYPES:
            exist_horse = self.find_horse_by_name(horse_name)
            if exist_horse:
                raise Exception(f"Horse {horse_name} has been already added!")

            horse = self.make_horse_instance(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        exist_jockey = self.find_jockey_by_name(jockey_name)
        if exist_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        exist_race_type = self.find_race_by_type(race_type)
        if exist_race_type:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        if horse_type in self.HORSE_TYPES:
            jockey = self.find_jockey_by_name(jockey_name)
            if not jockey:
                raise Exception(f"Jockey {jockey_name} could not be found!")
            last_horse = self.find_last_not_taken_horse_by_type(horse_type)
            if not last_horse:
                raise Exception(f"Horse breed {horse_type} could not be found!")

            if jockey.horse != None:
                return f"Jockey {jockey_name} already has a horse."

            last_horse.is_taken = True
            jockey.horse = last_horse
            return f"Jockey {jockey_name} will ride the horse {last_horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        race = self.find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse == None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race.race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        race = self.find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        participants_in_race = len(race.jockeys)
        if participants_in_race < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = max(race.jockeys)
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
