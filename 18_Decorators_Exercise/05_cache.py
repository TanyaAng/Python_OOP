from functools import wraps


def cache(func):


    @wraps(func)
    def wrapper(n):
        wrapper.log[n] = func(n)
        return wrapper.log[n]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
