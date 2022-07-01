class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        free_spaces = self.calculate_free_spaces()
        if free_spaces <= 0:
            return f"Not enough space"
        self.animals.append(animal_name)
        self.add_animal_to_vet_space(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if not self.remove_animal_from_vet_space(animal_name):
            return f"{animal_name} not in the clinic"
        self.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        free_spaces = self.calculate_free_spaces()
        return f"{self.name} has {len(self.animals)} animals. {free_spaces} space left in clinic"

    def calculate_free_spaces(self):
        return Vet.space - len(Vet.animals)

    def add_animal_to_vet_space(self, animal):
        Vet.animals.append(animal)

    def remove_animal_from_vet_space(self, animal):
        if animal in Vet.animals:
            Vet.animals.remove(animal)
            return True
        return False


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
