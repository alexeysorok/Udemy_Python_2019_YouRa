# импортирование всего модуля
import random
x = random.randint(1, 10)
print(x)

# импортирование только функции
from random import randint
z = randint(1, 100)
print(z)

my_list = [1, 2, 3]
random.shuffle(my_list)  # перемешать массив
print(my_list)

# назвать функцию по своему
from random import shuffle as s
s(my_list)

