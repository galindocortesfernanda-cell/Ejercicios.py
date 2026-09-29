cantidad = int(input("Cantidad de notas: "))
suma_notas = 0

print("Notas:")
for i in range(cantidad):
    nota = float(input())
    suma_notas = suma_notas + nota

promedio = suma_notas / cantidad
print("El promedio de las notas es:", round(promedio, 2))
