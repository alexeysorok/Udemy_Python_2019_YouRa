#  доступ к значению по ключу
car_prices = {'opel': 5000, 'bmw': 10000}
print(car_prices)
print(car_prices['bmw'])
car_prices['mazda'] = 4000
print(car_prices)
del car_prices['opel']
car_prices.clear()  # пустой удалить все

person = {
    'first name':  'Jack',
    'last name': 'Brown',
    'age': 23,
    'hobbies': ['football', 'game']
}
print(person['age'])
print(person['hobbies'][1])
print(person.keys())
print(person.values())

name_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value ** 3 for key, value in name_dict.items()}
print(new_dict)

