from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        params = []
        if args:
            [params.append(x) for x in args]
        if kwargs:
            [params.append(x) for x in kwargs.values()]
        # print(params)
        for p in params:
            if not isinstance(p,int) or p % 2 != 0:
                return f"Please use only even numbers!"
        return func(*args, **kwargs)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

@even_parameters
def func():
    return "hi"

print(func())


