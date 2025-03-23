def areaRectangulo(base , altura):
    if base < 0 or altura < 0:
        return "La base y la altura tienen q ser positivos."
    return base * altura

def main():
    print("Programa para calcular el area de un rectangulo.")
    print("________________________________________________")

    try:
         base = float(input("Ingrese la base del triangulo: "))
         altura = float(input("Ingrese la altura del triangulo: "))
         resultado = areaRectangulo(base, altura)
         
         if isinstance(resultado, str):  
            print(resultado)   
         else:
             print(f"El área del rectángulo es: {resultado} metros cuadrados")

    except ValueError:
        print("Escribe un valor valido.")
main()