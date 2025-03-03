#Escribe un programa que pida la base y la altura de un triángulo, y calcule su área usando la fórmula:
#A = (B * al)/2

def triangulo():
    try:
        al = float(input("Escriba la altura del triangulo: "))
        B = float(input("Escriba la base del triangulo: "))
        A = (B * al) / 2
        print(f"El área del triangulo es: {A}")

    except ValueError:
        print("Ingrese un numero valido.")
triangulo()