def use_module():
    import calculos

    result = calculos.suma(5, 3)
    print(result)  # Output: 8
    print(calculos.PI)  # Output: 3.1416


def use_module_imports():
    from calculos import PI, suma

    print(suma(3, 4))  # 12
    print(PI)  # 3.14
