user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - zmiennoprzecinkowe
liczba = 134567456345  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %s masz teraz %d lat" % (wiek, user))
# TypeError: %d format: a real number is required, not str
# %s str
# %d -digit

print('Witaj %(user)s, masz teraz %(age)d lat'
      % {'user': user, 'age': wiek})

print("Witaj {} masz teraz {} lat".format(user, wiek))  # Witaj Tomek masz teraz 39 lat
print("Witaj {} masz teraz {} lat".format(wiek, user))

print(f"Witaj {user}, masz teraz {wiek} lat")

print("Używamy wersji Pythona  %i" % 3)  # Używamy wersji Pythona  3
print("Używamy wersji Pythona %f" % 3.9)  # Używamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.1f" % 3.9)
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4
# zero miejsc po przecinku, ale z zaokrągleniem

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.900001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:>20}")
print(f"{user:<30}")  # "Tomek                         "

print(liczba)  # 134567456345
print("Nasza duża liczba {:,}".format(liczba))
# Nasza duża liczba 134,567,456,345
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))
