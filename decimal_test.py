#
# Przykład użycia Decimal do obliczeń na pieniądzach:
#
# python
# Copy code
import decimal
from decimal import Decimal
#

# Kwoty jako obiekty typu Decimal
kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
precyzja2 = Decimal('0.00')

# Dodawanie kwot
suma = kwota1 + kwota2
print("Suma:", suma)  # Suma: 15.75

# Odejmowanie kwot
roznica = kwota1 - kwota2
print(roznica)
print("Różnica:", roznica.quantize(precyzja2))  # Różnica: 4.75

# Mnożenie kwoty przez liczbę (np. podatek)
podatek = Decimal('0.23')  # 23% podatku
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja2))  # Kwota z podatkiem: 12.61

# Dzielenie kwoty przez liczbę (np. dzielenie rachunku na osobę)
ilosc_osob = 3
rachunek_na_osobe = kwota_z_podatkiem / ilosc_osob
print("Rachunek na osobę:", rachunek_na_osobe.quantize(precyzja2))  # Rachunek na osobę: 4.20
# W powyższym przykładzie używamy typu Decimal do obliczeń na pieniądzach.
# Ustawiamy precyzję obliczeń na 2 miejsca po przecinku,
# aby uzyskać odpowiednią precyzję dla operacji na pieniądzach.
# Następnie wykonujemy różne operacje matematyczne na obiektach Decimal.

import decimal

# Ustawienie precyzji po przecinku na 4 miejsca
precyzja = decimal.Decimal('0.0000')

# Przykład obliczeń z ustawioną precyzją po przecinku
a = decimal.Decimal('1.2345')
b = decimal.Decimal('2.3456')
c = a + b

wynik = c.quantize(precyzja)

print(wynik)  # Wynik: 3.5801
