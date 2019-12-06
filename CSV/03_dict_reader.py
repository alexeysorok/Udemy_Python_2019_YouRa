import csv

# вызов по ключам
with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)
    for item in csv_reader:
        print(f'{item["Make"]} {item["Model"]} cost {item["Price"]}')


