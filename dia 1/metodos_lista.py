mi_lista = [1, 2, 3]

# Añadir elementos
mi_lista.append(4)
print(mi_lista)  # Imprime: [1, 2, 3, 4]
mi_lista.extend([5, 6])
print(mi_lista)  # Imprime: [1, 2, 3, 4, 5, 6]
mi_lista.insert(1, 7)
print(mi_lista)  # Imprime: [1, 7, 2, 3, 4, 5, 6]

# Eliminar elementos
mi_lista.remove(7)
print(mi_lista)  # Imprime: [1, 2, 3, 4, 5, 6]
print(mi_lista.pop(1))  # Imprime: 2
print(mi_lista)  # Imprime: [1, 3, 4, 5, 6]
mi_lista.clear()
print(mi_lista)  # Imprime: []

# Buscar y contar
mi_lista = [1, 2, 2, 3]
print(mi_lista.index(2))  # Imprime: 1
print(mi_lista.count(2))  # Imprime: 2

# Ordenar y revertir
mi_lista = [3, 1, 2]
mi_lista.sort()
print(mi_lista)  # Imprime: [1, 2, 3]
mi_lista.reverse()
print(mi_lista)  # Imprime: [3, 2, 1]

# Copiar
mi_lista = [1, 2, 3]
copia_lista = mi_lista.copy()
print(copia_lista)  # Imprime: [1, 2, 3]
