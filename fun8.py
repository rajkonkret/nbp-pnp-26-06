def allparams(a, b, /, c=42, *args, d=9, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


# / oddziela pozycyjne od takich co moga byc przekazane po nazwie
allparams(1, 2)
allparams(1, 2, 3)  # c, d 3 9
allparams(1, 2, 3, d=8)
allparams(1, 2, c=3, d=8)
allparams(1, 2, 4, 1, 3, 4, 5, 6, 7, 8, 9)  # c musimy pozycyjnie gdy chcemy uzyc args
allparams(1, 2, 4, 1, 3, 4, 5, 6, 7, 8, 9, d=10)  # w takim przypadku d musimy po nazwie
allparams(1, 2, 3, 4, 5, 6, 7, user='radek')  # kwargs {'user': 'radek'}
allparams(1, 2, 3, 4, 5, 6, 7, user='radek', a=1)
