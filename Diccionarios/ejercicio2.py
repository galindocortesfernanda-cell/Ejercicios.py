cantidad = int(input("Cantidad de contactos: "))
agenda = {}

for i in range(cantidad):
    nombre = input("\nNombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

buscar = input("\nBuscar contacto: ")

if buscar in agenda:
    print("Teléfono de", buscar, ":", agenda[buscar])
else:
    print("El contacto no existe.")
