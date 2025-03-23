import math
def circulo(radio):
    if radio <= 0:
        return "Ingresa un valor mayor a 0."
    return f"El perimetro es: {(2 * math.pi) * radio}" 

def main():
    print("Calculadora del perimetro de un circulo.")
    print("________________________________________")

    try:
        radio = float(input("Ingresa el valor del radio: "))
        resultado = circulo(radio)
        print(resultado)
    
    except ValueError:
        print("Ingrese un numero valido.")
main()