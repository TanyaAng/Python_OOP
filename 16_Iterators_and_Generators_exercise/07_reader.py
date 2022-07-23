def read_next(*args):
    for arg in args:
        for el in arg:
            yield el


reader = read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4})
for item in reader:
    print(item, end='')
