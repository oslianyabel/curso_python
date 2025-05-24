numeros = [3, 1, 4, 1, 5, 9, 2]

print(len(numeros))  # 7
print(min(numeros))  # 1
print(max(numeros))  # 9
print(sum(numeros))  # 25

# sorted y reversed
print(sorted(numeros))  # [1, 1, 2, 3, 4, 5, 9]
print(list(reversed(numeros)))  # [2, 9, 5, 1, 4, 1, 3]

# filter y map
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [4, 2]
pares = [x for x in numeros if x % 2 == 0]  # alternativa
print(pares)

cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [9, 1, 16, 1, 25, 81, 4]
cuadrados = [x**2 for x in numeros]  # alternativa
print(cuadrados)
