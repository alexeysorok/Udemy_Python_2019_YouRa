# print('Some code')
# try:
#     print(var)
# except:
#     print('Some Error')
# print('Some after error')

# если есть ошибка except блок срабатывает, если нет ошибки работает else
number = input('Enter number')
try:
    print(number)
except:
    print('You have to enter a number')
else:
    print('Else block')
finally:
    print('Finally')
