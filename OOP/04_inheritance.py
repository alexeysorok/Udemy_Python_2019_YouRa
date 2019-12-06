class Car:
    wheels_number = 4

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
        print('Car is created')

    def drive(self, city):  # метод выполняется для каждого созданного объекта
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color


# наследование
class Truck(Car):
    # переопределение свойста в наследнике
    wheels_number = 6

    def __init__(self, name, color, year):
        Car.__init__(self, name, color, year)
        print('Truck is created')

    def drive(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)

    def load_cargo(self, weight):
        print('The cargo is loaded. Weight is ' +
              str(weight))


man_truck = Truck('Man', 'green', 1985)
# Car is created
# Truck is created
# создается сначало класс родитель метод init потом дочерний класс метод init

man_truck.change_color('red')
man_truck.drive('Moscow')
man_truck.load_cargo(2000)

# Polimorphism
# переопределение методов

# Чтобы гарантировать наличие методов у класса их объединяют и наследуют от родителя


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Class successor must implement this method') # выбрасывать ошиюку


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'is saying woof')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'is saying meow')


spike = Dog('Spike')
tom = Cat('Tom')

pet_list = [spike, tom]
for pet in pet_list:
    pet.speak()


def pet_voice(pet):
    pet.speak()


pet_voice(spike)

# множественное наследование, так как нет интерфейсов
class Swimmable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can swimming')

class Walkable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can walk')


class Flyable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can fly')


class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

# переопределяет все остальные мутоды
    def greeting(self):
        print(f'Hello! My name is {self.name}')
# если не переопрелять то сработает самый первый на первом месте


james = GameCharacter('James')
james.greeting()
#  !срабатывает метод определенный в первом классе который стоит в паметрах



