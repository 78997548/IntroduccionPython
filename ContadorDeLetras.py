#Contar letras en una palabra
#Pide una palabra al usuario y usa un bucle para contar cuántas letras tiene.

palabra = input("Digite una palabra: ")
contador = 0
for letra in palabra:
    contador += 1
print(f"La palabra ingresada contiene {contador} letras.")