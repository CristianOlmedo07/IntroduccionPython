# Adivina el número
import random
numero_secreto = random.randint(1, 100)
intento = 0
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento < numero_secreto:
        print("Más alto.")
    elif intento > numero_secreto:
        print("Más bajo.")
    else:
        print("¡Correcto! Has adivinado el número.")
        break
