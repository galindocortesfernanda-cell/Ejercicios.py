cantidad = int(input("Cantidad de vendedores: "))
ventas = {}

print()
for i in range(cantidad):
    datos = input().split()
    nombre = datos[0]
    total = int(datos[1])
    ventas[nombre] = total

mayor_vendedor = ""
mayor_venta = -1

for nombre in ventas:
    if ventas[nombre] > mayor_venta:
        mayor_venta = ventas[nombre]
        mayor_vendedor = nombre

print("\nMayor vendedor:\n")
print(mayor_vendedor, "-> $" + str(mayor_venta))
