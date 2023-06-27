# listy - przechowuje niskonczona ilosc danych
# zachowuje kolejnosc dodania
lista = []
print(lista)  # []
lista.append("Radek")
lista.append("MAciek")
lista.append("Jaśko")
lista.append("Zenek")
print(lista)
# ['Radek', 'MAciek', 'Jaśko', 'Zenek']
# indeksy w liscie sa numerowane od 0
print(len(lista))  # 4
print(lista[0])
print(lista[1])  # MAciek
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])
print(lista[-2])
print(lista[0:3])  # ['Radek', 'MAciek', 'Jaśko'] od 0 do 2
print(lista[2:])  # ['Jaśko', 'Zenek']

# nadpisanie elementu na danym indeksie
lista[2] = "Mikołaj"
print(lista)
# ['Radek', 'MAciek', 'Mikołaj', 'Zenek']

# wstawienie elementu pomiedzy inne
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'MAciek', 'Mikołaj', 'Zenek']

# usunięcie elementu z listy
lista.remove("MAciek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Zenek']

indeks = lista.index('Zenek')
print(indeks)

# usuniecie po indeksie, zwroci element usuniety
print(lista.pop(3))  # Zenek
print(lista)  # ['Radek', 'Marcin', 'Mikołaj']

lista2 = lista  # tylko kopia referencji (odwołąnia),
# obie wskazuja na to samo miejsce w pamięci
print(lista2)
lista3 = lista.copy()  # prawidłowa kopia listy

lista.clear()
print(lista)  # []
print(lista2)  # []
print(lista3)  # ['Radek', 'Marcin', 'Mikołaj']

print("Radek" in lista3)  # True
# zmienna logiczna True/False
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # 1 - True
czy_znasz_pythona = False
print(int(czy_znasz_pythona))  # 0

x = 1
print(bool(x))  # True

x = 100
print(bool(x))
x = -10
print(bool(x))
x = 0
print(bool(x))  # False
x = 'radek'
print(bool(x))  # True
x = None
print(bool(x))  # False
x = ''
print(bool(x))  # False
x = []
print(bool(x))  # False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True or False)  # True
print(False or False)  # False
print(not True)  # False

a = 14
b = 3
print(f"Wynik porównania {a} > {b}", a > b)
# Wynik porównania 14 > 3 True
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)  # porównanie
print(f"Wynik porównania {a} != {b}", a != b)  # rożne

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
liczby.sort()
print(liczby)
# [12.34, 22, 34, 54, 687, 999]
print(type(liczby))  # <class 'list'>
lista_osoby = ['radek', 'ola']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek']

liczby.reverse()
print(liczby)
liczby[3] = 6666
print(liczby)  # [999, 687, 54, 6666, 22, 12.34]
print(liczby[0:3])
print(liczby[-2])
print(liczby[0:-2])
print(liczby[-3:])  # try od końca [6666, 22, 12.34]

liczby.remove(54)
print(liczby)

print(liczby.pop(3))
print(liczby)

print(len(liczby))

krotka = tuple(liczby)  # zamiana na krotke
print(krotka)  # (999, 687, 6666, 12.34)
