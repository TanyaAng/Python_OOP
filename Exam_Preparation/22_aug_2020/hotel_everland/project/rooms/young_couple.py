from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    room_cost = 20
    members = 2
    appliances_type = (TV, Fridge, Laptop)

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, self.members)
        self.appliances = self.generate_appliances(*self.appliances_type)
        self.calculate_expenses(self.appliances)


