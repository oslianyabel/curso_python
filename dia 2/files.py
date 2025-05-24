with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, mundo!\nEsta es una segunda línea.")

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())