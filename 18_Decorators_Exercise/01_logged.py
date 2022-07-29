from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        params = []
        if args:
            [params.append(x) for x in args]
        if kwargs:
            [params.append(x) for x in kwargs.items()]
        # print(params)
        result = f"you called {func.__name__}({', '.join([str(x) for x in params])})\n"
        result += f"it returned {func(*args,**kwargs)}"
        return result
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
