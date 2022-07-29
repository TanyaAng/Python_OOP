from functools import wraps


def store_results(func):
    DEFAULT_FILE = "result.txt"

    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(DEFAULT_FILE, 'a') as file:
            result = func(*args, **kwargs)
            file.write(f"Function '{func.__name__}' was called. Result: {result}\n")
        return result

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
