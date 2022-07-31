class Planet:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items.split(', ') if items != [] else []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value


planet = Planet("Earth", "stone, water")
print(planet.__dict__)
planet2 = Planet("Mars")
print(planet2.__dict__)
