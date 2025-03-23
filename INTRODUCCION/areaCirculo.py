import math
def areaCirculo(radio):
    if radio <= 0:
        return "Ingresa un valor de radio positivo o mayor a 0."
    return f"Area del circulo es: {math.pi * radio**2}"

def main():
    print("Programa para calcular el perimetro de un rectangulo.")
    print("_____________________________________________________")

    try:
       radio = float(input("Ingrese el valor del radio: "))
       resultado = areaCirculo(radio)
       print(resultado)
       
    except ValueError:
        print("Ingresa un valor valido.")

main()

