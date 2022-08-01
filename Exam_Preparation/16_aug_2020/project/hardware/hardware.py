class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if software.capacity_consumption > self.capacity or software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    def find_all_installed_express_software(self):
        express_software = [s for s in self.software_components if s.__class__.__name__ == 'ExpressSoftware']
        if express_software:
            return express_software

    def find_all_installed_light_software(self):
        light_software = [s for s in self.software_components if s.__class__.__name__ == 'LightSoftware']
        if light_software:
            return light_software

    def total_memory_of_all_softwares(self):
        total_memory = 0
        for s in self.software_components:
            total_memory += s.memory_consumption
        return total_memory

    def total_capacity_of_all_softwares(self):
        total_capacity = 0
        for s in self.software_components:
            total_capacity += s.capacity_consumption
        return total_capacity

    def __str__(self):
        express_software = self.find_all_installed_express_software()
        if express_software:
            count_of_express_software = len(express_software)
        else:
            count_of_express_software = 0

        light_software = self.find_all_installed_light_software()
        if light_software:
            count_of_light_software = len(light_software)
        else:
            count_of_light_software = 0

        software_names = [s.name for s in self.software_components]
        if not software_names:
            software_names = 'None'

        return f"Hardware Component - {self.name}\n" \
               f"Express Software Components: {count_of_express_software}\n" \
               f"Light Software Components: {count_of_light_software}\n" \
               f"Memory Usage: {self.total_memory_of_all_softwares()} / {self.memory}\n" \
               f"Capacity Usage: {self.total_capacity_of_all_softwares()} / {self.capacity}\n" \
               f"Type: {self.hardware_type}\n" \
               f"Software Components: {', '.join(software_names)}"
