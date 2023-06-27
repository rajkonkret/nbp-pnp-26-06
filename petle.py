# for  - petla iterujaca
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    pass
lista2 = list(range(1, 50))

for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzysta")

# 0 jest parzysta
# 2 jest parzysta
# 4 jest parzysta
# 6 jest parzysta
# 8 jest parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)
# [0, 2, 4, 6, 8]
for c in lista3:
    if c == 2:
        c += 1  # c = c +1
    print(c)

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)

# wyswietlic elemrnty tej listy
# 0 Radek
# 1 Asia

for i in range(len(imiona)):  # 0..3 bo len = 4 range(4)
    print(i, imiona[i])

# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

# enumerate = zwraca ponumerowaną kolekcje
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Asia')
# (2, 'Zbyszek')
# (3, 'Marcin')

for p, w in enumerate(imiona):
    print(p, w, sep=";", end=" ")
# sep=  - separator miedzy wyrazami po przecinku
# end= - znak końca linii

ludzie = ['Radek', 'Zenek', 'Asia', 'Marcin', 'Franek']
wiek = [47, 67, 34, 32]
jezyk = ['java', 'python']
print()
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # IndexError: list index out of range

# zip - łaczy kolekcje
for o, w in zip(ludzie, wiek):
    print(o, w)

for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)
# Radek 47 java
# Zenek 67 python

for i, w in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, w)
# 0 ('Radek', 47, 'java')
# 1 ('Zenek', 67, 'python')
for i, (l, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, l, w, j)

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
print(zipped)

for item in zipped:
    print(item)

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # ujemny krok, petla idzie do tyłu
    print(i)
