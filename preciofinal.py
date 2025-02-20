
print("Bienvenido dinos los precios, ganancia y impuestos")
#escribir  leer
precio = input("Ingrese el precio: ")
precio= float(precio)

ganancia = input("Ingrese la ganancia: ")
ganancia = float(ganancia)

impuesto = input("Ingrese el impuesto: ")
impuesto = float(impuesto)

#funcion nombre del variable
def calcularImpuesto(impuesto, precio):
    return impuesto * precio

def calcularGanancia(ganancia, precio):
    return ganancia * precio

def calcularPrecioFinal(precio, impuesto, ganancia):
    precio1 = calcularGanancia(ganancia, precio) + precio
    impuestoVenta = calcularImpuesto(impuesto, precio1)
    return precio1 + impuestoVenta

print(calcularPrecioFinal(precio, impuesto, ganancia))
