cantidad = int(input("Cantidad de productos: "))
productos = []

print("\nProductos:")
for i in range(cantidad):
    prod = input()
    productos.append(prod)

print("\nLista de compras:\n")
for i in range(cantidad):
    print(f"{i + 1}. {productos[i]}")
