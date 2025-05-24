# Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 120


# Fibonacci recursivo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Ejercicio: Contar la profundidad de una lista
# Dada una lista que puede contener otras listas, contar la profundidad máxima de la lista.
def solve(lista):
    def solve_rec(lista, count):
        global ans
        for i in lista:
            if type(i) is list:
                solve_rec(i, count + 1)

        if ans < count:
            ans = count

    if type(lista) is not list:
        return False
    else:
        solve_rec(lista, 1)


ans = 0
lista = [1, 2, [1, 2, []]]
solve(lista)
print(ans)
