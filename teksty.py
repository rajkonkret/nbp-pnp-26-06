tekst = "Witaj świecie"
print(tekst)  # Witaj świecie

# teksty sa niemutowalne
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)

tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE

tekst3 = tekst.lower()
print(tekst3)  # witaj świecie

print(tekst.removeprefix("Witaj"))  # świecie
print(tekst.removesuffix("świecie"))  # "Witaj "

print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - zapisanie binary
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # sprawdzenie ile razy wystapi "i" w tekscie w znakach od pozycji 0 do 3

print(len(tekst))  # sprawdzenie długosci tekstu

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona \b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię Pythona
# "

# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!
print("""
     Tekst 
    wielolinijkowy""")
print("""
""")
# "     Tekst
#     wielolinijkowy"
