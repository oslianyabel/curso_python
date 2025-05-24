# Parámetro por valor (para tipos inmutables)
numero = 5

def modificar_numero(num):
    num += 10
    print(f"Dentro de la función: {num}")

modificar_numero(numero)  # Dentro de la función: 15
print(f"Fuera de la función: {numero}")  # Fuera de la función: 5


# Parámetro por referencia (para tipos mutables)
def modificar_lista(lista):
    lista.append(4)
    print(f"Dentro de la función: {lista}")

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)  # Dentro de la función: [1, 2, 3, 4]
print(f"Fuera de la función: {mi_lista}")  # Fuera de la función: [1, 2, 3, 4]


x = 10

def modificar_x():
    global x
    x = 20

modificar_x()
print(x)  # 20 (sí se modificó la global)