dictionary = {'imie': 'Radek', 'nazwisko': 'kowalski'}

print(type(dictionary))

# wydrukuje klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => kowalski

dictionary2 = {'name': 'imie', 'company': 'NBP'}
print(dictionary2)
print({value: key for key, value in dictionary2.items()})
# {'name': 'imie', 'company': 'NBP'}
# {'imie': 'name', 'NBP': 'company'}

d2 = {}
for k, v in dictionary2.items():
    d2[v] = k
print(d2)
# {'imie': 'name', 'NBP': 'company'}
