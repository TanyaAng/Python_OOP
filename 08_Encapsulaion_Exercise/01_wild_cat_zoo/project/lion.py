from project.animal import Animal


class Lion(Animal):
    LION_MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age, money_for_care=LION_MONEY_FOR_CARE):
        super().__init__(name, gender, age, money_for_care)



