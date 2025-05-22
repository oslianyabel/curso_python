import json

# Guardar json
datos = {"nombre": "Ana", "edad": 23, "ciudad": "Madrid"}
datos_json = json.dumps(datos)  # conversion de objeto python a formato json
with open("datos.json", "w") as archivo:
    archivo.write(datos_json)

# Otra via
datos = {"nombre": "Ana", "edad": 23, "ciudad": "Madrid"}
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)
