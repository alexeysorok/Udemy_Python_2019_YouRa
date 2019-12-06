# *args - arguments - договоренность так называть
# **kwargs - key word arguments - агрументы по ключевому слову
# используются чтобы получать в качестве парметров произвольное кол-во параметров


def ten_percent_of_product(x, y):
    return x * y * 0.1


def ten_percent_of_product_with_args(*args):  # *args use tuple
    product = 1
    for number in args:
        product = product * number
    return product * 0.1


def percent_of_product_with_args(percent, *args):  # *args use tuple
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent


def func_with_kwargs(**kwargs):  # передаются пары ключ значение
    print(kwargs)


# используются словари
print(func_with_kwargs(first=1))
# result {'first': 1}


def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:  # если в последовательности есть ключ name
        print('Hello! Nice to meet you, {}'.format(kwargs['name']))
    else:
        print('Hello! What is your name?')


# ключ значение
hello_with_kwargs(gender='male', age=24, name='Alex')

# print(ten_percent_of_product(10, 20))
# print(ten_percent_of_product_with_args(10, 20))
# print(percent_of_product_with_args(20, 20, 20))


def func_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}.'.format(args[0], kwargs['food']))
    print(kwargs)


func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')
