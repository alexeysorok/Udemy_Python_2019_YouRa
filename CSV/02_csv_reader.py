import csv

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     for car in csv_reader:
#         # print(car)
#         print(f'{car[1]} {car[2]} cost:{car[4]}')

with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)
    print(data_list)


