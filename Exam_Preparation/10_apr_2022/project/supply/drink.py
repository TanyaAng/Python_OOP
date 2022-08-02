from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_ENERGY = 15

    def __init__(self, name, energy=INITIAL_ENERGY):
        self.name = name
        self.energy = energy
