import csv

with open('students1.csv', 'w') as file:
    headers = ['First name', 'Last name', 'Age']
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        'First name': 'Jack',
        'Last name': 'White',
        'Age': 24})
