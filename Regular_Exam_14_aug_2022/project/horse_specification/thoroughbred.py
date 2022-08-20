from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREMENT = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        new_speed = self.speed + self.SPEED_INCREMENT
        if new_speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed = new_speed
