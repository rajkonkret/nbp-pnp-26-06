class Car:
    """
    klasa samochod
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkosc wynosi {self.__predkosc} km/h")

    def hamuj(self):
        """
        funkcja hamuj
        :return: None
        """
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("fiat", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)  # 50, nie zadziała bo mamy prywatne pole
car1.licznik()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
print(Car.hamuj.__doc__)