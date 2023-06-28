# klasy

class Human:
    """
    klasa Human opisująca człowieka
    """
    imie = ""
    wiek = ""
    plec = "k"

    def powitanie(self):
        print(f"Nazywam sie {self.imie}")


cz1 = Human()
print(Human.__doc__)  # dokumentacja z klasy
print(print.__doc__)
print(cz1.plec)
cz1.imie = "Radek"
cz1.powitanie()
# Nazywam sie Radek
cz2 = Human()
cz2.imie = "Aneta"
cz2.wiek = 20
cz2.plec = "k"
print(cz2.wiek)
cz2.powitanie()
# 20
# Nazywam sie Aneta

# 11:00