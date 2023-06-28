import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as f:
    csvreader = csv.reader(f, delimiter=";")
    print(type(csvreader))  # <class '_csv.reader'>

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)
# [['Radek', 'COE', '2', '9.1'], ['Radek', 'COE', '2', '9.1'], ['Radek', 'COE', '2', '9.1'], ['Radek', 'COE', '2', '9.1'],
#  ['Radek', 'COE', '2', '9.1']]
# python csv_test.py