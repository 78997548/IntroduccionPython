#Tabla de multiplicar de un número
#Escribe un programa que solicite un número y muestre su tabla de multiplicar del 1 al 10.

def tablaMultiplicar():
    print("Tabla de multiplicar de un número")
    num = int(input("Dijite un numero: "))
    for i in range(1, 11):
        print(f"{num} × {i} = {num * i}")
tablaMultiplicar()