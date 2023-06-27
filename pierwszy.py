print()  # wyswietlenie na ekranie
print("Nazywam się Radek")
# ctrl- d - duplikuje linie w ktorej stoi kursor
# print('Nazywam się Radek')
# print('Nazywam się Radek')
# print('Nazywam się Radek')
# print('Nazywam się Radek')
# PEP 8
# ctrl /(?) - kkomentowanie zanaczonego tekstu
# ctrl - atl  - l - formatowanie kodu wg zasad PEP8

# type() - wypisanie typu
print(type("Radek"))  # <class 'str'>  string - typ tekstowy

print(39)
print(type(39))  # <class 'int'> integer - liczby calkowite

print("39" + "15")  # 3915 konkatenacja, łaczenie tekstów
print(39 + 14)  # matematyczne dodawanie

print(5 * "4")
# print(5 + "4")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

imie = "Radek"
print(imie)  # nazwa zmiennej podanae bez cudzysłowia
print(type(imie))  # <class 'str'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>

# str() - rzutowanie (zamiana) na typ str
print(imie + str(wiek))  # Radek48

wiek = "Radek"
print(wiek)
print(type(wiek))  # <class 'str'>
