#Encontrar el primer múltiplo de 7 mayor que 100
#Usa un bucle while para encontrar el primer número mayor que 100 que sea múltiplo de 7.

numero = 101  

while numero % 7 != 0:  
    numero += 1

print(f"El primer multiplo de 7 mayor que 100 es {numero}.")