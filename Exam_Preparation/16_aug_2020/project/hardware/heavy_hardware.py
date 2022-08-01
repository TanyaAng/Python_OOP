from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    TYPE = 'Heavy'
    CAPACITY_COEFF = 2
    MEMORY_COEFF = 0.75

    def __init__(self, name, capacity, memory):
        capacity=self.CAPACITY_COEFF*capacity
        memory=floor(self.MEMORY_COEFF*memory)
        super().__init__(name, self.TYPE, capacity,memory)
#