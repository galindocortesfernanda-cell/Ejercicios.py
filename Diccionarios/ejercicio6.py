cantidad = int(input("Cantidad de empleados: "))
empleados = {}

print()
for i in range(cantidad):
    datos = input().split()
    id_emp = datos[0]
    salario = float(datos[1])
    empleados[id_emp] = salario

suma_salarios = 0.0
for id_emp in empleados:
    suma_salarios = suma_salarios + empleados[id_emp]

promedio = suma_salarios / cantidad
print("\nSalario promedio: $" + str(round(promedio, 2)))
