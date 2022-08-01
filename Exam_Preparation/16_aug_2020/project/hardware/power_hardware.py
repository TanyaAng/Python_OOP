from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    TYPE = 'Power'
    CAPACITY_COEFF = 0.25
    MEMORY_COEFF = 1.75

    def __init__(self, name, capacity, memory):
        capacity = floor(self.CAPACITY_COEFF * capacity)
        memory = floor(self.MEMORY_COEFF * memory)
        super().__init__(name, self.TYPE, capacity, memory)