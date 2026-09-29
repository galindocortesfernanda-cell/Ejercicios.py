cantidad = int(input("Cantidad de libros: "))
biblioteca = {}

for i in range(cantidad):
    codigo = input("\nCódigo: ")
    titulo = input("Título: ")
    biblioteca[codigo] = titulo

buscar = input("\nConsultar código: ")

print("\nLibro encontrado:\n")
if buscar in biblioteca:
    print(buscar, "->", biblioteca[buscar])
else:
    print("Código no encontrado.")
