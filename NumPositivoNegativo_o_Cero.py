#Escribe un programa que lea un número y diga si es positivo, negativo o igual a cero.

def calcular():
    print("Calculadora para determinar si el numero es positivo, negativo o igual a cero.")
    
    try:
        num = int(input("Ingrese un Numero: "))
        if num > 0:
            print(f"El numero {num} es positivo.")
        elif num < 0:
            print(f"El numero {num} es negativo.")
        else:
            print(f"El numero {num} es igual a cero.")
    except ValueError:
        print("Ingrese un numero valido.")
        
calcular()


