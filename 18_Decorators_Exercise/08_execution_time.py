from time import time
from functools import wraps


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(end - start)
        return result

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
#
#
# print(concatenate(["a" for i in range(1000000)]))
#
#
# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
#
#
# print(loop())
