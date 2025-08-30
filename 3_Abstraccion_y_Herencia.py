""" INTEGRANTES:
    - Wesley Bladimir Rivera Villanueva
    - Romel José Mancia Preza
    - Jacinto Tomas Cortez Serrano
"""

# creamos una clase abstracta llamada "FIGURA"
# tambien creamos un metodo abstracto llamado "area()"
from abc import ABC, abstractmethod

class FIGURA(ABC):
    @abstractmethod
    def area(self):
        pass
# creamos dos subclases de "FIGURA" que son "CIRCULO" y "RECTANGULO"
# "CIRCULO" tendra como atributo el "radio"
class CIRCULO(FIGURA):
    def _init_(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2

class RECTANGULO(FIGURA):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
# "RECTANGULO" tendra como atributos la "base" y la "altura"
class RECTANGULO(FIGURA):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
# "RECTANGULO" tendra como atributos la "base" y la "altura"
class RECTANGULO(FIGURA):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
# poner a prueba las clases
circulo = CIRCULO(4)
rectangulo = RECTANGULO(5, 3)

print("Area del circulo:", circulo.area())
print("Area del rectangulo:", rectangulo.area())
# mostrar los resultados y el area de ambos