from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    INITIAL_PORTION=200
    def __init__(self, name, price):
        super().__init__(name, self.INITIAL_PORTION, price)

