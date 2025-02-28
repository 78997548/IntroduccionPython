#Doble del numero

def calcular_doble():
    print("Calcular el doble de un número")
    
    try:
        num = int(input("Digita un numero: "))
        proceso = num * 2
        print(f"El doble del número {num} es: {proceso}")
    except ValueError:
        print("Ingresa un numero valido!!")

calcular_doble()