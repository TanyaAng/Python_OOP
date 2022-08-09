from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    members = 2
    appliances_type = (TV, Fridge, Stove)

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, self.members)
        self.appliances = self.generate_appliances(*self.appliances_type)
        self.calculate_expenses(self.appliances)


