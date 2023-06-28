# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z kalsy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):
    """
    klasa C, dziedziczy po kalsie A i B
    """

    def method(self):
        # trzy opcje
        super().method()
        print(f"Metoda z klasy C")
        B.method(self)


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
