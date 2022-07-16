from project.cat import Cat


class Tomcat(Cat):
    __gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.__gender)

    def make_sound(self):
        return "Hiss"
