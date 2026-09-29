cantidad = int(input("Cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    codigo = input("\nCódigo: ")
    nombre = input("Nombre: ")
    estudiantes[codigo] = nombre

print("\nListado de estudiantes\n")
for codigo in estudiantes:
    nombre = estudiantes[codigo]
    print(codigo, "->", nombre)
