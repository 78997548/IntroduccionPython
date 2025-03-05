#Adivina el número
#Genera un número aleatorio entre 1 y 100 y usa un bucle para que el usuario intente adivinarlo, dando pistas de "más alto" o "más bajo".

import random
def advinaNumero():
    numero = random.randint(1, 100)
    print("Bienvenido al juego Adivina el Numero.")

    while True: 
        try:
            num = int(input("Digita un numero: "))
            if num == numero:
                print("Felicidades, adivinastes el numero.")
                break
            elif num > numero:
                print("El numero es mas bajo, sigue intentandolo.")
            elif num < numero:
                print("El numero es mas alto, sigue intentandolo.")
        except ValueError:
            print("Ingresa un numero valido.")

advinaNumero()
