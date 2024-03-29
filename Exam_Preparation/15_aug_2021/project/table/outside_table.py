from project.table.table import Table


class OutsideTable(Table):
    TABLE_NUMBER_RANGE = range(51, 101)

    def __init__(self, table_number, capacity):
        super().__init__(table_number,capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value not in self.TABLE_NUMBER_RANGE:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number=value


