from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @staticmethod
    def make_food_instance(food_type, name, price):
        if food_type == 'Bread':
            return Bread(name, price)
        elif food_type == 'Cake':
            return Cake(name, price)

    def find_food_by_name(self, name):
        food = [f for f in self.food_menu if f.name == name]
        if food:
            return food[0]

    @staticmethod
    def make_drink_instance(drink_type, name, portion, brand):
        if drink_type == 'Tea':
            return Tea(name, portion, brand)
        elif drink_type == 'Water':
            return Water(name, portion, brand)

    def find_drink_by_name(self, name):
        drink = [d for d in self.drinks_menu if d.name == name]
        if drink:
            return drink[0]

    @staticmethod
    def make_instance_of_table(table_type, table_number, capacity):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)

    def find_table_by_number(self, number):
        table = [t for t in self.tables_repository if t.table_number == number]
        if table:
            return table[0]

    def find_suitable_table(self, number_of_people):
        table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people]
        if table:
            return table[0]

    def add_food(self, food_type, name, price):
        food = self.find_food_by_name(name)
        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type in ('Bread', 'Cake'):
            food = self.make_food_instance(food_type, name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink = self.find_drink_by_name(name)
        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type in ('Tea', 'Water'):
            drink = self.make_drink_instance(drink_type, name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        table = self.find_table_by_number(table_number)
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type in ('InsideTable', 'OutsideTable'):
            table = self.make_instance_of_table(table_type, table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        table = self.find_suitable_table(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *foods):
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        food_not_in_menu = []
        for food_name in foods:
            food = self.find_food_by_name(food_name)
            if food:
                table.order_food(food)
            else:
                food_not_in_menu.append(food_name)
        result = f'Table {table_number} ordered:\n'
        for food in table.food_orders:
            result += repr(food) + '\n'
        result.strip()
        result += f'{self.name} does not have in the menu:\n'
        for food_name in food_not_in_menu:
            result += food_name + '\n'
        return result.strip()

    def order_drink(self, table_number, *drinks):
        table = self.find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        drink_not_in_menu = []
        for drink_name in drinks:
            drink = self.find_drink_by_name(drink_name)
            if drink:
                table.order_drink(drink)
            else:
                drink_not_in_menu.append(drink_name)
        result = f"Table {table_number} ordered:\n"
        for drink in table.drink_orders:
            result += repr(drink) + '\n'
        result.strip()
        result += f'{self.name} does not have in the menu:\n'
        for drink_name in drink_not_in_menu:
            result += drink_name + '\n'
        return result.strip()

    def leave_table(self, table_number):
        table = self.find_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.is_reserved = False
            table.clear()
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for t in self.tables_repository:
            if not t.is_reserved:
                result += t.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
