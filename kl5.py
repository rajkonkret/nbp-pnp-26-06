from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")

    def wydaj_odglos(self):
        print("Kokokokokoko")


class Orzel(Ptak):
    def poluj(self):
        print("tu", self.gatunek, "Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiiiiiiiii")


# oznaczenie metody jako abstrakcyjnej powoduje, ze nie mozemu utworzyc takich obiektów
# or1 = Ptak("Orzeł", 20)
# or1.latam()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()

kur2 = Kura("Kura")
kur2.latam()
kur2.dziobanie()  # Tu Kura Idę sobie podziobać
kur2.wydaj_odglos()

or2 = Orzel("Orzel", 50)
or2.poluj()  # tu Orzel Rozpoczynam polowanie
or2.wydaj_odglos()
