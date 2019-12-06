class Car:
    wheels_number = 4

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def drive(self, city):  # метод выполняется для каждого созданного объекта
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color


opel_car = Car('Opel Tigra', 'red', 1985)
opel_car.drive('London')
opel_car.change_color('green')
print(opel_car.color)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius **2)


circle1 = Circle(3)
print(circle1.get_area())


# методы класса
class Gamer:
    active_gamers = 0

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    # метод класса
    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permissions(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')

    def log_out(self):
        Gamer.active_gamers -= 1


gamer_1 = Gamer('Gosh', 18, 1, 0)
gamer_2 = Gamer('Gari', 7, 7, 10)

print(gamer_1.get_age())
gamer_1.get_adult_level_permissions()
print(Gamer.active_gamers)
gamer_1.log_out()
print(Gamer.active_gamers)
print(Gamer.get_active_gamers())


james = Gamer.gamer_from_string('Jhon, 34, 2, 45')
print(james.nickname)

my_dict = dict.fromkeys((1,2,3), ('aple', 'orange', 'banana'))
print(my_dict)
# значение присвется каждому элементу в словаре 












