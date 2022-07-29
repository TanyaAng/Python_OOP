from functools import wraps

def tags(param):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            return f"<{param}>{func(*args,**kwargs)}</{param}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
