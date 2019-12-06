# вызвать ошибку
# raise ValueError('Invalid value')
# raise  ValueError()


def get_rainbow_color(color_number):
    colot_number_list = [1, 2, 3, 4, 5]
    if color_number not in colot_number_list:
        raise ValueError()
    if color_number == 1:
        return 'red'
    elif color_number == 2:
        return 'green'


color = get_rainbow_color(7)
print(color)