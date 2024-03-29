from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN = 50

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE

    def increase_oxygen(self, amount):
        self.oxygen += amount

