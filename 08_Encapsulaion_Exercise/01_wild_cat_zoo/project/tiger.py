from project.animal import Animal


class Tiger(Animal):
    TIGER_MONEY_FOR_CARE = 45

    def __init__(self, name, gender, age, money_for_care=TIGER_MONEY_FOR_CARE):
        super().__init__(name, gender, age, money_for_care)