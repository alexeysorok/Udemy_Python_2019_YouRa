# def sum_of_two_numbers(x):
#     return x + x
#
#
# number_list = [1, 2, 3, 4, 5, 6, 7]
# # хотим применить фугкцию для каждого элемента
#
# result = map(sum_of_two_numbers, number_list)
# print(result)
#
# for item in result:
#     print(item)


def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False


string_list = ['has', 'hi', 'mae']

# функция применена для каждого элемента из списка
print(list(map(is_a_in_string, string_list)))

# filter работает похожим образом, только возвращает такое значение
# которое при применении над ним функции дает True


def is_number_odd(number):
    return number % 2 == 1


number_list = [1, 2, 3, 4, 5, 6, 7]

print(list(filter(is_number_odd, number_list)))

# Lambda
# обычная функция
def cube(number):
    return number ** 3


# lambda используется один раз при запуске
# example: lambda number: number ** 3
print(list(map(lambda number: number ** 3, number_list)))

print(list(filter(lambda number: number % 2 == 1, number_list)))
print(list(filter(lambda number: number % 2 == 0, number_list)))








