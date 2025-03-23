def perimetroRectangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Ingresa un valor positivo."
    return (f"El perimetro es: {(base + altura) * 2}")

def main():
    print("Programa para calcular el perimetro de un rectangulo.")
    print("_____________________________________________________")

    try:
        base = float(input("Ingrese el valor de la base: "))
        altura = float(input("Ingrese el valor de la altura: "))
        resultado = perimetroRectangulo(base, altura)
        print(resultado)

    except ValueError:
        print("Escribe un valor valido.")
main()