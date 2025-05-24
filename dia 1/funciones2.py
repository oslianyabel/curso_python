# *args para múltiples argumentos posicionales
def sumar(*args):
    return sum(args)

print(sumar(1, 2, 3))  # 6
print(sumar(5, 10, 15, 20))  # 50


# **kwargs para múltiples argumentos nombrados
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
# nombre: Juan
# edad: 30
# ciudad: Madrid