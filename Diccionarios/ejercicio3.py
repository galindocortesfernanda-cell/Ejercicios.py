cantidad = int(input("Cantidad de estudiantes: "))
notas = {}

print()
for i in range(cantidad):
    datos = input().split()
    nombre = datos[0]
    nota = float(datos[1])
    notas[nombre] = nota

mejor_estudiante = ""
mejor_nota = -1.0

for nombre in notas:
    if notas[nombre] > mejor_nota:
        mejor_nota = notas[nombre]
        mejor_estudiante = nombre

print("\nEl estudiante con la mejor nota es:\n")
print(mejor_estudiante, "->", mejor_nota)
