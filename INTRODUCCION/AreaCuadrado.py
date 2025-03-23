def areaCuadrado(lado):

    if lado < 0:
        return "Escribe un valor q sea positivo"
    return lado * lado

def main():
      print("Este programa es para calcular el area de un cuadrado")
      print("____________________________________________________")
      
      try:
          lado = float(input("Escribe el valor del lado del cuadrado: "))
          print(f"El area del cudrado es: {areaCuadrado(lado)}")
      except ValueError:
          print("Escribe un valor q sea valido")
main()
