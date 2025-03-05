#Suma de dígitos de un número
#Pide un número al usuario y usa un bucle para sumar sus dígitos.

num = input("Digite un numero: ")
sumador = 0
for digitos in num:
     sumador += int(digitos)
print(f"La suma de los digitos de {num} es {sumador}.")