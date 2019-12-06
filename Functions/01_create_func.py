def print_greeting():
    '''
    Print 'Hello' text
    :return: None
    '''
    print('Hello')


print_greeting()
# вызов документации
help(print_greeting)


def print_greeting_with_name(name='Name'):
    '''
    :param name
    :return: None
    '''
    print('Hello ' + name + '!')


print(print_greeting_with_name('Alex'))
print(print_greeting_with_name())
help(print_greeting_with_name)


def sum_of_two_numbers(a=0, b=0):
    '''

    :param a:
    :param b:
    :return: Sum of a and b
    '''
    return a + b


def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


def is_hello_in_text2(text):
    return 'hello' in text.lower()


def is_string_in_text(string, text):
    return string in text


# print(is_string_in_text('he', 'The apple'))

# print(is_hello_in_text('Say Hello everihing'))
# print(is_hello_in_text('Say Brand'))
def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        print('Hello ' + name + '!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + '!')
        return gender


return_value = greeting_depends_on_gender('Alex', 'male')
print(return_value)



