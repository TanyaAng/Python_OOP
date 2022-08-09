class Room:
    room_cost = 0
    appliances_type = ()

    # appliances = []

    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = self.generate_appliances(*self.appliances_type)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            for x in items:
                result += x.get_monthly_expense()
        self.expenses = result

    def generate_appliances(self, *args):
        appliances = []
        for type in args:
            for _ in range(self.members_count):
                appliances.append(type())
        return appliances

    def room_monthly_consumption(self):
        return self.expenses + self.room_cost

    def appliances_consumption(self):
        total = 0
        for item in self.appliances:
            total += item.get_monthly_expense()
        return total

    def __str__(self):
        result = f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$\n"
        if self.children:
            for idx, child in enumerate(self.children):
                result += f"--- Child {idx + 1} monthly cost: {child.get_monthly_expense():.2f}$\n"
        if self.appliances:
            result += f"--- Appliances monthly cost: {self.appliances_consumption():.2f}$\n"
        return result
