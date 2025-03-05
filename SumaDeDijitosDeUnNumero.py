# Suma de dígitos de un número
numero = input("Ingrese un número para sumar sus dígitos: ")
suma = 0
for digito in numero:
    if digito.isdigit():  # Verificar que sea un número
        suma += int(digito)
print(f"La suma de los dígitos de {numero} es {suma}.")
