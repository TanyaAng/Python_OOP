from itertools import permutations

def possible_permutations(items):
    for per in permutations(items):
        yield list(per)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
