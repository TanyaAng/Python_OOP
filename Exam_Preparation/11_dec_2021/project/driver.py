class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def win_race(self):
        self.number_of_wins += 1

    def take_the_car(self, car):
        self.car=car
        self.car.is_taken=True

    def message_when_win_the_race(self, race_name):
        self.win_race()
        return f"Driver {self.name} wins the {race_name} race with a speed of {self.car.speed_limit}."



