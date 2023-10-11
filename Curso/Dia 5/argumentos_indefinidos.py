def suma(*args):
    print(type(len(args)))
    print(type(args))
    return sum(args)


print(suma(5,6,5,6,500,12))