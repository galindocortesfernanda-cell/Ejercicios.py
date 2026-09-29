cantidad = int(input("Cantidad de calificaciones: "))
calificaciones = []

print("\nCalificaciones:")
for i in range(cantidad):
    nota = float(input())
    calificaciones.append(nota)

suma = 0
for nota in calificaciones:
    suma = suma + nota

promedio = suma / cantidad
print(f"\nPromedio: {promedio:.2f}")
