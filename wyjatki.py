# wyjątki
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    5. Koniec""")

    odp = input("Podaj działanie")
    if odp not in ['1', '2', '3', '4']:
        break
    try:
        a = int(input("Podaj pierwsza liczbe"))
        b = int(input("Podaj drugą liczbe"))
        if odp == '1':
            print(f"Wynik działąnia {a} + {b} = {a + b}")
        elif odp == '2':
            print(f"Wynik działąnia {a} - {b} = {a - b}")
        elif odp == '3':
            print(f"Wynik działąnia {a} * {b} = {a * b}")
        elif odp == '4':
            print(f"Wynik działąnia {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
    except ValueError:
        print("Błąd wartosci")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Inny błąd", e)
    else:
        print("Gdy nie ma błedu")
    finally:
        print("Zawsze")

# \033[31m: Set text color to red
# \033[32m: Set text color to green
# \033[33m: Set text color to yellow
# \033[34m: Set text color to blue
# \033[35m: Set text color to magenta
# \033[36m: Set text color to cyan
# \033[37m: Set text color to white
# \033[0m: Reset text color to default
# \033[1m: Set text style to bold
# \033[4m: Set text style to underline
# print("\033[31mHello\033[0m") - kolorki
