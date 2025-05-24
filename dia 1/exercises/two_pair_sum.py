# Dada una lista de números y un número objetivo, contar cuántas combinaciones de dos números en la lista suman el número objetivo.
def solve(num_list, result):
    count = 0
    for i, n1 in enumerate(num_list):
        for j in range(i + 1, len(num_list)):
            if n1 + num_list[j] == result:
                count += 1

    return count


print(solve([1, 1, 3, 4, 5], 4))
