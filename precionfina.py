
print("Bienvenido dinos el precio, ganancias y impuestos")
#escribir leer
precio = input("Ingrece el precio:")
precio = float(precio)

ganacia = input("Ingrece la ganacia:")
ganacia = float(ganacia)

impuesto = input("Ingrece el impuesto:")
impuesto = float(impuesto)

def calcularImpuesto(impuesto, precio):
    return impuesto * precio
    
def calcularGanacia(ganacia, precio):
    return ganacia * precio

def calcularPrecioFinal(precio, impuesto):
    precio1 = calcularGanacia(ganacia, precio) + precio
    impuestoVenta = calcularImpuesto(impuesto,precio1)
    return precio1 + impuestoVenta
print(calcularPrecioFinal(precio,impuesto,ganacia))