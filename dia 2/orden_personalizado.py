personas = [
    {"name": "Ana", "age": 25},
    {"name": "Juan", "age": 20},
    {"name": "Luís", "age": 25}
]

personas.sort(key=lambda x: (x["age"], x["name"]))
print(personas)
