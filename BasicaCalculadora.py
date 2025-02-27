import math

def calculadora():
    print("Calculadora basica")
    print("Selecciones una operacion: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    OperacionElejida = input("Ingrese el numero de la operacion deseada: ")
    
    if OperacionElejida in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        
        if OperacionElejida == '1':
            print(f"Resultado {num1} + {num2} = {num1 + num2}")
        elif OperacionElejida == '2':
            print(f"Resultado {num1} - {num2} = {num1 - num2}")
        elif OperacionElejida == '3':
            print(f"Resultado {num1} * {num2} = {num1 * num2}")
        elif OperacionElejida == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Intente de nuevo.")



calculadora()