from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 50
    FISH_TYPES = ('FreshwaterFish',)

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)
