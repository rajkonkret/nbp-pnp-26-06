class Dom:
    """
    Klasa Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def moj_kolor(self):
        print(f"Mój kolor {self.__kolor}")

    def moj_metraz(self):
        print(f"Mój metraz {self.__metraz}")

    def moj_okna(self):
        print(f"Mój kolor {self.__liczba_okien}")

    def zmien_metraz(self):
        wybor = int(input("Podaj  nowy metraż"))
        self.__metraz = wybor
        print(f"Metraz wynosi {self.__metraz}")

    def zmien_kolor(self):
        wybor = input("Podaj  nowy kolor")
        self.__kolor = wybor
        print(f"kolor: {self.__kolor}")

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        print(f"Liczba okien wynosi {self.__liczba_okien}")


dom1 = Dom(500, "czerwony", 5)
dom1.moj_metraz()
# dom1.__metraz = 150
# print(dom1.__metraz)
dom1.moj_metraz()
dom1.zmien_metraz()
dom1.zmien_kolor()