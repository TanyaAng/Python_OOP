from functools import wraps


def cache(func):
    memo = {}

    @wraps(func)
    def wrapper(n):
        if n in memo:
            return memo[n]
        result = func(n)
        memo[n]=result
        return result
    wrapper.log=memo
    return wrapper


@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(12))
print(fibonacci.log)
