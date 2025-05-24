nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")


dia = 2
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case _:
        print("Otro día")


# Ejemplo 1: Iterar sobre una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Ejemplo 2: Iterar sobre un rango de números
for i in range(5):
    print(i)  # Imprime números del 0 al 4

# Ejemplo 3: Iterar sobre una cadena
cadena = "hola"
for caracter in cadena:
    print(caracter)

# Ejemplo 1: Contador
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Ejemplo 2: Pedir input hasta que sea correcto
while True:
    usuario = input("Ingrese 'salir' para terminar: ")
    if usuario.lower() == "salir":
        break
    print("Intentelo de nuevo.")


# enumerate
for indice, fruta in enumerate(frutas, start=1):
    print(f"Posición {indice}: {fruta}")


# zip
nombres = ["Ana", "Juan", "Carlos"]
edades = [25, 30, 22]
ciudades = ["Madrid", "Barcelona", "Valencia"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
