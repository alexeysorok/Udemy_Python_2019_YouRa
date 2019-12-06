color_list = ['red', 'orange', 'green', 'indigo']

with open('color.txt', 'w') as list_color:
    for color in color_list:
        print(color, file=list_color)
