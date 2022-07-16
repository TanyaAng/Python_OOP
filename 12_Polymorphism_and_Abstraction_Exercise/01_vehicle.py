from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.can_travel = True

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION_INCREASE_IN_SUMMER = 0.9

    def drive(self, distance):
        if (self.fuel_consumption + Car.CONSUMPTION_INCREASE_IN_SUMMER) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + Car.CONSUMPTION_INCREASE_IN_SUMMER) * distance
            self.can_travel = True
        else:
            self.can_travel = False

    def refuel(self, fuel):
        if self.can_travel:
            self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_INCRESE_IN_SUMMER = 1.6

    def drive(self, distance):
        if (self.fuel_consumption + Truck.CONSUMPTION_INCRESE_IN_SUMMER) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + Truck.CONSUMPTION_INCRESE_IN_SUMMER) * distance
            self.can_travel = True
        else:
            self.can_travel = False

    def refuel(self, fuel):
        if self.can_travel:
            self.fuel_quantity += 0.95 * fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
