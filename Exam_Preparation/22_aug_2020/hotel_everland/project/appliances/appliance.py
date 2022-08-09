class Appliance:
    DAYS_PER_MONTH = 30

    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        return self.DAYS_PER_MONTH * self.cost


