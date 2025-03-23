def perimetroCuadarado(lado):
    if lado < 0:
        return "Escribe un numeor q sea positivo"
    return lado * 4

def main():
    print("Programa para calcular el perimetro de un cuadrado")
    print("__________________________________________________")
    
    try:
        lado = float(input("Escribe el valor del lado del cuadrado: "))
        print(f"El perimetro del cuadrado es: {perimetroCuadarado(lado)}")
    except ValueError:
        print("Escribe un numer q sea valido")
main()
