from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def find_hardware_by_name(name):
        hardware = [h for h in System._hardware if h.name == name]
        if hardware:
            return hardware[0]

    @staticmethod
    def find_software_by_name(name):
        software = [s for s in System._software if s.name == name]
        if software:
            return software[0]

    @staticmethod
    def calc_total_memory_of_softwares():
        total_memory = 0
        for software in System._software:
            total_memory += software.memory_consumption
        return total_memory

    @staticmethod
    def calc_total_memory_of_hardwares():
        total_memory = 0
        for hardware in System._hardware:
            total_memory += hardware.memory
        return total_memory

    @staticmethod
    def calc_total_capacity_of_softwares():
        total_capacity = 0
        for software in System._software:
            total_capacity += software.capacity_consumption
        return total_capacity

    @staticmethod
    def calc_total_capacity_of_hardwares():
        total_capacity = 0
        for hardware in System._hardware:
            total_capacity += hardware.capacity
        return total_capacity

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.find_hardware_by_name(hardware_name)
        if not hardware:
            return f"Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.find_hardware_by_name(hardware_name)
        if not hardware:
            return f"Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = System.find_hardware_by_name(hardware_name)
        software = System.find_software_by_name(software_name)
        if not hardware or not software:
            return f"Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {System.calc_total_memory_of_softwares()} / {System.calc_total_memory_of_hardwares()}\n" \
               f"Total Capacity Taken: {System.calc_total_capacity_of_softwares()} / {System.calc_total_capacity_of_hardwares()}"

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += str(hardware) + '\n'
        return result.strip()
