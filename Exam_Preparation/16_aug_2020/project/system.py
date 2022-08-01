class System:
    def __init__(self):
        self._hardware=[]
        self._software=[]

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        pass

    @staticmethod
    def register_heavy_hardware(name,capacity, memory):
        pass

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        pass

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        pass

    @staticmethod
    def release_software_component(hardware_name, software_name):
        pass

    @staticmethod
    def analyze():
        pass

    @staticmethod
    def system_split():
        pass

