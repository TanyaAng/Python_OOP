from project.software.software import Software
from math import floor




class LightSoftware(Software):
    TYPE = 'Light'
    CAPACITY_CONSUMPTION_COEFF = 1.50
    MEMORY_CONSUMPTION_COEFF = 0.50

    def __init__(self, name, capacity_consumption, memory_consumption):
        capacity_consumption = floor(self.CAPACITY_CONSUMPTION_COEFF * capacity_consumption)
        memory_consumption = floor(self.MEMORY_CONSUMPTION_COEFF * memory_consumption)
        super().__init__(name, self.TYPE, capacity_consumption, memory_consumption)


