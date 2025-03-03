#Verificar si una persona es mayor de edad
#Escribe un programa que solicite la edad de una persona y determine si es mayor de edad (18 años o más).

def mayorEdad():
    try:
        print("Verificador de mayoria de edad.")
        edad = int(input("Ingrese su edad: "))
        
        if edad >= 18:
            print("Eres mayor de edad, bienvenido.")
        elif edad <= 17:
            print("Eres menor de edad, acceso denegado.")
        
    except ValueError:
        print("Ingresa una edad valida.")

mayorEdad()

