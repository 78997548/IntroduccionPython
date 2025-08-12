#MIEMBROS:
#Romel José Mancia Preza
#Wesley Bladimir Rivera Villanueva
#Jose Alejandro Diaz Cortez
#Jacinto Tomas Cortez Serrano
#Karen Estefani Guillen Quijada.

def ejercicio1():
    
    print("\n🧩 Ejercicio 1 – Número positivo, negativo o cero (condicional simple y múltiple)")
    
    numero = float(input("ingrese por favor el numero: ")) # se le solicita un numero al usuario
    if numero in (1,2,3,4,5,6,7,8,9): # se escriben los numeros positivos
        print("el numero es positivo") # se imprime que el numero es positivo
    elif numero in (-1,-2,-3,-4,-5,-6,-7,-8,-9): #se escriben los numeros negativos
        print("el numero es negativo") # se imprime que el numero es negativo
    else:
        print("el numero es igual a cero") # se imprime que el numero es igual a cero

# fin del primer ejercicio



def ejercicio2():
    # se creara un ciclo con WHILE para contar desde el uno hasta 15
    # no se ejecuta (al menos que este comentado)

    print("\n\n🔁 Ejercicio 2 – Contador con while")

    contador = 1 # se inicializa el contador desde el numero 1
    while contador <= 15: # se  establece el limite
        print(contador) # se imprime el contador
        contador += 1 # se incrementa el contador

    # fin del segundo ejercicio



def ejercicio3():
# ejercicio 3
# se le solicita un numero al usuario y muestra su tabla de multiplicar del 1 al 10
# se usara un ciclo FOR
# no se ejecuta (al menos que este comentado)
    print("\n\n🔢 Ejercicio 3 – Tabla de multiplicar con for")
    
    numero = int(input("ingrese por favor el numero:")) # se le solicita un numero al usuario
    for numero2 in range(1, 11): # se establece el rango que tendra la tabla de multiplicar
        print(f"{numero} x {numero2}  = {numero * numero2}") # se imprime la tabla de multiplicar

    # fin del tercer ejercicio



def ejercicio4():
# ejercicio 4
# creamos un programa que sume numeros introducidos por el usuario uno por uno
# la suma termina cuando el usuario ingresa un numero negativo
# usamos WHILE Y BREAK
# no se ejecuta (al menos que este comentado)

    print("\n\n🔁 Ejercicio 4 – Suma acumulativa con break")

    suma = 0  # se inicializa la suma en cero
    while True:
        numero3 = float(input("Ingrese un número para sumar (o un número negativo para terminar): "))
        if numero3 < 0:
            break  # si el numero es negativo, se termina el ciclo
        suma += numero3  # se suma el numero ingresado por el usuario

    print(f"La suma total es: {suma}")  # imprimimos el resultado final


# fin del cuarto ejercicio



# bloque de comando para ejecutar SOLO  UNO cuando se quiera probar
if __name__ == "__main__":
    while True:
        print("\nElije el ejercicio")
        print("1 Positivo, negativo o cero")
        print("2 Contador con while")
        print("3 Tabla de multiplicar")
        print("4 Suma acumulativa")
        print("0 Salir")

        seleccion = int(input("Elija una opcion de 1 a 4: "))

        if seleccion == 1:
            ejercicio1()
        elif seleccion == 2:
            ejercicio2()
        elif seleccion == 3:
            ejercicio3()
        elif seleccion == 4:
            ejercicio4()
        elif seleccion == 0:
            print("Cerrando programa")
            break
        else:
            print("Opcionn inbalida")