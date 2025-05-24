def use_module():
    import paquete.calculos

    result = paquete.calculos.suma(5, 3)
    print(result)  # Output: 8
    print(paquete.calculos.PI)  # Output: 3.1416


def use_module_imports():
    from paquete.calculos import PI, suma

    print(suma(3, 4))  # 12
    print(PI)  # 3.14


def use_module_init_imports():
    from paquete import PI, suma

    print(suma(3, 4))  # 12
    print(PI)  # 3.14

use_module_init_imports()