from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = 'Express'
    MEMORY_CONSUMPTION_COEFF = 2

    def __init__(self, name, capacity_consumption, memory_consumption):
        memory_consumption = self.MEMORY_CONSUMPTION_COEFF * memory_consumption
        super().__init__(name,self.TYPE, capacity_consumption, memory_consumption)

