# plik csv - sa to pliki, gdzie dane są oddzielone znakiem podziału

import csv

fields = ['name', 'branch', 'year', 'cgpa']

dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': "Radek"},
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': "Radek"},
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': "Radek"},
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': "Radek"},
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': "Radek"},
]

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict)
