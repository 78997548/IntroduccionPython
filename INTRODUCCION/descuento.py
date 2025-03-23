#
#
#
#

compra = float(input("Ingrese el monto de la compra: "))
unidades = int(input("Ingrese la cantidad de unidades: "))
impuesto = 0
if compra < 0 :
    print("El monto de la compra no puede ser negativo.")
if unidades < 12 : descueto = 0
if unidades >= 12 : descueto = 0.02
if compra >= 100 and compra < 50: impuesto = 0.05 
if compra > 50 and compra < 100: impuesto = 0.10
if compra > 100 and compra < 200: impuesto = 0.20
if compra > 200: impuesto = 0.20

resultado = compra * impuesto
montoTotal = compra + resultado - descueto * compra
print(descueto * compra)
print("El impuesto a pagar es: ", montoTotal)

# pedir desde consola un monto de si compra 12 unidades 10% de descuento
# si compra 20 unidades 10% de descuento

