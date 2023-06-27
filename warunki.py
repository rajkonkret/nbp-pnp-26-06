# warunki  - instrukcje sterowania przepływem programu

# if
odp = False

if odp:
    print("Brawo")
else:
    print("Musisz się dalej uczyć")

print("Program nadal działą")

# podatek = 0.0
# zarobki = int(input('Podaj dochód'))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f'Zapłacisz {podatek * zarobki} zł')

suma_zam = 50
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

# 11:15

lista_bledow = []
alert_system = 'email'
error = 'dowolny'
error_message = "Stało się coś strasznego"

if alert_system == 'console':  # ==  porównanie
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append("email")
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == "critical":
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny")

print(lista_bledow)

# test z historii
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print("Prawidłowa odpowiedź")
else:
    print("Maszw ksiązce na stronie 23")
