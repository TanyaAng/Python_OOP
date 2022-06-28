class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value <= 0:
            self.__health = 0
        else:
            self.__health = value

    def defend(self, damage):
        self.health -= damage
        if self.health == 0:
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(120))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))
