# Métodos de diccionarios
mi_diccionario = {'a': 1, 'b': 2}

# Acceder a claves y valores
print(list(mi_diccionario.keys()))  # Imprime: ['a', 'b']
print(list(mi_diccionario.values()))  # Imprime: [1, 2]
print(list(mi_diccionario.items()))  # Imprime: [('a', 1), ('b', 2)]

# Acceder y actualizar valores
print(mi_diccionario.get('c', 0))  # Imprime: 0
mi_diccionario.update({'c': 3})
print(mi_diccionario)  # Imprime: {'a': 1, 'b': 2, 'c': 3}

# Eliminar elementos
print(mi_diccionario.pop('a'))  # Imprime: 1
print(mi_diccionario)  # Imprime: {'b': 2, 'c': 3}
mi_diccionario.clear()
print(mi_diccionario)  # Imprime: {}