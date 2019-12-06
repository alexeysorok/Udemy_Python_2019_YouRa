# def simple_function():
#     print('Simple function code')
#
#
# # хотим расширить функцию
# simple_function()
#

# def decorator_function(original_function):
#     def wrap_function():
#         print('Some code before the old code')
#         original_function()
#         print('Some code after the old code')
#     return wrap_function
# 
# 
# # decorated_function = decorator_function(simple_function)
# # decorated_function()
# 
# @decorator_function
# def simple_function():
#     print('Simple function code')
# 
# 
# simple_function()
# # добавились методы из функции декоратора


def make_compliment(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet you!')
        func(*args, **kwargs)
        print('Yoy greet')
    return wrapper


@make_compliment
def ask_me():
    print('What is you name')

ask_me()

@make_compliment
def say_name(name):
    print('My name is ' + name )


say_name('Alex')

@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')


order('chip', 'cola')


