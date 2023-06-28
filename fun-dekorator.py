# dekorator - funkcja opakowująca inną funkcję
def dekorator(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


@dekorator
def hej():
    print("Hej!")


hej()
# Dekorujemy
# Hej!
