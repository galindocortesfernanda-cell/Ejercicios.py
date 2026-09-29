cantidad = int(input("Cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    codigo = input("\nCódigo: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    promedio = float(input("Promedio: "))
    
    # Se guarda cada estudiante usando un diccionario interno
    estudiantes[codigo] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }

mejor_codigo = ""
mejor_promedio = -1.0

for codigo in estudiantes:
    if estudiantes[codigo]["promedio"] > mejor_promedio:
        mejor_promedio = estudiantes[codigo]["promedio"]
        mejor_codigo = codigo

print("\nMejor estudiante\n")
print("Código:", mejor_codigo)
print("Nombre:", estudiantes[mejor_codigo]["nombre"])
print("Edad:", estudiantes[mejor_codigo]["edad"])
print("Carrera:", estudiantes[mejor_codigo]["carrera"])
print("Promedio:", estudiantes[mejor_codigo]["promedio"])
