'''
valor1 = int(input("ingrese un valor:"))
valor2 = int(input("ingrese otro valor:"))

if valor1 < valor2:
    print("es mayor")

else: print("es menor") 

if 4==4: 
    print("4==4", "=true")
'''
respuesta = int(input("Ingrese un número para verificar si es par o impar: "))
    
if respuesta % 2 == 0:
    print("es par")
else:
    print("es impar")
    
if respuesta < 0:
    print("es negativo")
else:
    print("es positivo")
    
if respuesta == 0:
    print("es cero")
# if una opcion

print("_______________________________")

respuesta1 = "es par" if respuesta % 2 == 0 else "es impar"
respuesta2= "negativo" if respuesta < 0 else "positivo"
print (f"{respuesta1} , {respuesta2}")


#definir el numero par
#def nombre (): 

def modulo (valor):
    valor = True if respuesta % 2 == 0 else False
    print(valor)
    return valor
# Las funciones son estructuras de 
# codigo que se ejecutan mediante su llamado nombre()

def signo(respuesta):
    valor = True if respuesta < 0 else False
    print(valor)
    return valor


def detectarLetras(valor):
    if any(c.isalpha() for c in str(valor)):
        print(True)
        return True
    else:
        print(False)
        return False
#any es una funcion que ya tra python
#true de lo contrario false
#for c es una variable temporal
#for dara las vueltas necesarias para terminar el numero segun sus caracteres
#isasphan nos indica si todos los caracteres son letras o numeros

valor = 36
modulo(valor)
signo(respuesta)
detectarLetras("53")

def ejecutar():
    pedirValor = int(input("Ingrese un número: "))
    if pedirValor == True:
        ejecutar()
    else:
        #valor = True if respuesta % 2 == 0 else False
        Mrespuesta = modulo(pedirValor)
        #valor = True if respuesta < 0 else False
        Srespuesta = signo(pedirValor)
        #positivo y par
        if Mrespuesta == True and Srespuesta == True:
            print("Es positivo y par")
        if Mrespuesta == True or Srespuesta == False:
            print("Es negativo y par")
ejecutar()