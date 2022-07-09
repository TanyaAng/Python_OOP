from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def find_by_name(self, collection, name):
        searched_instance = [elem for elem in collection if elem.name == name]
        if searched_instance:
            return searched_instance[0]

    def sum_workers_salary(self):
        return sum([worker.salary for worker in self.workers])

    def sum_animals_money_for_care(self):
        return sum([animal.money_for_care for animal in self.animals])

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        searched_worker = self.find_by_name(self.workers, worker_name)
        if not searched_worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(searched_worker)
        return f"{searched_worker.name} fired successfully"

    def pay_workers(self):
        if self.__budget < self.sum_workers_salary():
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= self.sum_workers_salary()
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        if self.__budget < self.sum_animals_money_for_care():
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= self.sum_animals_money_for_care()
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [repr(animal) for animal in self.animals if animal.__class__.__name__ == 'Lion']
        tigers = [repr(animal) for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [repr(animal) for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        result = f"You have {len(self.animals)} animals\n"
        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs)
        return result.strip()

    def workers_status(self):
        keepers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vets = [repr(worker) for worker in self.workers if worker.__class__.__name__ == 'Vet']
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets)
        return result.strip()
