# lambda - skrocony zapis funkcji
odejmij = lambda a, b: a - b  # domyslnie zwraca wartosc
print(odejmij(6, 7))

# def odemij(a, b):
#     return a - b

wiek = lambda x: "dziecko" if x < 10 else \
    ("nastolatek" if x < 18 else "dorosły")

print(wiek(5))
print(wiek(15))
print(wiek(25))
# kwargs {'user': 'radek'}

lista = [1, 2, 3, 4, 545, 67, 23]
# map()
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 1090, 134, 46]

# filter() - filtrowanie danych wg wzorca
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1, 2]
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
# 3 x > 3 i x < 20  =  3 < x < 20
# Zastosowanie filter: [4]