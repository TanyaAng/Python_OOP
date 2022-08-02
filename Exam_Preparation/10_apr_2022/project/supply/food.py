from project.supply.supply import Supply


class Food(Supply):
    INITIAL_ENERGY = 25

    def __init__(self, name):
        super().__init__(name, self.INITIAL_ENERGY)
