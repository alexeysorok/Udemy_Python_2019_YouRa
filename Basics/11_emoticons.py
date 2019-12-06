# smile = '\U0001f600'
# print(smile)

for num in range(10):
    count = 0
    emoticons = ''
    while count <= num:
        emoticons += '\U0001f600'
        count += 1
    print(emoticons)

for num in range(1, 11):
    print('\U0001f600' * num)
