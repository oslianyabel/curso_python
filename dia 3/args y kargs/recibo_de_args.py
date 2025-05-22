def sumar(*args):
    print(args)
    return sum(args)


print(sumar(1, 2, 3))  # 6
print(sumar(5, 10, 15, 20))  # 50
