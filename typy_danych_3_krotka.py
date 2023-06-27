# krotka - niemutowalna, zmienna, niezmienna
tupla = ("radek",)
print(type(tupla))  # <class 'tuple'>

tupla2 = "Tomek", "Asia", "Zbyszek", "Marcin"
print(type(tupla2))  # <class 'tuple'>
tupla3 = (43, 55, 22.34, 11, 200)
tupla4 = 37, 5
print(type(tupla4))
print(type(tupla3))  # <class 'tuple'>
print(tupla2.count("Tomek"))
print(tupla2.index("Asia"))

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

a, *b = 1, 2, 3
print(a)
print(b)
# rozpakowanie tupli

tupla2 = "Tomek", "Asia", "Zbyszek", "Marcin"

imie1, *imie2, imie3 = tupla2
print(imie2)  # ['Asia', 'Zbyszek']
print(type(imie2))

lista = list(tupla2)
print(lista)  # ['Tomek', 'Asia', 'Zbyszek', 'Marcin']
