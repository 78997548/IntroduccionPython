#Multiplicación con bucles
#Pide un número al usuario y usa un bucle para mostrar su tabla de multiplicar del 1 al 10.

num = int(input("Dijite un numero: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")