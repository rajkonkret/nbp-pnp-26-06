# funkcje
a = 4
b = 8


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


dodaj()
dodaj2(5, 6)
odejmij(4, 5)
odejmij(4, 5, 8)
odejmij(b=6, a=9, c=10)
print(dodaj())