from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def make_instance_of_car(car_type, model, speed_limit):
        if car_type == 'MuscleCar':
            return MuscleCar(model, speed_limit)
        elif car_type == 'SportsCar':
            return SportsCar(model, speed_limit)

    def find_car_by_model(self, model):
        car = [c for c in self.cars if c.model == model]
        if car:
            return car[0]

    def find_available_car_by_type(self, car_type):
        cars = [car for car in self.cars if car.__class__.__name__ == car_type and car.is_taken == False]
        if cars:
            return cars

    def find_driver_by_name(self, name):
        driver = [d for d in self.drivers if d.name == name]
        if driver:
            return driver[0]

    def find_race_by_name(self, name):
        race = [r for r in self.races if r.name == name]
        if race:
            return race[0]

    def create_car(self, car_type, model, speed_limit):
        if self.find_car_by_model(model):
            raise Exception(f"Car {model} is already created!")
        if car_type in ('MuscleCar', 'SportsCar'):
            car = self.make_instance_of_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if self.find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if self.find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_cars = self.find_available_car_by_type(car_type)
        if not available_cars:
            raise Exception(f"Car {car_type} could not be found!")

        last_added_car = available_cars[-1]
        if driver.car is not None:
            previous_car = driver.car
            driver.car.is_taken = False
            driver.car = None
            driver.take_the_car(last_added_car)
            return f"Driver {driver_name} changed his car from {previous_car.model} to {last_added_car.model}."
        driver.take_the_car(last_added_car)
        return f"Driver {driver_name} chose the car {last_added_car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car == None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = [driver for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit)][0:3]
        result = ''
        for driver in fastest_drivers:
            result += driver.message_when_win_the_race(race_name) + '\n'
        return result.strip()


