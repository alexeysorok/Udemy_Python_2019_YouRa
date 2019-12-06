greeting = "Hello!"
first_name = "Jack"
last_name = "White"
print(greeting + ' ' + first_name + ' ' + last_name)
print(len(greeting))  # длина
print(greeting[-1])
print(greeting[2:5])
print(greeting[::-1])  # перевернуть строку
print(greeting.upper())
print(greeting.lower())
print(greeting.split())  # разделяет по пробелам

# форматирование
name = "Jack"
age = 23
name_and_age = "My name is {0}. I\'m {1} years old.".format(name, age)
name_and_age2 = "My name is {0}. I\'m {1} years old.".format('Dan', 28)
name_and_age3 = "My name is {}. I\'m {} years old.".format('Ran', 30)
print(name_and_age)
week_days = "There are 7 days in a week: {mon}."\
    .format(mon="Monday")
print(week_days)

float_result = 1000 / 7
print('The result of division is {0:1.3f}'.format(float_result))

# new 3.6
name_and_age = f'My name is {name}. I\'m {age} years old'
print(name_and_age)

