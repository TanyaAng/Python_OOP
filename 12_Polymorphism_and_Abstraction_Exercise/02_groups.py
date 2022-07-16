class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    __index = 0

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.people):
            item = self.__index
            self.__index += 1
            return f"Person {item}: {self.people[item]}"
        raise StopIteration


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
print(p4)

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
