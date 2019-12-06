# кортежи. Не изменяемый
tuple_1 = (1, 2, 4)
tuple_2 = ('word',)
x, y, z, = 11, 12, 13
person_tuple = ('John', 'Smith', 1986)
# распаковкка переменных
first_name, last_name, birth = person_tuple
print(first_name, last_name, birth)
print(person_tuple.count(1986))  # сколько раз встрачается

