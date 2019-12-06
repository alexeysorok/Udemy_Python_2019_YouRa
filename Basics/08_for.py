numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
sum_numbers = 0
for number in numbers:
    sum_numbers = sum_numbers + number
print(sum_numbers)

greeting = 'Hello Python'
for letter in greeting:
    if letter == 'o':
        print(letter)

tuple_list = [('a', 'b'), ['c', 'd']]
for item in tuple_list:
    print(item)
for letter_one, letter_two in tuple_list:
    print(letter_one, letter_two)
# последовательность
for x in range(5):
    print(x)
# когда нужно просто повторить число раз  без переменной
for _ in range(5):
    print('Hello')
