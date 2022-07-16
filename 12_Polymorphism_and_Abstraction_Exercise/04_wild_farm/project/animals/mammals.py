from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    __weight_increase = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) or not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Mouse.__weight_increase * food.quantity
        self.food_eaten += food.quantity
        food.quantity = 0


class Dog(Mammal):
    __weight_increase = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Dog.__weight_increase * food.quantity
        self.food_eaten += food.quantity
        food.quantity = 0


class Cat(Mammal):
    __weight_increase = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) or not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Cat.__weight_increase * food.quantity
        self.food_eaten += food.quantity
        food.quantity = 0


class Tiger(Mammal):
    __weight_increase = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Tiger.__weight_increase * food.quantity
        self.food_eaten += food.quantity
        food.quantity = 0
