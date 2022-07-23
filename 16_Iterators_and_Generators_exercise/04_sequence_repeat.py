class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.idx = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        if self.idx >= len(self.sequence):
            self.idx = 0
        value = self.sequence[self.idx]
        self.idx += 1
        self.counter += 1
        return value


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end='')
