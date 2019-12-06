class Car:
    # атрибут уровня класса
    wheels_number = 4

    def __init__(self, name, color, year):
        self.name = name  # атрибут уровня объекта
        self.color = color
        self.year = year
# init вызывается каждый раз когда создается объект класса


mazda_car = Car('Mazda CX7', 'red', 2017)
print(mazda_car.name)

bmw_car = Car('BMW', 'black', 2018)
bmw_car.wheels_number = 10
print(bmw_car.name, bmw_car.wheels_number)
# можно обращаться к атрибуту класса
print(Car.wheels_number)
