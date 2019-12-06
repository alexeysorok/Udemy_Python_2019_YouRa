#  функции высшего порядке, могут приниммать функции или возвращать функции


def product(n, func):  # произведение
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


def cube(x):
    return x * x * x


print(product(4, square))
print(product(4, cube))


def my_function(a, b, func):  # функция в качестве параметра
    result = func([a, b])
    return result


print(my_function(7, 3, sum))

# вложенная функция

from random import choice


def colorized(thing):
    def get_color():
        colors = ('red', 'green', 'blue')
        color = choice(colors)
        return color
    result = get_color() + ' ' + thing
    return result


print(colorized('aple'))


def make_color():
    def get_color():
        colors = ('red', 'green', 'blue')
        color = choice(colors)
        return color
    return get_color  # вернуть функцию 


color = make_color()
print(color())  # странный вызов но он работает


