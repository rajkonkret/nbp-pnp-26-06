def kantor(waluta):
    print("Uruchomienie kantoru", waluta)

    def usd(kwota):
        print(f"Wymieniam dolary: {kwota}  = {kwota * 4.1} zł")

    def eur(kwota):
        print(f"Wymieniam euro: {kwota} = {kwota * 4.4} zł")

    if waluta == "eur":
        return eur
    else:
        return usd


waluta = input("Podaj walute (usd/eur)")
kantor1 = kantor(waluta)
print(type(kantor1))
print(kantor1)
kwota1 = int(input("Podaj kwote"))
kantor1(kwota1)
# Wymieniam dolary: 1000  = 4100.0 zł
