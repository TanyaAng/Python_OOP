from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED = 250
    MAX_SPEED = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)
