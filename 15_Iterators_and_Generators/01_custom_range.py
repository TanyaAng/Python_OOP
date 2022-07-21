class custom_range_iterator:
    def __init__(self, cr):
        self.next_value = cr.start
        self.end = cr.end

    def __next__(self):
        if self.next_value > self.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1
        return value_to_return


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_value = start

    def __iter__(self):
        return custom_range_iterator(self)


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
