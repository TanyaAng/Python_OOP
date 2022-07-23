class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary_items = dictionary
        self.lenght = len(self.dictionary_items)
        self.keys = list(self.dictionary_items.keys())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.lenght:
            raise StopIteration
        key_to_return = self.keys[self.current]
        value_to_return = self.dictionary_items[key_to_return]
        self.current+=1
        return (key_to_return, value_to_return)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
