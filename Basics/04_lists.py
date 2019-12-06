number_list = [1, 2, 4, 5, 45, 89]
some_list = [1, 'fd', 3.6]
print(len(some_list))
print(some_list[1])
print(some_list[:2])
some_list[2] = 'some text'
print(some_list)
some_list.append('other item')
some_list.insert(0, 'one')
print(some_list)
# del
some_list.pop()
some_list.remove('one')
print(some_list)

greeting = 'hello'
letter_list = [letter for letter in greeting]
print(letter_list)
number_list = [number for number in '0123456789']
print(number_list)
number_list1 = [number for number in range(10)]
print(number_list1)
number_list2 = [num ** 2 for num in range(10)]
print(number_list2)

num_list = [5, 6, -90, 76]
new_list = [num for num in num_list if num > 0]
print(new_list)
