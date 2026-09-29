cantidad = int(input("Cantidad de elementos: "))

lista1 = []
print("\nLista 1:")
for i in range(cantidad):
    num = int(input())
    lista1.append(num)

lista2 = []
print("\nLista 2:")
for i in range(cantidad):
    num = int(input())
    lista2.append(num)

lista_combinada = []

for num in lista1:
    lista_combinada.append(num)

for num in lista2:
    lista_combinada.append(num)

print("\nLista combinada:\n")
for num in lista_combinada:
    print(num)
