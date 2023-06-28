# funkcja zagnieżdzona
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy tylko adres funkcji


print(fun1())  # <function fun1.<locals>.fun2 at 0x102d94680>
xFun = fun1()
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
# xFun = <function fun1.<locals>.fun2 at 0x106600ae0>
