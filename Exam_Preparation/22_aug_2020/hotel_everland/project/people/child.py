class Child:
    DAYS_PER_MONTH = 30

    def __init__(self, food_cost, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.DAYS_PER_MONTH * self.cost
