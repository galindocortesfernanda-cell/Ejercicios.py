cantidad = int(input("Cantidad de números: "))
lista = []

print("\nLista:")
for i in range(cantidad):
    num = int(input())
    lista.append(num)

buscar = int(input("\nNúmero a buscar: "))

encontrado = False
posicion = -1

for i in range(len(lista)):
    if lista[i] == buscar:
        encontrado = True
        posicion = i
        break

if encontrado:
    print(f"\nEl número {buscar} se encuentra en la posición {posicion}.")
else:
    print(f"\nEl número {buscar} no se encuentra en la lista.")
