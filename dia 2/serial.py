import json

datos = {"nombre": "Ana", "edad": 23, "ciudad": "Madrid"}
datos_json = json.dumps(datos)
with open("datos.json", "w") as archivo:
    archivo.write(datos_json)
    #json.dump(datos, archivo, indent=4)

with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)
    print(datos_cargados["nombre"])