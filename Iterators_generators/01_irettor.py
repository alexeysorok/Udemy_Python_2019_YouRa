# список можно перебрать
number_list = [1, 2, 3, 4, 5]
for number in number_list:
    print(number)
# строка тоже
for letter in 'my string':
    print(letter)

number_list_iterator = iter(number_list)
print(number_list_iterator)

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration


first_range = MyRange(20, 30)
for number in first_range:
    print(number)

def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


print(count_up_to(4))
counter = count_up_to(4)
print(counter.__next__())
print(counter.__next__())

for num in count_up_to(10):
    print(num)


def get_current_pattern():
    patterns = ('First', 'Two', 'Third')
    i = 0
    while True:
        if i >= len(patterns):
            i = 0;
        yield patterns[i]
        i += 1

# создаются не все элементы скопом а по одному не расходуя память
current_pattern = get_current_pattern()
current_pattern.__next__()
# бесконечный список и не большая нагрузка для памяти и процессора

print(sum([number for number in range(10)]))
# создается цедиком массив
print(sum(number for number in range(10)))
#  1 элемент в момент времени

import time

# list_start_time = time.time()
# print(sum([number for number in range(100000000)]))
# list_processing_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum(number for number in range(100000000)))
gen_processing_time = time.time() - gen_start_time

# print(f'Processing with list is {list_processing_time}')
print(f'Processing with generator is {gen_processing_time}')

# на windows работает медленее кстати
