def square_perfect(n):
    root = n ** (1 / 2)
    return root.is_integer()
    root = int(root)  # contrevir a entero
    if root**2 == n:
        return True

    return False


ok = square_perfect(9)
print(ok)
