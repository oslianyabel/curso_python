while True:
    entrada = input(
        "Introdusca 2 números seguidos por un operador(+ - * /). Ej: 5,4,+ \nPara salir escriba 'salir'\n"
    )
    if entrada.lower() == "salir":
        break

    lista_str = entrada.split(",")
    lista_num = list(map(int, lista_str[:-1]))

    if lista_str[2] == "+":
        print(lista_num[0] + lista_num[1])
    elif lista_str[2] == "-":
        print(lista_num[0] - lista_num[1])
    elif lista_str[2] == "*":
        print(lista_num[0] * lista_num[1])
    elif lista_str[2] == "/":
        print(lista_num[0] / lista_num[1])
    else:
        print("Entrada invalida")
