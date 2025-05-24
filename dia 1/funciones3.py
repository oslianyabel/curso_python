# parametros opcionales
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")

saludar("Carlos")  # Hola, Carlos!
saludar("Ana", "Buenos días")  # Buenos días, Ana!

#multiples parametros
def concatenar(*palabras, separador=" "):
    return separador.join(palabras)

print(concatenar("Python", "es", "genial"))  # Python es genial
print(concatenar("Python", "es", "genial", separador="-"))  # Python-es-genial