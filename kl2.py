class Human:
    """
    klasa opisująca człowieka
    """

    def __init__(self, imie, wiek, plec="k"):
        self.imie = imie
        self.plec = plec
        self.wiek = wiek

    def powitanie(self):
        print("Mam na imię", self.imie)

    def moj_wiek(self):
        print(f"Moj wiek", self.wiek)

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem")
        else:
            print("Ruszyłam")


cz1 = Human("Radek", 50, "m")
print(cz1)  # <__main__.Human object at 0x10502ed50>
print(cz1.wiek)
cz1.powitanie()
cz1.ruszaj()
cz1.moj_wiek()

cz2 = Human("Ania", 67)
print(cz2.plec)
cz2.moj_wiek()
cz2.powitanie()
cz2.ruszaj()
