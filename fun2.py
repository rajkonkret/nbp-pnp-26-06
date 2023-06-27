# funkcje zwracające wynik

def dodaj(a, b):
    return a + b  # zwroc, odeslij wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

zm = oblicz_vat(1000)
print(zm)
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Prawidłowo")
else:
    print("Błąd")
