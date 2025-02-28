#Convertir grados Celsius a Fahrenheit

def conversor():
    print("Conversor de grados Celsius a Fahrenheit")
    c = float(input("Ingresa los grados celcius a convertir: "))
    F = (c * 9/5) +32

    print(f"{c} Grados Celsius es igual a: {F} Grados Fahrenheit")

conversor()


