class TarjetaPrepago:
    #atributos el saldo dede ser privado que no se muestre directamente
    def _init_(self, saldo_inicial, numero):
        self.__saldo = saldo_inicial
        self.numero = numero
    #metodo para recargar saldo
    def recargar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se ha recargado {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto debe ser mayor que cero.")  
    #metodo para consumir saldo
    def consumir(self, monto):
        if monto <= 0:
            print("Error el monto de se mayor")
        elif monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se ha consumido {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("No hay suficiente saldo.")
            return False
    #metodo de consulta
    def consultar_saldo(self):
        return self.__saldo

#tarjeta de prueba 
tarjeta = TarjetaPrepago(200, "123456789")
tarjeta.recargar(100)            
tarjeta.consumir(80)
#si se quiere consumir mas de lo que hay en el saldo saldra error
tarjeta.consumir(3000)
print("error")