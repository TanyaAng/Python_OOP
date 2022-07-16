from project.cat import Cat


class Kitten(Cat):
    __gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.__gender)

    def make_sound(self):
        return "Meow"
