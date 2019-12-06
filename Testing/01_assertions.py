#true
assert 2 + 2 == 4
# false
# assert 2 + 2 == 5, '2 + 2 mast equals 4'


# def divide(a, b):
#     assert b != 0, 'b must not equal 0'
#     return a / b
#
# print(divide(2, 0))

def multiply_positive_numbers(a, b):
    assert a > 0 and b > 0, 'a and b must be positive'
    print(a * b)


print(multiply_positive_numbers(1, -2))


