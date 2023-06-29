from pprint import pprint

import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = re.get(url)
print(response)

# <Response [200]> - ok
# 3xx - dziwne błędy
# 4xx - grube błedy np.: 404 - brak zasobu
# 5Xx - błedy wewnętrzne serwera

table = response.json()
print(table)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '124/A/NBP/2023', 'effectiveDate': '2023-06-29', 'mid': 4.0832}]}
print(table.keys())
# dict_keys(['table', 'currency', 'code', 'rates'])

print(table['table'])  # A
print(table['currency'])  # dolar amerykański
print(table['code'])  # USD
print(table['rates'])
# [{'no': '124/A/NBP/2023', 'effectiveDate': '2023-06-29', 'mid': 4.0832}]
print(table['rates'][0])
# {'no': '124/A/NBP/2023', 'effectiveDate': '2023-06-29', 'mid': 4.0832}
print(table['rates'][0]['mid'])  # 4.0832

# url2 = 'http://api.nbp.pl/api/cenyzlota'
url2 = 'http://api.nbp.pl/api/cenyzlota/last/10'
response = re.get(url2)
print(response)  # [{'data': '2023-06-29', 'cena': 249.85}]

gold = response.json()
print(gold)
# [{'data': '2023-06-16', 'cena': 258.63}, {'data': '2023-06-19', 'cena': 256.55}, {'data': '2023-06-20', 'cena': 255.19},
#  {'data': '2023-06-21', 'cena': 251.88}, {'data': '2023-06-22', 'cena': 251.65}, {'data': '2023-06-23', 'cena': 248.96},
#  {'data': '2023-06-26', 'cena': 253.82}, {'data': '2023-06-27', 'cena': 251.42}, {'data': '2023-06-28', 'cena': 249.73},
#  {'data': '2023-06-29', 'cena': 249.85}]

for i in gold:
    print(i)

pprint(gold)