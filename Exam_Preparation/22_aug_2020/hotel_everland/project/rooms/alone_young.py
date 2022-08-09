from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_cost = 10
    members = 1
    appliances_type = (TV,)

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, self.members)
        self.appliances = self.generate_appliances(*self.appliances_type)
        self.calculate_expenses(self.appliances)

    # def calculate_expenses(self):
    #     result = 0
    #     for item in self.appliances:
    #         result += item.get_monthly_expense()
    #     self.expenses = result
