import json

# Cargar json
with open("datos.json", "r") as archivo:
    datos = archivo.read()
    datos_json = json.loads(datos)  # conversion de formato json a objeto python
    print(datos_json)
    print(type(datos_json))

# Otra via
with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)
    print(datos_json)
    print(type(datos_json))
