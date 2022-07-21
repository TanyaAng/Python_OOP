class User:
    USER_RESTRICTION = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == '':
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.USER_RESTRICTION:
            raise ValueError(f"Users under the age of {self.USER_RESTRICTION} are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n"
        result += f"Liked movies:\n"
        if not self.movies_liked:
            result += f"No movies liked.\n"
        else:
            result += '\n'.join([movie.details() for movie in self.movies_liked])+'\n'

        result += f"Owned movies:\n"
        if not self.movies_owned:
            result += f"No movies owned.\n"
        else:
            result += '\n'.join([movie.details() for movie in self.movies_owned])
        return result
