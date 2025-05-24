# crea un generador de contraseñas aleatorias de 8 caracteres con al menos una mayúscula, un carácter especial y un número
import random

ans = ""
for i in range(8):
    caracters = range(33, 122)
    val = random.choice(caracters)
    ans += chr(val)

print(ans)
