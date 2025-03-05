import json
from datetime import datetime #NOTAAA:  TENGO QUE ELIMINAR LAS NOTAS Y PONER BIEN LAS PALABRAS 
                              #QUE SE MUESTRAN EN PRINT XD

class SistemaVentas:
    PRODUCTOS = {
        "Bebidas A LA VRG": {
            1: ("Pilsener", 1.50),
            2: ("Corona", 1.50),
            3: ("Botella de Agua Cristal", 0.50),
            4: ("Limonada Natural", 2.00),
            5: ("Coca Cola", 1.00)
        },
        "Comidas": {
            6: ("Sopa de pescado", 10.00),
            7: ("Churrasco", 12.00),
            8: ("Tacos", 6.00),
            9: ("Plato Boqueado", 10.00),
            10: ("Mariscos", 13.00)
        },
        "Postres": {
            11: ("Tres leches", 3.00),
            12: ("Pastel de Chocolate", 3.00), #ESTO ES PARA MIENTRAS UNA IDEA
            13: ("Budín", 1.50) #TENGO QUE PREGUNTARLE A BLADI EL MENU COMPLETO
        }
    }

    def __init__(self, archivo="ventas.json"):
        self.archivo = archivo
        self.ventas = self.cargar_ventas()

    def agregar_venta(self, producto_id, cantidad):
        for categoria, productos in self.PRODUCTOS.items():
            if producto_id in productos:
                producto, precio_unitario = productos[producto_id]
                total = cantidad * precio_unitario
                fecha = datetime.now().strftime("%Y-%m-%d")
                venta = {
                    "producto": producto,
                    "cantidad": cantidad,
                    "precio_unitario": precio_unitario,
                    "total": total,
                    "fecha": fecha  
                }
                self.ventas.append(venta)
                self.guardar_ventas()
                print(f"Venta registrada: {producto} x{cantidad} - Total: ${total:.2f} - Fecha: {fecha}")
                return
        print("Producto no encontrado porque no existe pendej.")

    def mostrar_ventas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
            return

        print("Historial de Ventas ALV:")
        ingresos_por_fecha = {}

        for i, venta in enumerate(self.ventas, 1):
            fecha = venta.get("fecha", "Fecha desconocida")  # Evitar error si falta la clave
            print(f"{i}. {venta['producto']} - {venta['cantidad']} x ${venta['precio_unitario']:.2f} = ${venta['total']:.2f} - 📅 {fecha}")
            
            if fecha not in ingresos_por_fecha:
                ingresos_por_fecha[fecha] = {}
            
            if venta["producto"] in ingresos_por_fecha[fecha]:
                ingresos_por_fecha[fecha][venta["producto"]]["cantidad"] += venta["cantidad"]
                ingresos_por_fecha[fecha][venta["producto"]]["total"] += venta["total"]
            else:
                ingresos_por_fecha[fecha][venta["producto"]] = {
                    "cantidad": venta["cantidad"],
                    "total": venta["total"]
                }

        print("Ingresos por día:")
        for fecha, productos in ingresos_por_fecha.items():
            print(f"📅 {fecha}")
            for producto, datos in productos.items():
                print(f"🔹 {producto} x{datos['cantidad']} = ${datos['total']:.2f}")

        print(f"Ingresos Totales: ${self.calcular_total():.2f}")

    def calcular_total(self):
        return sum(venta["total"] for venta in self.ventas)

    def guardar_ventas(self):
        with open(self.archivo, "w") as f:
            json.dump(self.ventas, f, indent=4)

    def cargar_ventas(self):
        try:
            with open(self.archivo, "r") as f:
                ventas = json.load(f)
                for venta in ventas:
                    if "fecha" not in venta:
                        venta["fecha"] = "Fecha desconocida"  # Evita error en datos antiguos
                return ventas
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def menu():
    sistema = SistemaVentas() #NOTA: TENGO QUE APRENDER A HACER CODIGO INTERACTIVO TACTIL
                               #NO UTILIZANDO LA OPCION DE NUMEROS XD
    while True:
        print("Menú del Sistema de Ventas Pesera el TENGO QUE DEFINIR EL NOMBRE XD ")
        print("1️⃣ Agregar venta")
        print("2️⃣ Mostrar ventas") #TENGO QUE APRENDER A UTILIZAR MAS EMOJIS PARA Q SE VEA MAS BONITO EL CODIGO xd
        print("3️⃣ Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Lista de productos:")
            for categoria, productos in SistemaVentas.PRODUCTOS.items():
                print(f"🔸 {categoria}:")
                for num, (nombre, precio) in productos.items():
                    print(f" {num}. {nombre} - ${precio:.2f}")

            try:
                producto_id = int(input("Selecciona el número del producto: "))
                cantidad = int(input("Cantidad vendida: "))
                sistema.agregar_venta(producto_id, cantidad)
            except ValueError:
                print("Entrada inválida. Intenta de nuevo.")
        elif opcion == "2":
            sistema.mostrar_ventas()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()

#TENGO QUE HACER UN ESPACIO PARA ENUMERAR LAS MESAS Y PONER HORA Y MINUTO EXACTO 
# Y ASI SABER EL REGISTRO DE LA VENTA EXACTA PARA QUE SE PUEDAN REVIZAR LAS CAMARAS