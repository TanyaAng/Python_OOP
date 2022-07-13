class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def is_found_customer(self, customer_id):
        customer = [c for c in self.customers if c.id == customer_id]
        if customer:
            return customer[0]

    def is_found_dvd(self, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id]
        if dvd:
            return dvd[0]

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        if self.is_found_customer(customer_id) and self.is_found_dvd(dvd_id):
            customer = self.is_found_customer(customer_id)
            dvd = self.is_found_dvd(dvd_id)
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            if dvd.is_rented:
                return f"DVD is already rented"
            if customer.age < dvd.age_restriction:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        if self.is_found_customer(customer_id) and self.is_found_dvd(dvd_id):
            customer = self.is_found_customer(customer_id)
            dvd = self.is_found_dvd(dvd_id)
            if dvd in customer.rented_dvds:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += repr(c) + '\n'
        for dvd in self.dvds:
            result += repr(dvd) + '\n'
        return result.strip()


from project.customer import Customer
from project.dvd import DVD
# from project.movie_world import MovieWorld

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)

