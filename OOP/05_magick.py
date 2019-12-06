# Special method
# как бы перегрузка метоодов

class Person:
    def __init__(self, firts_name, last_name, age):
        self.first_name = firts_name
        self.lat_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.lat_name}'

    def __len__(self):
        return self.age


don = Person('Don', 'White', 45)
print(don)
print(len(don))