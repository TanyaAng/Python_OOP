from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    initial_members = 2
    appliances_type = (TV, Fridge, Laptop)

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, self.initial_members + len(children))
        self.children = children
        self.appliances = self.generate_appliances(*self.appliances_type)
        self.calculate_expenses(self.appliances, self.children)


