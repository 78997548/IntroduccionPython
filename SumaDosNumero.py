#Sumar dos números

def sumar():
    while True:
        print("Calculadora de suma de dos numeros.")
        try:
            num1 = float(input("Digite el primer numero a sumar: "))
            num2 = float(input("Digite el segundo numero a sumar: "))
            total = num1 + num2
            print(f"El resultado es: {total}")
        except ValueError:
            print("Digite un numero valido.")

sumar()