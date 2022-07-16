from project.animals.animal import Bird
from project.food import Meat, Vegetable


class Owl(Bird):
    __weight_increase = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Owl.__weight_increase*food.quantity
        self.food_eaten += food.quantity
        food.quantity=0


class Hen(Bird):
    __weight_increase = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += Hen.__weight_increase*food.quantity
        self.food_eaten += food.quantity
        food.quantity = 0



