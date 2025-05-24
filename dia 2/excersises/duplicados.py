# 1- elimina los duplicados de cada lista
# 2- crea una lista con los elementos comunes a ambas listas

lista1 = [3, 5, 7, 9, 5, 3, 1]
lista2 = [2, 3, 5, 10, 5, 2]

# 1
lista1_sin_duplicados = list(set(lista1))
lista2_sin_duplicados = list(set(lista2))
print(lista1_sin_duplicados)
print(lista2_sin_duplicados)

#2
lista_comun = list(set(lista1) & set(lista2))
print(lista_comun)