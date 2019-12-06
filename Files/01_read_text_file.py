my_text = open('sample.txt')
# for line in my_text:
#     print(line, end='')
# my_text.close()

for line in my_text:
    if 'let' in line.lower():  # если let входит в строку
        print(line, end='')
my_text.close()

with open('sample.txt') as text2:  # автоматически закроет файл
    for line in text2:
        if 'there' in line.lower():  # если let входит в строку
            print(line, end='')

with open('sample.txt') as text3:
    line = text3.readline()  # получаем все строки потрочно
    while line:
        print(line, end='')
        line = text3.readline()

with open('sample.txt') as text4:
    lines = text4.readlines()  # получаем все строки в виде списка
print(lines)

for line in lines:
    print(line)

with open('sample.txt') as text5:
    text_file = text5.read()  # весь текст из файла
print(text_file)

# рекомандация использовать readlines() в больших файлах чтобы не перегружать память компьютера








