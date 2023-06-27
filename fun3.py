a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 6
    b = 7
    print(a + b)


print("Zmiennna a z góry", a)
dodaj()
print("Zmiennna a z góry", a)
dodaj2()
print("Zmiennna a z góry", a)
dodaj3()
print("Zmiennna a z góry", a)
