cantidad = int(input("Cantidad de productos: "))
inventario = {}

for i in range(cantidad):
    producto = input("\nProducto: ")
    cant = int(input("Cantidad: "))
    inventario[producto] = cant

buscar = input("\nConsultar producto: ")

if buscar in inventario:
    print("Cantidad disponible de", buscar, ":", inventario[buscar])
else:
    print("El producto no está registrado.")
