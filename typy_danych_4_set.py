# set - (zbiór) - przechowuje niezduplikowane elementy
# tracimy kolejnosc przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # tworzenie seta
print(zbior)
print(type(zbior))  # <class 'set'>
# {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # pusty zbiór
print(zb2)  # set()
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

zbior.remove(55)
print(zbior)

print(zbior.pop())  # usuniecie pierwszego
print(zbior)
# {66, 777, 11, 44, 18, 22}
print(zbior.pop())  # 66
print(zbior)

zbior.pop()
print(zbior)
# {11, 44, 18, 22}

lista2 = list(zbior)
print(lista2)  # [11, 44, 18, 22]
print(type(lista2))  # <class 'list'>

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

print(zbior | zbior2)  # suma zbiorów {66, 999, 11, 44, 18, 52, 22, 62}
print(zbior & zbior2)  # częśc wspólna {18, 11, 44}
print(zbior - zbior2)  # różnica {22}
print(zbior2 - zbior)  # {66, 52, 62, 999}

print(zbior.difference(zbior2))  # {22}
print(zbior2.difference(zbior))  # {66, 52, 62, 999}
