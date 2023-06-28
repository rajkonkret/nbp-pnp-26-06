# funkcja obliczająca średnią
def liczby(*cyfry):
    print(cyfry)
    suma = 0
    count = len(cyfry)
    try:
        for c in cyfry:
            print(c)
            suma += c

        print(f"Średnia wynosi {suma / count}")
    except ZeroDivisionError:
        print("Dzielenie przez zero")
    except Exception as e:
        print("Bład", e)


liczby()  # ()
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
liczby("a", "b")
