def logged(func):
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper


@logged
def func(*args, **kwargs):
    return 3 +len(args) + len(kwargs)

x=func(4,4,4,b=4)
print(x)