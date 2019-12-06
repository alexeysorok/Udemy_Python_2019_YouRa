from functools import wraps


def print_function_data(function):
    @wraps(function)  # чтобы наша функция не теряла документацию
    def wrapper(*args, **kwargs):
        print(f'You are using {function.__name__}')
        print(f'Func documentation {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    return a * a + b * b


print(squares_sum(2, 3))
print(squares_sum.__name__)
help(squares_sum)

