class Player:
    MIN_STAMINA = 0
    MAX_STAMINA = 100
    INITIAL_STAMINA = 100
    __player_names = []

    def __init__(self, name, age, stamina=INITIAL_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name not valid!")
        if value in Player.__player_names:
            raise Exception(f"Name {value} is already used!")
        self.__name = value
        Player.__player_names.append(self.__name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def increase_stamina(self, supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy

    def decrease_stamina(self, value):
        if self.stamina - value < 0:
            self.stamina = 0
        else:
            self.stamina -= value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def __gt__(self, other):
        return self.stamina > other.stamina
