from functools import wraps


def type_check(param_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            params = []
            if args:
                [params.append(x) for x in args]
            if kwargs:
                [params.append(x) for x in kwargs.items()]
            for p in params:
                if not isinstance(p, param_type):
                    return f"Bad Type"
            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

