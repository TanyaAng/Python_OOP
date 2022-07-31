from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_DECREASE = 5
    INITIAL_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= self.OXYGEN_DECREASE

    def increase_oxygen(self, amount):
        self.oxygen += amount
