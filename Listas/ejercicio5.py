cantidad = int(input("Cantidad de palabras: "))
palabras = []

print("\nPalabras:")
for i in range(cantidad):
    p = input()
    palabras.append(p)

print("\nLista invertida:\n")
for i in range(cantidad - 1, -1, -1):
    print(palabras[i])
