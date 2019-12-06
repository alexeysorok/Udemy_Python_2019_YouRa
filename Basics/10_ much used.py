for x in range(3, 11, 3):
    print(x)
print(range(5))
print(list(range(5)))

# enumerate()

# находится ли в
print('a' in 'jack')
letter_list = ['a', 'b', 'c']
print('a' in letter_list)

print(min(1, 3, 4))
print(max(3, 100, 1000))

from random import shuffle  # перетасовать
my_list = [1, 3, 5, 34]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(1, 10))


