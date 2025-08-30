""" INTEGRANTES:
    - Wesley Bladimir Rivera Villanueva
    - Romel José Mancia Preza
    - Jacinto Tomas Cortez Serrano
"""


class Persona:
    def __init__(self, nombre, edad):
        # inicializamos los atributos
        self.nombre = nombre # se guarda el nombre
        self.edad = edad # se guarda la edad

    # metodo para mostrar los datos de la persona
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        
    """mostrar_datos():
        Muestra el nombre y la edad de la persona.
    es_mayor_de_edad():
        Devuelve True si la persona tiene 18 años o más, False en caso contrario.
    """

    # mtodo para determinar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18: 
            return True # si tiene 18 o mas, es mayor
        else:
            return False # si no, es menor

# crear dos instancias de persona
persona1 = Persona("Wesley", 20)  # mayor de edad
persona2 = Persona("Michell", 15)  # este menor de edad

# mostrar los datos y tambien verificar si son mayores de edad
persona1.mostrar_datos()
print("Mayor de edad:", persona1.es_mayor_de_edad())

persona2.mostrar_datos()
print("Mayor de edad:", persona2.es_mayor_de_edad())
