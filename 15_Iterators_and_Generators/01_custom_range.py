class custom_range_iterator:
    def __init__(self, cr):
        self.cr = cr
        self.next_value = self.cr.start

    def __next__(self):
        if self.next_value > self.cr.end:
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


class custom_range_with_generator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        value = self.start
        while value < self.end:
            yield value
            value += 1


one_to_ten = custom_range_with_generator(3, 10)
for num in one_to_ten:
    print(num)
